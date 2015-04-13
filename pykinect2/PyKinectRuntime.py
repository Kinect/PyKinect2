from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *

import ctypes
import _ctypes 
from _ctypes import COMError
import comtypes
import sys
import numpy
import time
import importlib 

if sys.hexversion >= 0x03000000: 
    import _thread as thread
    from queue import Queue, Empty
else:
    import thread
    from Queue import Queue, Empty

KINECT_MAX_BODY_COUNT = 6


class PyKinectRuntime(object):
    """manages Kinect objects and simplifying access to them"""
    def __init__(self, frame_source_types, max_frames_stored=2):
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
        
        #self._color_frame_ready = PyKinectV2._event()
        #self._depth_frame_ready = PyKinectV2._event()
        #self._body_frame_ready = PyKinectV2._event()
        #self._body_index_frame_ready = PyKinectV2._event()
        #self._infrared_frame_ready = PyKinectV2._event()
        #self._long_exposure_infrared_frame_ready = PyKinectV2._event()
        #self._audio_frame_ready = PyKinectV2._event()

        self._close_event = ctypes.windll.kernel32.CreateEventW(None, False, False, None)

        self._color_frame_arrived_event = 0
        self._depth_frame_arrived_event = 0
        self._body_frame_arrived_event = 0
        self._body_index_frame_arrived_event = 0
        self._infrared_frame_arrived_event = 0  
        self._long_exposure_infrared_frame_arrived_event = 0
        self._audio_frame_arrived_event = 0

        #initialize sensor
        self._sensor = ctypes.POINTER(PyKinectV2.IKinectSensor)()
        hres = ctypes.windll.kinect20.GetDefaultKinectSensor(ctypes.byref(self._sensor)) 
        hres = self._sensor.Open() 

        self._mapper = self._sensor.CoordinateMapper

        self.frame_source_types = frame_source_types
        self.max_body_count = KINECT_MAX_BODY_COUNT

        self._handles = (ctypes.c_voidp * 8)()
        self._handles[0] = self._close_event
        self._handles[1] = self._close_event
        self._handles[2] = self._close_event
        self._handles[3] = self._close_event
        self._handles[4] = self._close_event
        self._handles[5] = self._close_event
        self._handles[6] = self._close_event
        self._handles[7] = self._close_event

        self._waitHandleCount = 1

        self._color_source = self._sensor.ColorFrameSource 
        self.color_frame_desc = self._color_source.FrameDescription
        self._depth_source = self._sensor.DepthFrameSource 
        self.depth_frame_desc = self._depth_source.FrameDescription 
        self._body_index_source = self._sensor.BodyIndexFrameSource 
        self.body_index_frame_desc = self._body_index_source.FrameDescription 
        self._body_source = self._sensor.BodyFrameSource 
        self._body_frame_data = ctypes.POINTER(ctypes.POINTER(IBody))
        self.max_body_count = self._body_source.BodyCount

        self._color_frame_data = None 
        self._depth_frame_data = None 
        self._body_frame_data = None
        self._body_index_frame_data = None
        self._infrared_frame_data = None
        self._long_exposure_infrared_frame_data = None
        self._audio_frame_data = None

        if(self.frame_source_types & FrameSourceTypes_Color):
            self._color_frame_data = ctypes.POINTER(ctypes.c_ubyte) 
            self._color_frame_data_capacity = ctypes.c_uint(self.color_frame_desc.Width * self.color_frame_desc.Height * 4)
            self._color_frame_data_type = ctypes.c_ubyte * self._color_frame_data_capacity.value
            self._color_frame_data = ctypes.cast(self._color_frame_data_type(), ctypes.POINTER(ctypes.c_ubyte))
            self._color_frame_reader = self._color_source.OpenReader()
            self._color_frame_arrived_event = self._color_frame_reader.SubscribeFrameArrived()
            self._handles[self._waitHandleCount] = self._color_frame_arrived_event
            self._waitHandleCount += 1

        if(self.frame_source_types & FrameSourceTypes_Depth):
            self._depth_frame_data = ctypes.POINTER(ctypes.c_ushort) 
            self._depth_frame_data_capacity = ctypes.c_uint(self.depth_frame_desc.Width * self.depth_frame_desc.Height)
            self._depth_frame_data_type = ctypes.c_ushort * self._depth_frame_data_capacity.value
            self._depth_frame_data = ctypes.cast(self._depth_frame_data_type(), ctypes.POINTER(ctypes.c_ushort))
            self._depth_frame_reader = self._depth_source.OpenReader()
            self._depth_frame_arrived_event = self._depth_frame_reader.SubscribeFrameArrived()
            self._handles[self._waitHandleCount] = self._depth_frame_arrived_event
            self._waitHandleCount += 1

        if(self.frame_source_types & FrameSourceTypes_BodyIndex):
            self._body_index_frame_data = ctypes.POINTER(ctypes.c_ubyte) 
            self._body_index_frame_data_capacity = ctypes.c_uint(self.body_index_frame_desc.Width * self.body_index_frame_desc.Height)
            self._body_index_frame_data_type = ctypes.c_ubyte * self._body_index_frame_data_capacity.value
            self._body_index_frame_data = ctypes.cast(self._body_index_frame_data_type(), ctypes.POINTER(ctypes.c_ubyte))
            self._body_index_frame_reader = self._body_index_source.OpenReader()
            self._body_index_frame_arrived_event = self._body_index_frame_reader.SubscribeFrameArrived()
            self._handles[self._waitHandleCount] = self._body_index_frame_arrived_event
            self._waitHandleCount += 1

        self._body_frame_data = None 
        if(self.frame_source_types & FrameSourceTypes_Body):
            self._body_frame_data_capacity = ctypes.c_uint(self.max_body_count)
            self._body_frame_data_type = ctypes.POINTER(IBody) * self._body_frame_data_capacity.value
            self._body_frame_data = ctypes.cast(self._body_frame_data_type(), ctypes.POINTER(ctypes.POINTER(IBody)))
            self._body_frame_reader = self._body_source.OpenReader()
            self._body_frame_arrived_event = self._body_frame_reader.SubscribeFrameArrived()
            self._handles[self._waitHandleCount] = self._body_frame_arrived_event
            self._waitHandleCount += 1

        thread.start_new_thread(self.kinect_frame_thread, ())

        self._color_frame_queue = Queue(maxsize=max_frames_stored)
        self._depth_frame_queue = Queue(maxsize=max_frames_stored)
        self._body_frame_queue = Queue(maxsize=max_frames_stored)
        self._body_index_frame_queue = Queue(maxsize=max_frames_stored)
        self._infrared_frame_queue = Queue(maxsize=max_frames_stored)
        self._long_exposure_infrared_frame_queue = Queue(maxsize=max_frames_stored)
        self._audio_frame_queue = Queue(maxsize=max_frames_stored)

    def close(self):
        if self._sensor is not None:
            ctypes.windll.kernel32.SetEvent(self._close_event)
            ctypes.windll.kernel32.CloseHandle(self._close_event)

            self._color_frame_reader = None
            self._depth_frame_reader = None
            self._body_index_frame_reader = None
            self._body_frame_reader = None

            self._color_source = None
            self._depth_source = None
            self._body_index_source = None
            self._body_source = None

            self._body_frame_data = None

            self._sensor.Close()
            self._sensor = None

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def surface_as_array(self, surface_buffer_interface):
       address = ctypes.c_void_p()
       size = self.Py_ssize_t()
       self._PyObject_AsWriteBuffer(surface_buffer_interface,
                              ctypes.byref(address), ctypes.byref(size))
       bytes = (ctypes.c_byte * size.value).from_address(address.value)
       bytes.object = surface_buffer_interface
       return bytes

    def get_last_color_frame(self, blocking=True):
        try:
            return self._color_frame_queue.get(block=blocking)
        except Empty:
            return None

    def get_last_depth_frame(self, blocking=True):
        try:
            return self._depth_frame_queue.get(block=blocking)
        except Empty:
            return None

    def get_last_body_frame(self, blocking=True):
        try:
            return self._body_frame_queue.get(block=blocking)
        except Empty:
            return None

    def get_last_body_index_frame(self, blocking=True):
        try:
            return self._body_index_frame_queue.get(block=blocking)
        except Empty:
            return None

    def body_joint_to_color_space(self, joint): 
        return self._mapper.MapCameraPointToColorSpace(joint.Position) 

    def body_joints_to_color_space(self, joints):
        joint_points = numpy.ndarray((PyKinectV2.JointType_Count), dtype=numpy.object)

        for j in range(0, PyKinectV2.JointType_Count):
            joint_points[j] = self.body_joint_to_color_space(joints[j])

        return joint_points

    def kinect_frame_thread(self):
        while 1:    
                wait = ctypes.windll.kernel32.WaitForMultipleObjects(self._waitHandleCount, self._handles, False, PyKinectV2._INFINITE)
               
                if wait == 0: 
                    break
                
                if self._handles[wait] == self._color_frame_arrived_event: 
                    self.handle_color_arrived(wait)
                elif self._handles[wait] == self._depth_frame_arrived_event: 
                    self.handle_depth_arrived(wait)
                elif self._handles[wait] == self._body_frame_arrived_event: 
                    self.handle_body_arrived(wait)
                elif self._handles[wait] == self._body_index_frame_arrived_event: 
                    self.handle_body_index_arrived(wait)
                elif self._handles[wait] == self._infrared_frame_arrived_event: 
                    self.handle_infrared_arrived(wait)
                elif self._handles[wait] == self._long_exposure_infrared_frame_arrived_event: 
                    self.handle_long_exposure_infrared_arrived(wait)
                elif self._handles[wait] == self._audio_frame_arrived_event: 
                    self.handle_audio_arrived(wait)
                else:
                    break

    def handle_color_arrived(self, handle_index):
        colorFrameEventData = self._color_frame_reader.GetFrameArrivedEventData(self._handles[handle_index])
        colorFrameRef = colorFrameEventData.FrameReference
        try:
            colorFrame = colorFrameRef.AcquireFrame()
            try:
                colorFrame.CopyConvertedFrameDataToArray(self._color_frame_data_capacity, self._color_frame_data, PyKinectV2.ColorImageFormat_Bgra)
                self._color_frame_queue.put(numpy.copy(numpy.ctypeslib.as_array(self._color_frame_data, shape=(self._color_frame_data_capacity.value,))))
            except:
                pass
        except:
            pass

    def handle_depth_arrived(self, handle_index):
        depthFrameEventData = self._depth_frame_reader.GetFrameArrivedEventData(self._handles[handle_index])
        depthFrameRef = depthFrameEventData.FrameReference
        try:
            depthFrame = depthFrameRef.AcquireFrame()
            try:
                depthFrame.CopyFrameDataToArray(self._depth_frame_data_capacity, self._depth_frame_data)
                self._depth_frame_queue.put(numpy.copy(numpy.ctypeslib.as_array(self._depth_frame_data, shape=(self._depth_frame_data_capacity.value,))))
            except:
                pass
        except:
            pass
  
    def handle_body_arrived(self, handle_index):
        bodyFrameEventData = self._body_frame_reader.GetFrameArrivedEventData(self._handles[handle_index])
        bofyFrameRef = bodyFrameEventData.FrameReference
        try:
            bodyFrame = bofyFrameRef.AcquireFrame()

            try: 
                bodyFrame.GetAndRefreshBodyData(self._body_frame_data_capacity, self._body_frame_data)
                self._body_frame_queue.put(KinectBodyFrameData(bodyFrame, self._body_frame_data, self.max_body_count).copy())

                # need these 2 lines as a workaround for handling IBody referencing exception 
                self._body_frame_data = None
                self._body_frame_data = ctypes.cast(self._body_frame_data_type(), ctypes.POINTER(ctypes.POINTER(IBody)))

            except:
                pass
        except:
            pass

    def handle_body_index_arrived(self, handle_index):
        bodyIndexFrameEventData = self._body_index_frame_reader.GetFrameArrivedEventData(self._handles[handle_index])
        bodyIndexFrameRef = bodyIndexFrameEventData.FrameReference
        try:
            bodyIndexFrame = bodyIndexFrameRef.AcquireFrame()
            try:
                bodyIndexFrame.CopyFrameDataToArray(self._body_index_frame_data_capacity, self._body_index_frame_data)
                self._body_index_frame_queue.put(numpy.copy(numpy.ctypeslib.as_array(self._body_index_frame_data, shape=(self._body_index_frame_data_capacity.value,))))
            except:
                pass
        except:
            pass

    def handle_infrared_arrived(self, handle_index):
        pass 

    def handle_long_exposure_infrared_arrived(self, handle_index):
        pass 

    def handle_audio_arrived(self, handle_index):
        pass 


