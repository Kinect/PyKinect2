import PyKinectV2
from PyKinectV2 import *

import ctypes
import _ctypes 
from _ctypes import COMError
import comtypes
import pygame
import sys

import importlib 

if sys.hexversion >= 0x03000000: 
    import _thread as thread
else:
    import thread 

class GameKinectRuntime(object):
    def __init__(self):
        # recipe to get address of surface: http://archives.seul.org/pygame/users/Apr-2008/msg00218.html
        is_64bits = sys.maxsize > 2**32
        if not is_64bits:
           self.Py_ssize_t = ctypes.c_int
        else:
           self.Py_ssize_t = ctypes.c_int64

        self._PyObject_AsWriteBuffer = ctypes.pythonapi.PyObject_AsWriteBuffer
        self._PyObject_AsWriteBuffer.restype = ctypes.c_int
        self._PyObject_AsWriteBuffer.argtypes = [ctypes.py_object,
                                          ctypes.POINTER(ctypes.c_void_p),
                                          ctypes.POINTER(self.Py_ssize_t)]
        
        self._color_frame_ready = PyKinectV2._event()
        
        # Start code here
        pygame.init()

        #initialize sensor
        self._sensor = ctypes.POINTER(PyKinectV2.IKinectSensor)()
        hres = ctypes.windll.kinect20.GetDefaultKinectSensor(ctypes.byref(self._sensor)) 
        hres = self._sensor.Open() 

        self._colorSource = self._sensor.ColorFrameSource 
        self._frameDesc = self._colorSource.FrameDescription 
        self._colorReader = self._colorSource.OpenReader()

        self._frame_data = ctypes.POINTER(ctypes.c_ubyte) 
        self._frameDataCapacity = ctypes.c_uint(self._frameDesc.Width * self._frameDesc.Height * 4)
        self._frame_data_type = ctypes.c_ubyte * self._frameDataCapacity.value
        self._needFrameData = True

 
        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1), 0, 32)

        pygame.display.set_caption("Kinect for Windows v2 Game")
 
        # Loop until the user clicks the close button.
        self._done = False
 
        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        self._frameSurface = pygame.Surface((self._frameDesc.Width, self._frameDesc.Height), 0, 32)
        self._frameArrivedEvent = self._colorReader.SubscribeFrameArrived();
        self._screen_lock = thread.allocate()

    def surface_as_array(self, surface):
       buffer_interface = surface.get_buffer()
       address = ctypes.c_void_p()
       size = self.Py_ssize_t()
       self._PyObject_AsWriteBuffer(buffer_interface,
                              ctypes.byref(address), ctypes.byref(size))
       bytes = (ctypes.c_byte * size.value).from_address(address.value)
       bytes.object = buffer_interface
       return bytes

    def kinect_thread(self):
        handles = (ctypes.c_voidp * 1)()
        handles[0] = self._frameArrivedEvent
        while 1:    
                wait = ctypes.windll.kernel32.WaitForMultipleObjects(1, handles, False, PyKinectV2._INFINITE)
                if wait == 0:
                    colorFrameEventData = self._colorReader.GetFrameArrivedEventData(handles[0])
                    colorFrameRef = colorFrameEventData.FrameReference
                    try:
                        colorFrame = colorFrameRef.AcquireFrame()
                        self._color_frame_ready.fire(colorFrame) 
                        colorFrame = None
                    except:
                        pass
                    colorFrameRef = None
                    colorFrameEventData = None


    def video_frame_ready_proc(self, frame):
        #self = args[0]
        #frame = args[1]
        with self._screen_lock:
            if self._needFrameData:
                self._needFrameData = False
                self._frame_data = ctypes.cast(self._frame_data_type(), ctypes.POINTER(ctypes.c_ubyte))

            try:
                frame.CopyConvertedFrameDataToArray(self._frameDataCapacity, self._frame_data, PyKinectV2.ColorImageFormat_Bgra)
            except Exception as ex:
                pass

            self._frameSurface.lock()
            address = self.surface_as_array(self._frameSurface)
            ctypes.memmove(address, self._frame_data, self._frameDataCapacity.value)
            del address
            self._frameSurface.unlock()
         
            frame = None

            hToW = float(self._frameSurface.get_height()) / self._frameSurface.get_width()
            tagetHeight = int(hToW * self._screen.get_width())
            surfaceToDraw = pygame.transform.scale(self._frameSurface, (self._screen.get_width(), tagetHeight));
            #surfaceToDraw = pygame.transform.flip(surfaceToDraw, True, False)
            self._screen.blit(surfaceToDraw, (0,0))
            surfaceToDraw = None
            pygame.display.update()

    def Run(self): 
        #register color_frame_ready event and start kinect thread
        self._color_frame_ready += self.video_frame_ready_proc
        thread.start_new_thread(self.kinect_thread, ())

        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag that we are done so we exit this loop
 
            # --- Game logic should go here
 
            # --- Drawing code should go here

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
 
            # --- Limit to 60 frames per second
            self._clock.tick(60)
 
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit()

__main__ = "Kinect v2 Game" 
game = GameKinectRuntime();
game.Run();