class KinectBody(object): 
    def __init__(self, body = None):
        self.is_restricted = False
        self.tracking_id = -1

        self.is_tracked = False 
        
        if body is not None: 
            self.is_tracked = body.IsTracked

        if self.is_tracked:
            self.is_restricted = body.IsRestricted
            self.tracking_id = body.TrackingId
            self.engaged = body.Engaged
            self.lean = body.Lean
            self.lean_tracking_state = body.LeanTrackingState
            self.hand_left_state = body.HandLeftState
            self.hand_left_confidence = body.HandLeftConfidence
            self.hand_right_state = body.HandRightState
            self.hand_right_confidence = body.HandRightConfidence
            self.clipped_edges = body.ClippedEdges

            joints = ctypes.POINTER(PyKinectV2._Joint)
            joints_capacity = ctypes.c_uint(PyKinectV2.JointType_Count)
            joints_data_type = PyKinectV2._Joint * joints_capacity.value
            joints = ctypes.cast(joints_data_type(), ctypes.POINTER(PyKinectV2._Joint))
            body.GetJoints(PyKinectV2.JointType_Count, joints)
            self.joints = joints

            joint_orientations = ctypes.POINTER(PyKinectV2._JointOrientation)
            joint_orientations_data_type = PyKinectV2._JointOrientation * joints_capacity.value
            joint_orientations = ctypes.cast(joint_orientations_data_type(), ctypes.POINTER(PyKinectV2._JointOrientation))
            body.GetJointOrientations(PyKinectV2.JointType_Count, joint_orientations)
            self.joint_orientations = joint_orientations 


class KinectBodyFrameData(object): 
    def __init__(self, bodyFrame, body_frame_data, max_body_count):
        self.bodies = None
        self.floor_clip_plane = None
        if bodyFrame is not None:
            self.floor_clip_plane = bodyFrame.FloorClipPlane

            self.bodies = numpy.ndarray((max_body_count), dtype=numpy.object)
            for i in range(0, max_body_count):
               self.bodies[i] = KinectBody(body_frame_data[i])

    def copy(self):
        res = KinectBodyFrameData(None, None, 0)
        res.floor_clip_plane = self.floor_clip_plane
        res.bodies = numpy.copy(self.bodies)
        return res 

