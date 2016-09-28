# -*- coding: mbcs -*-
typelib_path = 'c:\\Users\\vladkol\\Documents\\PyKinect2\\idl\\Kinect.tlb'
_lcid = 0 # change this if required
import ctypes 
import comtypes
from ctypes import *
from comtypes import *
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
STRING = c_char_p
INT_PTR = c_int
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import _FILETIME
WSTRING = c_wchar_p

from _ctypes import COMError
comtypes.hresult.E_PENDING = 0x8000000A 

import numpy.distutils.system_info as sysinfo


class _event(object):
    """class used for adding/removing/invoking a set of listener functions"""
    __slots__ = ['handlers']
        
    def __init__(self):
        self.handlers = []
    
    def __iadd__(self, other):
        self.handlers.append(other)
        return self
        
    def __isub__(self, other):
        self.handlers.remove(other)
        return self

    def fire(self, *args):
        for handler in self.handlers:
            handler(*args)

class IBody(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{46AEF731-98B0-4D18-827B-933758678F4A}')
    _idlflags_ = []
class _Joint(Structure):
    pass
class _JointOrientation(Structure):
    pass

# values for enumeration '_DetectionResult'
DetectionResult_Unknown = 0
DetectionResult_No = 1
DetectionResult_Maybe = 2
DetectionResult_Yes = 3
_DetectionResult = c_int # enum

# values for enumeration '_HandState'
HandState_Unknown = 0
HandState_NotTracked = 1
HandState_Open = 2
HandState_Closed = 3
HandState_Lasso = 4
_HandState = c_int # enum

# values for enumeration '_TrackingConfidence'
TrackingConfidence_Low = 0
TrackingConfidence_High = 1
_TrackingConfidence = c_int # enum
class _PointF(Structure):
    pass

# values for enumeration '_TrackingState'
TrackingState_NotTracked = 0
TrackingState_Inferred = 1
TrackingState_Tracked = 2
_TrackingState = c_int # enum
IBody._methods_ = [
    COMMETHOD([], HRESULT, 'GetJoints',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(_Joint), 'joints' )),
    COMMETHOD([], HRESULT, 'GetJointOrientations',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(_JointOrientation), 'jointOrientations' )),
    COMMETHOD(['propget'], HRESULT, 'Engaged',
              ( ['retval', 'out'], POINTER(_DetectionResult), 'detectionResult' )),
    COMMETHOD([], HRESULT, 'GetExpressionDetectionResults',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(_DetectionResult), 'detectionResults' )),
    COMMETHOD([], HRESULT, 'GetActivityDetectionResults',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(_DetectionResult), 'detectionResults' )),
    COMMETHOD([], HRESULT, 'GetAppearanceDetectionResults',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(_DetectionResult), 'detectionResults' )),
    COMMETHOD(['propget'], HRESULT, 'HandLeftState',
              ( ['retval', 'out'], POINTER(_HandState), 'handState' )),
    COMMETHOD(['propget'], HRESULT, 'HandLeftConfidence',
              ( ['retval', 'out'], POINTER(_TrackingConfidence), 'confidence' )),
    COMMETHOD(['propget'], HRESULT, 'HandRightState',
              ( ['retval', 'out'], POINTER(_HandState), 'handState' )),
    COMMETHOD(['propget'], HRESULT, 'HandRightConfidence',
              ( ['retval', 'out'], POINTER(_TrackingConfidence), 'confidence' )),
    COMMETHOD(['propget'], HRESULT, 'ClippedEdges',
              ( ['retval', 'out'], POINTER(c_ulong), 'ClippedEdges' )),
    COMMETHOD(['propget'], HRESULT, 'TrackingId',
              ( ['retval', 'out'], POINTER(c_ulonglong), 'TrackingId' )),
    COMMETHOD(['propget'], HRESULT, 'IsTracked',
              ( ['retval', 'out'], POINTER(c_bool), 'tracked' )),
    COMMETHOD(['propget'], HRESULT, 'IsRestricted',
              ( ['retval', 'out'], POINTER(c_bool), 'IsRestricted' )),
    COMMETHOD(['propget'], HRESULT, 'Lean',
              ( ['retval', 'out'], POINTER(_PointF), 'amount' )),
    COMMETHOD(['propget'], HRESULT, 'LeanTrackingState',
              ( ['retval', 'out'], POINTER(_TrackingState), 'TrackingState' )),
]
################################################################
## code template for IBody implementation
##class IBody_Impl(object):
##    def GetJoints(self, capacity):
##        '-no docstring-'
##        #return joints
##
##    @property
##    def IsTracked(self):
##        '-no docstring-'
##        #return tracked
##
##    @property
##    def HandLeftState(self):
##        '-no docstring-'
##        #return handState
##
##    @property
##    def HandLeftConfidence(self):
##        '-no docstring-'
##        #return confidence
##
##    @property
##    def TrackingId(self):
##        '-no docstring-'
##        #return TrackingId
##
##    @property
##    def Lean(self):
##        '-no docstring-'
##        #return amount
##
##    @property
##    def Engaged(self):
##        '-no docstring-'
##        #return detectionResult
##
##    @property
##    def HandRightState(self):
##        '-no docstring-'
##        #return handState
##
##    @property
##    def ClippedEdges(self):
##        '-no docstring-'
##        #return ClippedEdges
##
##    def GetJointOrientations(self, capacity):
##        '-no docstring-'
##        #return jointOrientations
##
##    def GetExpressionDetectionResults(self, capacity):
##        '-no docstring-'
##        #return detectionResults
##
##    @property
##    def IsRestricted(self):
##        '-no docstring-'
##        #return IsRestricted
##
##    def GetActivityDetectionResults(self, capacity):
##        '-no docstring-'
##        #return detectionResults
##
##    @property
##    def HandRightConfidence(self):
##        '-no docstring-'
##        #return confidence
##
##    def GetAppearanceDetectionResults(self, capacity):
##        '-no docstring-'
##        #return detectionResults
##
##    @property
##    def LeanTrackingState(self):
##        '-no docstring-'
##        #return TrackingState
##

class IColorCameraSettings(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DBF802AB-0ADF-485A-A844-CF1C7956D039}')
    _idlflags_ = []
IColorCameraSettings._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'ExposureTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'ExposureTime' )),
    COMMETHOD(['propget'], HRESULT, 'FrameInterval',
              ( ['retval', 'out'], POINTER(c_longlong), 'FrameInterval' )),
    COMMETHOD(['propget'], HRESULT, 'Gain',
              ( ['retval', 'out'], POINTER(c_float), 'Gain' )),
    COMMETHOD(['propget'], HRESULT, 'Gamma',
              ( ['retval', 'out'], POINTER(c_float), 'Gamma' )),
]
################################################################
## code template for IColorCameraSettings implementation
##class IColorCameraSettings_Impl(object):
##    @property
##    def ExposureTime(self):
##        '-no docstring-'
##        #return ExposureTime
##
##    @property
##    def FrameInterval(self):
##        '-no docstring-'
##        #return FrameInterval
##
##    @property
##    def Gamma(self):
##        '-no docstring-'
##        #return Gamma
##
##    @property
##    def Gain(self):
##        '-no docstring-'
##        #return Gain
##

class IAudioBeamFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B5733DE9-6ECF-46B2-8B23-A16D71F1A75C}')
    _idlflags_ = []
class IAudioBeamFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E0DBE62D-2045-4571-8D1D-ECF3981E3C3D}')
    _idlflags_ = []
class IAudioBeamFrameList(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5393C8B9-C044-49CB-BDD6-23DFFFD7427E}')
    _idlflags_ = []
class IAudioSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{52D1D743-AED1-4E61-8AF8-19EF287A662C}')
    _idlflags_ = []
IAudioBeamFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeamFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestBeamFrames',
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeamFrameList)), 'audioBeamFrameList' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'AudioSource',
              ( ['retval', 'out'], POINTER(POINTER(IAudioSource)), 'AudioSource' )),
]
################################################################
## code template for IAudioBeamFrameReader implementation
##class IAudioBeamFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    @property
##    def AudioSource(self):
##        '-no docstring-'
##        #return AudioSource
##
##    def AcquireLatestBeamFrames(self):
##        '-no docstring-'
##        #return audioBeamFrameList
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##

class IDepthFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D8600853-8835-44F9-84A7-E617CDD7DFDD}')
    _idlflags_ = []
class IFrameDescription(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{21F6EFB7-EB6D-48F4-9C08-181A87BF0C98}')
    _idlflags_ = []
class IDepthFrameSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C428D558-5E46-490A-B699-D1DDDAA24150}')
    _idlflags_ = []
IDepthFrame._methods_ = [
    COMMETHOD([], HRESULT, 'CopyFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ushort), 'frameData' )),
    COMMETHOD([], HRESULT, 'AccessUnderlyingBuffer',
              ( [], POINTER(c_uint), 'capacity' ),
              ( [], POINTER(POINTER(c_ushort)), 'buffer' )), #'out'
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
    COMMETHOD(['propget'], HRESULT, 'DepthFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameSource)), 'DepthFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'DepthMinReliableDistance',
              ( ['retval', 'out'], POINTER(c_ushort), 'DepthMinReliableDistance' )),
    COMMETHOD(['propget'], HRESULT, 'DepthMaxReliableDistance',
              ( ['retval', 'out'], POINTER(c_ushort), 'DepthMaxReliableDistance' )),
]
################################################################
## code template for IDepthFrame implementation
##class IDepthFrame_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def DepthMaxReliableDistance(self):
##        '-no docstring-'
##        #return DepthMaxReliableDistance
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def CopyFrameDataToArray(self, capacity):
##        '-no docstring-'
##        #return frameData
##
##    def AccessUnderlyingBuffer(self):
##        '-no docstring-'
##        #return capacity, buffer
##
##    @property
##    def DepthMinReliableDistance(self):
##        '-no docstring-'
##        #return DepthMinReliableDistance
##
##    @property
##    def DepthFrameSource(self):
##        '-no docstring-'
##        #return DepthFrameSource
##

class IDepthFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2B01BCB8-29D7-4726-860C-6DA56664AA81}')
    _idlflags_ = []
class IDepthFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{20621E5E-ABC9-4EBD-A7EE-4C77EDD0152A}')
    _idlflags_ = []
IDepthFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameReference)), 'depthFrameReference' )),
]
################################################################
## code template for IDepthFrameArrivedEventArgs implementation
##class IDepthFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return depthFrameReference
##

class IColorFrameSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{57621D82-D8EE-4783-B412-F7E019C96CFD}')
    _idlflags_ = []
class IFrameCapturedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{24CBAB8E-DF1A-4FA8-827E-C1B27A44A3A1}')
    _idlflags_ = []
class IColorFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9BEA498C-C59C-4653-AAF9-D884BAB7C35B}')
    _idlflags_ = []

# values for enumeration '_ColorImageFormat'
ColorImageFormat_None = 0
ColorImageFormat_Rgba = 1
ColorImageFormat_Yuv = 2
ColorImageFormat_Bgra = 3
ColorImageFormat_Bayer = 4
ColorImageFormat_Yuy2 = 5
_ColorImageFormat = c_int # enum
class IKinectSensor(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3C6EBA94-0DE1-4360-B6D4-653A10794C8B}')
    _idlflags_ = []
IColorFrameSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameReader)), 'reader' )),
    COMMETHOD([], HRESULT, 'CreateFrameDescription',
              ( [], _ColorImageFormat, 'format' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'rawFrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
]
################################################################
## code template for IColorFrameSource implementation
##class IColorFrameSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return rawFrameDescription
##
##    def CreateFrameDescription(self, format):
##        '-no docstring-'
##        #return FrameDescription
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

class Library(object):
    u'Kinect for Windiws v2 Type Library'
    name = u'Kinect'
    _reg_typelib_ = ('{7E31D9B1-D4F2-4DEF-999A-6601F7AB0562}', 1, 0)


# values for enumeration '_Activity'
Activity_EyeLeftClosed = 0
Activity_EyeRightClosed = 1
Activity_MouthOpen = 2
Activity_MouthMoved = 3
Activity_LookingAway = 4
Activity_Count = 5
_Activity = c_int # enum

# values for enumeration '_FrameSourceTypes'
FrameSourceTypes_None = 0
FrameSourceTypes_Color = 1
FrameSourceTypes_Infrared = 2
FrameSourceTypes_LongExposureInfrared = 4
FrameSourceTypes_Depth = 8
FrameSourceTypes_BodyIndex = 16
FrameSourceTypes_Body = 32
FrameSourceTypes_Audio = 64
_FrameSourceTypes = c_int # enum

# values for enumeration '_KinectCapabilities'
KinectCapabilities_None = 0
KinectCapabilities_Vision = 1
KinectCapabilities_Audio = 2
KinectCapabilities_Face = 4
KinectCapabilities_Expressions = 8
KinectCapabilities_Gamechat = 16
_KinectCapabilities = c_int # enum
class IAudioBeamFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1BD29D0E-6304-4AFB-9C85-77CFE3DC4FCE}')
    _idlflags_ = []
IAudioBeamFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeamFrameReference)), 'audioBeamFrameReference' )),
]
################################################################
## code template for IAudioBeamFrameArrivedEventArgs implementation
##class IAudioBeamFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return audioBeamFrameReference
##

class ILongExposureInfraredFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2AF23594-0115-417B-859F-A0E3FFB690D2}')
    _idlflags_ = []
class ILongExposureInfraredFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D73D4B5E-E329-4F04-894C-0C97482690D4}')
    _idlflags_ = []
class ILongExposureInfraredFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D1199394-9A42-4577-BE12-90A38B72282C}')
    _idlflags_ = []
class ILongExposureInfraredFrameSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D7150EDA-EDA2-4673-B4F8-E3C76D1F402B}')
    _idlflags_ = []
ILongExposureInfraredFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrame)), 'longExposureInfraredFrame' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'LongExposureInfraredFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameSource)), 'LongExposureInfraredFrameSource' )),
]
################################################################
## code template for ILongExposureInfraredFrameReader implementation
##class ILongExposureInfraredFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    @property
##    def LongExposureInfraredFrameSource(self):
##        '-no docstring-'
##        #return LongExposureInfraredFrameSource
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return longExposureInfraredFrame
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##


# values for enumeration '_FrameEdges'
FrameEdge_None = 0
FrameEdge_Right = 1
FrameEdge_Left = 2
FrameEdge_Top = 4
FrameEdge_Bottom = 8
_FrameEdges = c_int # enum

# values for enumeration '_FrameCapturedStatus'
FrameCapturedStatus_Unknown = 0
FrameCapturedStatus_Queued = 1
FrameCapturedStatus_Dropped = 2
_FrameCapturedStatus = c_int # enum
IFrameCapturedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameType',
              ( ['retval', 'out'], POINTER(_FrameSourceTypes), 'FrameType' )),
    COMMETHOD(['propget'], HRESULT, 'FrameStatus',
              ( ['retval', 'out'], POINTER(_FrameCapturedStatus), 'FrameStatus' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IFrameCapturedEventArgs implementation
##class IFrameCapturedEventArgs_Impl(object):
##    @property
##    def FrameStatus(self):
##        '-no docstring-'
##        #return FrameStatus
##
##    @property
##    def FrameType(self):
##        '-no docstring-'
##        #return FrameType
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##

class IKinectSensorCollection(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{EF1FE50F-641C-4FB8-B7BA-C2A8295E1C74}')
    _idlflags_ = []
class IEnumKinectSensor(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E7DEB409-8F82-4D72-9F91-2BB1D2025DC4}')
    _idlflags_ = []
IKinectSensorCollection._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'Enumerator',
              ( ['retval', 'out'], POINTER(POINTER(IEnumKinectSensor)), 'Enumerator' )),
]
################################################################
## code template for IKinectSensorCollection implementation
##class IKinectSensorCollection_Impl(object):
##    @property
##    def Enumerator(self):
##        '-no docstring-'
##        #return Enumerator
##

IAudioBeamFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireBeamFrames',
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeamFrameList)), 'audioBeamFrameList' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IAudioBeamFrameReference implementation
##class IAudioBeamFrameReference_Impl(object):
##    def AcquireBeamFrames(self):
##        '-no docstring-'
##        #return audioBeamFrameList
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##

class ILongExposureInfraredFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{10043A3E-0DAA-409C-9944-A6FC66C85AF7}')
    _idlflags_ = []
ILongExposureInfraredFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameReference)), 'longExposureInfraredFrameReference' )),
]
################################################################
## code template for ILongExposureInfraredFrameArrivedEventArgs implementation
##class ILongExposureInfraredFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return longExposureInfraredFrameReference
##

class IBodyFrameSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BB94A78A-458C-4608-AC69-34FEAD1E3BAE}')
    _idlflags_ = []
class IBodyFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{45532DF5-A63C-418F-A39F-C567936BC051}')
    _idlflags_ = []
IBodyFrameSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD(['propget'], HRESULT, 'BodyCount',
              ( ['retval', 'out'], POINTER(c_int), 'BodyCount' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameReader)), 'reader' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
    COMMETHOD([], HRESULT, 'OverrideHandTracking',
              ( [], c_ulonglong, 'TrackingId' )),
    COMMETHOD([], HRESULT, 'OverrideAndReplaceHandTracking',
              ( [], c_ulonglong, 'oldTrackingId' ),
              ( [], c_ulonglong, 'newTrackingId' )),
]
################################################################
## code template for IBodyFrameSource implementation
##class IBodyFrameSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    def OverrideHandTracking(self, TrackingId):
##        '-no docstring-'
##        #return 
##
##    def OverrideAndReplaceHandTracking(self, oldTrackingId, newTrackingId):
##        '-no docstring-'
##        #return 
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def BodyCount(self):
##        '-no docstring-'
##        #return BodyCount
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

class IAudioBeamFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{07AADCC8-EC4A-42F8-90A9-C72ECF0A1D06}')
    _idlflags_ = []
IAudioBeamFrameList._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'BeamCount',
              ( ['retval', 'out'], POINTER(c_uint), 'count' )),
    COMMETHOD([], HRESULT, 'OpenAudioBeamFrame',
              ( [], c_uint, 'index' ),
              ( ['out'], POINTER(POINTER(IAudioBeamFrame)), 'audioBeamFrame' )),
]
################################################################
## code template for IAudioBeamFrameList implementation
##class IAudioBeamFrameList_Impl(object):
##    def OpenAudioBeamFrame(self, index):
##        '-no docstring-'
##        #return audioBeamFrame
##
##    @property
##    def BeamCount(self):
##        '-no docstring-'
##        #return count
##


# values for enumeration '_Appearance'
Appearance_WearingGlasses = 0
Appearance_Count = 1
_Appearance = c_int # enum
class IColorFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{82A2E32F-4AE5-4614-88BB-DCC5AE0CEAED}')
    _idlflags_ = []
class IColorFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{39D05803-8803-4E86-AD9F-13F6954E4ACA}')
    _idlflags_ = []
IColorFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrame)), 'colorFrame' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'ColorFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameSource)), 'ColorFrameSource' )),
]
################################################################
## code template for IColorFrameReader implementation
##class IColorFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def ColorFrameSource(self):
##        '-no docstring-'
##        #return ColorFrameSource
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return colorFrame
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##


# values for enumeration '_KinectAudioCalibrationState'
KinectAudioCalibrationState_Unknown = 0
KinectAudioCalibrationState_CalibrationRequired = 1
KinectAudioCalibrationState_Calibrated = 2
_KinectAudioCalibrationState = c_int # enum
ILongExposureInfraredFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrame)), 'longExposureInfraredFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for ILongExposureInfraredFrameReference implementation
##class ILongExposureInfraredFrameReference_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return longExposureInfraredFrame
##

class IDepthFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{81C0C0AB-6E6C-45CB-8625-A5F4D38759A4}')
    _idlflags_ = []
IDepthFrameSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameReader)), 'reader' )),
    COMMETHOD(['propget'], HRESULT, 'DepthMinReliableDistance',
              ( ['retval', 'out'], POINTER(c_ushort), 'DepthMinReliableDistance' )),
    COMMETHOD(['propget'], HRESULT, 'DepthMaxReliableDistance',
              ( ['retval', 'out'], POINTER(c_ushort), 'DepthMaxReliableDistance' )),
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
]
################################################################
## code template for IDepthFrameSource implementation
##class IDepthFrameSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def DepthMaxReliableDistance(self):
##        '-no docstring-'
##        #return DepthMaxReliableDistance
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    @property
##    def DepthMinReliableDistance(self):
##        '-no docstring-'
##        #return DepthMinReliableDistance
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

class IAudioBeam(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F692D23A-14D0-432D-B802-DD381A45A121}')
    _idlflags_ = []
class IAudioBeamSubFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0967DB97-80D1-4BC5-BD2B-4685098D9795}')
    _idlflags_ = []
IAudioBeamFrame._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'AudioSource',
              ( ['retval', 'out'], POINTER(POINTER(IAudioSource)), 'AudioSource' )),
    COMMETHOD(['propget'], HRESULT, 'duration',
              ( ['retval', 'out'], POINTER(c_longlong), 'duration' )),
    COMMETHOD(['propget'], HRESULT, 'AudioBeam',
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeam)), 'AudioBeam' )),
    COMMETHOD(['propget'], HRESULT, 'SubFrameCount',
              ( ['retval', 'out'], POINTER(c_uint), 'pSubFrameCount' )),
    COMMETHOD([], HRESULT, 'GetSubFrame',
              ( [], c_uint, 'subFrameIndex' ),
              ( ['out'], POINTER(POINTER(IAudioBeamSubFrame)), 'audioBeamSubFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTimeStart',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IAudioBeamFrame implementation
##class IAudioBeamFrame_Impl(object):
##    @property
##    def AudioSource(self):
##        '-no docstring-'
##        #return AudioSource
##
##    @property
##    def SubFrameCount(self):
##        '-no docstring-'
##        #return pSubFrameCount
##
##    @property
##    def RelativeTimeStart(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def AudioBeam(self):
##        '-no docstring-'
##        #return AudioBeam
##
##    @property
##    def duration(self):
##        '-no docstring-'
##        #return duration
##
##    def GetSubFrame(self, subFrameIndex):
##        '-no docstring-'
##        #return audioBeamSubFrame
##


# values for enumeration '_JointType'
JointType_SpineBase = 0
JointType_SpineMid = 1
JointType_Neck = 2
JointType_Head = 3
JointType_ShoulderLeft = 4
JointType_ElbowLeft = 5
JointType_WristLeft = 6
JointType_HandLeft = 7
JointType_ShoulderRight = 8
JointType_ElbowRight = 9
JointType_WristRight = 10
JointType_HandRight = 11
JointType_HipLeft = 12
JointType_KneeLeft = 13
JointType_AnkleLeft = 14
JointType_FootLeft = 15
JointType_HipRight = 16
JointType_KneeRight = 17
JointType_AnkleRight = 18
JointType_FootRight = 19
JointType_SpineShoulder = 20
JointType_HandTipLeft = 21
JointType_ThumbLeft = 22
JointType_HandTipRight = 23
JointType_ThumbRight = 24
JointType_Count = 25
_JointType = c_int # enum
class IBodyFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BF5CCA0E-00C1-4D48-837F-AB921E6AEE01}')
    _idlflags_ = []
class IBodyFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{52884F1F-94D7-4B57-BF87-9226950980D5}')
    _idlflags_ = []
IBodyFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrame)), 'bodyFrame' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'BodyFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameSource)), 'BodyFrameSource' )),
]
################################################################
## code template for IBodyFrameReader implementation
##class IBodyFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def BodyFrameSource(self):
##        '-no docstring-'
##        #return BodyFrameSource
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return bodyFrame
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##

class IColorFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5CC49E38-9BBD-48BE-A770-FD30EA405247}')
    _idlflags_ = []
IColorFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameReference)), 'colorFrameReference' )),
]
################################################################
## code template for IColorFrameArrivedEventArgs implementation
##class IColorFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return colorFrameReference
##

ILongExposureInfraredFrame._methods_ = [
    COMMETHOD([], HRESULT, 'CopyFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ushort), 'frameData' )),
    COMMETHOD([], HRESULT, 'AccessUnderlyingBuffer',
              ( [], POINTER(c_uint), 'capacity' ),
              ( [], POINTER(POINTER(c_ushort)), 'buffer' )), #'out'
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
    COMMETHOD(['propget'], HRESULT, 'LongExposureInfraredFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameSource)), 'LongExposureInfraredFrameSource' )),
]
################################################################
## code template for ILongExposureInfraredFrame implementation
##class ILongExposureInfraredFrame_Impl(object):
##    @property
##    def LongExposureInfraredFrameSource(self):
##        '-no docstring-'
##        #return LongExposureInfraredFrameSource
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def CopyFrameDataToArray(self, capacity):
##        '-no docstring-'
##        #return frameData
##
##    def AccessUnderlyingBuffer(self):
##        '-no docstring-'
##        #return capacity, buffer
##

class IAudioBeamList(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3C792C7B-7D95-4C56-9DC7-EF63955781EA}')
    _idlflags_ = []
IAudioSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD(['propget'], HRESULT, 'SubFrameLengthInBytes',
              ( ['retval', 'out'], POINTER(c_uint), 'length' )),
    COMMETHOD(['propget'], HRESULT, 'SubFrameDuration',
              ( ['retval', 'out'], POINTER(c_longlong), 'duration' )),
    COMMETHOD(['propget'], HRESULT, 'MaxSubFrameCount',
              ( ['retval', 'out'], POINTER(c_uint), 'count' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeamFrameReader)), 'reader' )),
    COMMETHOD(['propget'], HRESULT, 'AudioBeams',
              ( ['retval', 'out'], POINTER(POINTER(IAudioBeamList)), 'audioBeamList' )),
    COMMETHOD(['propget'], HRESULT, 'AudioCalibrationState',
              ( ['retval', 'out'], POINTER(_KinectAudioCalibrationState), 'AudioCalibrationState' )),
]
################################################################
## code template for IAudioSource implementation
##class IAudioSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    @property
##    def SubFrameLengthInBytes(self):
##        '-no docstring-'
##        #return length
##
##    @property
##    def AudioCalibrationState(self):
##        '-no docstring-'
##        #return AudioCalibrationState
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def MaxSubFrameCount(self):
##        '-no docstring-'
##        #return count
##
##    @property
##    def AudioBeams(self):
##        '-no docstring-'
##        #return audioBeamList
##
##    @property
##    def SubFrameDuration(self):
##        '-no docstring-'
##        #return duration
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

class _Vector4(Structure):
    pass
_Vector4._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('w', c_float),
]
assert sizeof(_Vector4) == 16, sizeof(_Vector4)
assert alignment(_Vector4) == 4, alignment(_Vector4)
class IBodyIndexFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E9724AA1-EBFA-48F8-9044-E0BE33383B8B}')
    _idlflags_ = []
class IBodyIndexFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{10B7E92E-B4F2-4A36-A459-06B2A4B249DF}')
    _idlflags_ = []
class IBodyIndexFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2CEA0C07-F90C-44DF-A18C-F4D18075EA6B}')
    _idlflags_ = []
class IBodyIndexFrameSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{010F2A40-DC58-44A5-8E57-329A583FEC08}')
    _idlflags_ = []
IBodyIndexFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrame)), 'bodyIndexFrame' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'BodyIndexFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameSource)), 'BodyIndexFrameSource' )),
]
################################################################
## code template for IBodyIndexFrameReader implementation
##class IBodyIndexFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def BodyIndexFrameSource(self):
##        '-no docstring-'
##        #return BodyIndexFrameSource
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return bodyIndexFrame
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##


# values for enumeration '_AudioBeamMode'
AudioBeamMode_Automatic = 0
AudioBeamMode_Manual = 1
_AudioBeamMode = c_int # enum
class ISequentialStream(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
IAudioBeam._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'AudioSource',
              ( ['retval', 'out'], POINTER(POINTER(IAudioSource)), 'AudioSource' )),
    COMMETHOD(['propget'], HRESULT, 'AudioBeamMode',
              ( ['retval', 'out'], POINTER(_AudioBeamMode), 'AudioBeamMode' )),
    COMMETHOD(['propput'], HRESULT, 'AudioBeamMode',
              ( [], _AudioBeamMode, 'AudioBeamMode' )),
    COMMETHOD(['propget'], HRESULT, 'BeamAngle',
              ( ['retval', 'out'], POINTER(c_float), 'BeamAngle' )),
    COMMETHOD(['propput'], HRESULT, 'BeamAngle',
              ( [], c_float, 'BeamAngle' )),
    COMMETHOD(['propget'], HRESULT, 'BeamAngleConfidence',
              ( ['retval', 'out'], POINTER(c_float), 'BeamAngleConfidence' )),
    COMMETHOD([], HRESULT, 'OpenInputStream',
              ( ['retval', 'out'], POINTER(POINTER(IStream)), 'stream' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IAudioBeam implementation
##class IAudioBeam_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return AudioBeamMode
##    def _set(self, AudioBeamMode):
##        '-no docstring-'
##    AudioBeamMode = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def AudioSource(self):
##        '-no docstring-'
##        #return AudioSource
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def BeamAngleConfidence(self):
##        '-no docstring-'
##        #return BeamAngleConfidence
##
##    def OpenInputStream(self):
##        '-no docstring-'
##        #return stream
##
##    def _get(self):
##        '-no docstring-'
##        #return BeamAngle
##    def _set(self, BeamAngle):
##        '-no docstring-'
##    BeamAngle = property(_get, _set, doc = _set.__doc__)
##

class IBodyFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C3A1733C-5F84-443B-9659-2F2BE250C97D}')
    _idlflags_ = []
IBodyFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameReference)), 'bodyFrameReference' )),
]
################################################################
## code template for IBodyFrameArrivedEventArgs implementation
##class IBodyFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return bodyFrameReference
##

IColorFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrame)), 'colorFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IColorFrameReference implementation
##class IColorFrameReference_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return colorFrame
##

IDepthFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrame)), 'depthFrame' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'DepthFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameSource)), 'DepthFrameSource' )),
]
################################################################
## code template for IDepthFrameReader implementation
##class IDepthFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DepthFrameSource(self):
##        '-no docstring-'
##        #return DepthFrameSource
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return depthFrame
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##

IBodyIndexFrameSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameReader)), 'reader' )),
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
]
################################################################
## code template for IBodyIndexFrameSource implementation
##class IBodyIndexFrameSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

IBodyFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrame)), 'bodyFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IBodyFrameReference implementation
##class IBodyFrameReference_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return bodyFrame
##

class IBodyIndexFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D0EA0519-F7E7-4B1E-B3D8-03B3C002795F}')
    _idlflags_ = []
IBodyIndexFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameReference)), 'bodyIndexFrameReference' )),
]
################################################################
## code template for IBodyIndexFrameArrivedEventArgs implementation
##class IBodyIndexFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return bodyIndexFrameReference
##


# values for enumeration '_Expression'
Expression_Neutral = 0
Expression_Happy = 1
Expression_Count = 2
_Expression = c_int # enum
IColorFrame._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'RawColorImageFormat',
              ( ['retval', 'out'], POINTER(_ColorImageFormat), 'RawColorImageFormat' )),
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'rawFrameDescription' )),
    COMMETHOD([], HRESULT, 'CopyRawFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ubyte), 'frameData' )),
    COMMETHOD([], HRESULT, 'AccessRawUnderlyingBuffer',
              ( [], POINTER(c_uint), 'capacity' ),
              ( [], POINTER(POINTER(c_ubyte)), 'buffer' )), #'out'
    COMMETHOD([], HRESULT, 'CopyConvertedFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ubyte), 'frameData' ), #( [], POINTER(c_ubyte), 'frameData' )
              ( [], _ColorImageFormat, 'colorFormat' )),
    COMMETHOD([], HRESULT, 'CreateFrameDescription',
              ( [], _ColorImageFormat, 'format' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'ColorCameraSettings',
              ( ['retval', 'out'], POINTER(POINTER(IColorCameraSettings)), 'ColorCameraSettings' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
    COMMETHOD(['propget'], HRESULT, 'ColorFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameSource)), 'ColorFrameSource' )),
]
################################################################
## code template for IColorFrame implementation
##class IColorFrame_Impl(object):
##    def CopyConvertedFrameDataToArray(self, capacity, colorFormat):
##        '-no docstring-'
##        #return frameData
##
##    @property
##    def ColorCameraSettings(self):
##        '-no docstring-'
##        #return ColorCameraSettings
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return rawFrameDescription
##
##    @property
##    def RawColorImageFormat(self):
##        '-no docstring-'
##        #return RawColorImageFormat
##
##    def AccessRawUnderlyingBuffer(self):
##        '-no docstring-'
##        #return capacity, buffer
##
##    def CreateFrameDescription(self, format):
##        '-no docstring-'
##        #return FrameDescription
##
##    def CopyRawFrameDataToArray(self, capacity):
##        '-no docstring-'
##        #return frameData
##
##    @property
##    def ColorFrameSource(self):
##        '-no docstring-'
##        #return ColorFrameSource
##

ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( [], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( [], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( [], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

IFrameDescription._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'Width' )),
    COMMETHOD(['propget'], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'Height' )),
    COMMETHOD(['propget'], HRESULT, 'HorizontalFieldOfView',
              ( ['retval', 'out'], POINTER(c_float), 'HorizontalFieldOfView' )),
    COMMETHOD(['propget'], HRESULT, 'VerticalFieldOfView',
              ( ['retval', 'out'], POINTER(c_float), 'VerticalFieldOfView' )),
    COMMETHOD(['propget'], HRESULT, 'DiagonalFieldOfView',
              ( ['retval', 'out'], POINTER(c_float), 'DiagonalFieldOfView' )),
    COMMETHOD(['propget'], HRESULT, 'LengthInPixels',
              ( ['retval', 'out'], POINTER(c_uint), 'LengthInPixels' )),
    COMMETHOD(['propget'], HRESULT, 'BytesPerPixel',
              ( ['retval', 'out'], POINTER(c_uint), 'BytesPerPixel' )),
]
################################################################
## code template for IFrameDescription implementation
##class IFrameDescription_Impl(object):
##    @property
##    def HorizontalFieldOfView(self):
##        '-no docstring-'
##        #return HorizontalFieldOfView
##
##    @property
##    def DiagonalFieldOfView(self):
##        '-no docstring-'
##        #return DiagonalFieldOfView
##
##    @property
##    def VerticalFieldOfView(self):
##        '-no docstring-'
##        #return VerticalFieldOfView
##
##    @property
##    def Height(self):
##        '-no docstring-'
##        #return Height
##
##    @property
##    def Width(self):
##        '-no docstring-'
##        #return Width
##
##    @property
##    def BytesPerPixel(self):
##        '-no docstring-'
##        #return BytesPerPixel
##
##    @property
##    def LengthInPixels(self):
##        '-no docstring-'
##        #return LengthInPixels
##

IBodyIndexFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrame)), 'bodyIndexFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IBodyIndexFrameReference implementation
##class IBodyIndexFrameReference_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return bodyIndexFrame
##

class tagSTATSTG(Structure):
    pass
IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( [], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( [], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( [], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( [], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##
##    def Revert(self):
##        '-no docstring-'
##        #return 
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return 
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return 
##

IDepthFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrame)), 'depthFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IDepthFrameReference implementation
##class IDepthFrameReference_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return depthFrame
##

class _CameraSpacePoint(Structure):
    pass
_CameraSpacePoint._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
]
assert sizeof(_CameraSpacePoint) == 12, sizeof(_CameraSpacePoint)
assert alignment(_CameraSpacePoint) == 4, alignment(_CameraSpacePoint)
_Joint._fields_ = [
    ('JointType', _JointType),
    ('Position', _CameraSpacePoint),
    ('TrackingState', _TrackingState),
]
assert sizeof(_Joint) == 20, sizeof(_Joint)
assert alignment(_Joint) == 4, alignment(_Joint)
IBodyIndexFrame._methods_ = [
    COMMETHOD([], HRESULT, 'CopyFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ubyte), 'frameData' )),
    COMMETHOD([], HRESULT, 'AccessUnderlyingBuffer',
              ( [], POINTER(c_uint), 'capacity' ),
              ( [], POINTER(POINTER(c_ubyte)), 'buffer' )), #'out'
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
    COMMETHOD(['propget'], HRESULT, 'BodyIndexFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameSource)), 'BodyIndexFrameSource' )),
]
################################################################
## code template for IBodyIndexFrame implementation
##class IBodyIndexFrame_Impl(object):
##    @property
##    def BodyIndexFrameSource(self):
##        '-no docstring-'
##        #return BodyIndexFrameSource
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def CopyFrameDataToArray(self, capacity):
##        '-no docstring-'
##        #return frameData
##
##    def AccessUnderlyingBuffer(self):
##        '-no docstring-'
##        #return capacity, buffer
##

_PointF._fields_ = [
    ('x', c_float),
    ('y', c_float),
]
assert sizeof(_PointF) == 8, sizeof(_PointF)
assert alignment(_PointF) == 4, alignment(_PointF)
class _ColorSpacePoint(Structure):
    pass
_ColorSpacePoint._fields_ = [
    ('x', c_float),
    ('y', c_float),
]
assert sizeof(_ColorSpacePoint) == 8, sizeof(_ColorSpacePoint)
assert alignment(_ColorSpacePoint) == 4, alignment(_ColorSpacePoint)
class _RectF(Structure):
    pass
_RectF._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('Width', c_float),
    ('Height', c_float),
]
assert sizeof(_RectF) == 16, sizeof(_RectF)
assert alignment(_RectF) == 4, alignment(_RectF)
class IMultiSourceFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3532F40B-D908-451D-BBF4-6CA73B782558}')
    _idlflags_ = []
class IMultiSourceFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DD70E845-E283-4DD1-8DAF-FC259AC5F9E3}')
    _idlflags_ = []
IMultiSourceFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IMultiSourceFrameReference)), 'frames' )),
]
################################################################
## code template for IMultiSourceFrameArrivedEventArgs implementation
##class IMultiSourceFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return frames
##

class _DepthSpacePoint(Structure):
    pass
_DepthSpacePoint._fields_ = [
    ('x', c_float),
    ('y', c_float),
]
assert sizeof(_DepthSpacePoint) == 8, sizeof(_DepthSpacePoint)
assert alignment(_DepthSpacePoint) == 4, alignment(_DepthSpacePoint)
_JointOrientation._fields_ = [
    ('JointType', _JointType),
    ('Orientation', _Vector4),
]
assert sizeof(_JointOrientation) == 20, sizeof(_JointOrientation)
assert alignment(_JointOrientation) == 4, alignment(_JointOrientation)
class IMultiSourceFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{29A63AFB-76CE-4359-895A-997F1E094D1C}')
    _idlflags_ = []
IMultiSourceFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(IMultiSourceFrame)), 'frame' )),
]
################################################################
## code template for IMultiSourceFrameReference implementation
##class IMultiSourceFrameReference_Impl(object):
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return frame
##

ILongExposureInfraredFrameSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameReader)), 'reader' )),
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
]
################################################################
## code template for ILongExposureInfraredFrameSource implementation
##class ILongExposureInfraredFrameSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

class IInfraredFrameReference(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{60183D5B-DED5-4D5C-AE59-64C7724FE5FE}')
    _idlflags_ = []
IMultiSourceFrame._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'colorFrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameReference)), 'colorFrameReference' )),
    COMMETHOD(['propget'], HRESULT, 'depthFrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameReference)), 'depthFrameReference' )),
    COMMETHOD(['propget'], HRESULT, 'bodyFrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameReference)), 'bodyFrameReference' )),
    COMMETHOD(['propget'], HRESULT, 'bodyIndexFrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameReference)), 'bodyIndexFrameReference' )),
    COMMETHOD(['propget'], HRESULT, 'infraredFrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameReference)), 'infraredFrameReference' )),
    COMMETHOD(['propget'], HRESULT, 'longExposureInfraredFrameReference',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameReference)), 'longExposureInfraredFrameReference' )),
]
################################################################
## code template for IMultiSourceFrame implementation
##class IMultiSourceFrame_Impl(object):
##    @property
##    def depthFrameReference(self):
##        '-no docstring-'
##        #return depthFrameReference
##
##    @property
##    def bodyIndexFrameReference(self):
##        '-no docstring-'
##        #return bodyIndexFrameReference
##
##    @property
##    def longExposureInfraredFrameReference(self):
##        '-no docstring-'
##        #return longExposureInfraredFrameReference
##
##    @property
##    def bodyFrameReference(self):
##        '-no docstring-'
##        #return bodyFrameReference
##
##    @property
##    def infraredFrameReference(self):
##        '-no docstring-'
##        #return infraredFrameReference
##
##    @property
##    def colorFrameReference(self):
##        '-no docstring-'
##        #return colorFrameReference
##

class _CameraIntrinsics(Structure):
    pass
_CameraIntrinsics._fields_ = [
    ('FocalLengthX', c_float),
    ('FocalLengthY', c_float),
    ('PrincipalPointX', c_float),
    ('PrincipalPointY', c_float),
    ('RadialDistortionSecondOrder', c_float),
    ('RadialDistortionFourthOrder', c_float),
    ('RadialDistortionSixthOrder', c_float),
]
assert sizeof(_CameraIntrinsics) == 28, sizeof(_CameraIntrinsics)
assert alignment(_CameraIntrinsics) == 4, alignment(_CameraIntrinsics)
class ICoordinateMapper(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8784DF2D-16B0-481C-A11E-55E70BF25018}')
    _idlflags_ = []
class ICoordinateMappingChangedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E9A2A0BF-13BD-4A53-A157-91FC8BB41F85}')
    _idlflags_ = []
ICoordinateMapper._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeCoordinateMappingChanged',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeCoordinateMappingChanged',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetCoordinateMappingChangedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(ICoordinateMappingChangedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'MapCameraPointToDepthSpace',
              ( [], _CameraSpacePoint, 'cameraPoint' ),
              ( ['retval', 'out'], POINTER(_DepthSpacePoint), 'depthPoint' )),
    COMMETHOD([], HRESULT, 'MapCameraPointToColorSpace',
              ( [], _CameraSpacePoint, 'cameraPoint' ),
              ( ['retval', 'out'], POINTER(_ColorSpacePoint), 'colorPoint' )),
    COMMETHOD([], HRESULT, 'MapDepthPointToCameraSpace',
              ( [], _DepthSpacePoint, 'depthPoint' ),
              ( [], c_ushort, 'depth' ),
              ( ['retval', 'out'], POINTER(_CameraSpacePoint), 'cameraPoint' )),
    COMMETHOD([], HRESULT, 'MapDepthPointToColorSpace',
              ( [], _DepthSpacePoint, 'depthPoint' ),
              ( [], c_ushort, 'depth' ),
              ( ['retval', 'out'], POINTER(_ColorSpacePoint), 'colorPoint' )),
    COMMETHOD([], HRESULT, 'MapCameraPointsToDepthSpace',
              ( [], c_uint, 'cameraPointCount' ),
              ( ['in'], POINTER(_CameraSpacePoint), 'cameraPoints' ),
              ( [], c_uint, 'depthPointCount' ),
              ( [], POINTER(_DepthSpacePoint), 'depthPoints' )),
    COMMETHOD([], HRESULT, 'MapCameraPointsToColorSpace',
              ( [], c_uint, 'cameraPointCount' ),
              ( ['in'], POINTER(_CameraSpacePoint), 'cameraPoints' ),
              ( [], c_uint, 'colorPointCount' ),
              ( [], POINTER(_ColorSpacePoint), 'colorPoints' )),
    COMMETHOD([], HRESULT, 'MapDepthPointsToCameraSpace',
              ( [], c_uint, 'depthPointCount' ),
              ( ['in'], POINTER(_DepthSpacePoint), 'depthPoints' ),
              ( [], c_uint, 'depthCount' ),
              ( ['in'], POINTER(c_ushort), 'depths' ),
              ( [], c_uint, 'cameraPointCount' ),
              ( [], POINTER(_CameraSpacePoint), 'cameraPoints' )),
    COMMETHOD([], HRESULT, 'MapDepthPointsToColorSpace',
              ( [], c_uint, 'depthPointCount' ),
              ( ['in'], POINTER(_DepthSpacePoint), 'depthPoints' ),
              ( [], c_uint, 'depthCount' ),
              ( ['in'], POINTER(c_ushort), 'depths' ),
              ( [], c_uint, 'colorPointCount' ),
              ( [], POINTER(_ColorSpacePoint), 'colorPoints' )),
    COMMETHOD([], HRESULT, 'MapDepthFrameToCameraSpace',
              ( [], c_uint, 'depthPointCount' ),
              ( ['in'], POINTER(c_ushort), 'depthFrameData' ),
              ( [], c_uint, 'cameraPointCount' ),
              ( [], POINTER(_CameraSpacePoint), 'cameraSpacePoints' )),
    COMMETHOD([], HRESULT, 'MapDepthFrameToColorSpace',
              ( [], c_uint, 'depthPointCount' ),
              ( ['in'], POINTER(c_ushort), 'depthFrameData' ),
              ( [], c_uint, 'colorPointCount' ),
              ( [], POINTER(_ColorSpacePoint), 'colorSpacePoints' )),
    COMMETHOD([], HRESULT, 'MapColorFrameToDepthSpace',
              ( [], c_uint, 'depthDataPointCount' ),
              ( ['in'], POINTER(c_ushort), 'depthFrameData' ),
              ( [], c_uint, 'depthPointCount' ),
              ( [], POINTER(_DepthSpacePoint), 'depthSpacePoints' )),
    COMMETHOD([], HRESULT, 'MapColorFrameToCameraSpace',
              ( [], c_uint, 'depthDataPointCount' ),
              ( ['in'], POINTER(c_ushort), 'depthFrameData' ),
              ( [], c_uint, 'cameraPointCount' ),
              ( [], POINTER(_CameraSpacePoint), 'cameraSpacePoints' )),
    COMMETHOD([], HRESULT, 'GetDepthFrameToCameraSpaceTable',
              ( [], POINTER(c_uint), 'tableEntryCount' ),
              ( ['retval', 'out'], POINTER(POINTER(_PointF)), 'tableEntries' )),
    COMMETHOD([], HRESULT, 'GetDepthCameraIntrinsics',
              ( ['retval', 'out'], POINTER(_CameraIntrinsics), 'cameraIntrinsics' )),
]
################################################################
## code template for ICoordinateMapper implementation
##class ICoordinateMapper_Impl(object):
##    def GetDepthCameraIntrinsics(self):
##        '-no docstring-'
##        #return cameraIntrinsics
##
##    def MapDepthPointsToCameraSpace(self, depthPointCount, depthPoints, depthCount, depths, cameraPointCount):
##        '-no docstring-'
##        #return cameraPoints
##
##    def GetCoordinateMappingChangedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def MapCameraPointsToDepthSpace(self, cameraPointCount, cameraPoints, depthPointCount):
##        '-no docstring-'
##        #return depthPoints
##
##    def MapColorFrameToCameraSpace(self, depthDataPointCount, depthFrameData, cameraPointCount):
##        '-no docstring-'
##        #return cameraSpacePoints
##
##    def MapCameraPointToColorSpace(self, cameraPoint):
##        '-no docstring-'
##        #return colorPoint
##
##    def SubscribeCoordinateMappingChanged(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    def MapDepthPointsToColorSpace(self, depthPointCount, depthPoints, depthCount, depths, colorPointCount):
##        '-no docstring-'
##        #return colorPoints
##
##    def MapDepthPointToCameraSpace(self, depthPoint, depth):
##        '-no docstring-'
##        #return cameraPoint
##
##    def MapColorFrameToDepthSpace(self, depthDataPointCount, depthFrameData, depthPointCount):
##        '-no docstring-'
##        #return depthSpacePoints
##
##    def UnsubscribeCoordinateMappingChanged(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def MapCameraPointsToColorSpace(self, cameraPointCount, cameraPoints, colorPointCount):
##        '-no docstring-'
##        #return colorPoints
##
##    def GetDepthFrameToCameraSpaceTable(self):
##        '-no docstring-'
##        #return tableEntryCount, tableEntries
##
##    def MapDepthFrameToCameraSpace(self, depthPointCount, depthFrameData, cameraPointCount):
##        '-no docstring-'
##        #return cameraSpacePoints
##
##    def MapDepthFrameToColorSpace(self, depthPointCount, depthFrameData, colorPointCount):
##        '-no docstring-'
##        #return colorSpacePoints
##
##    def MapCameraPointToDepthSpace(self, cameraPoint):
##        '-no docstring-'
##        #return depthPoint
##
##    def MapDepthPointToColorSpace(self, depthPoint, depth):
##        '-no docstring-'
##        #return colorPoint
##

tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
required_size = 64 + sysinfo.platform_bits / 4

assert sizeof(tagSTATSTG) == required_size, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
IAudioBeamList._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'BeamCount',
              ( ['retval', 'out'], POINTER(c_uint), 'count' )),
    COMMETHOD([], HRESULT, 'OpenAudioBeam',
              ( [], c_uint, 'index' ),
              ( ['out'], POINTER(POINTER(IAudioBeam)), 'AudioBeam' )),
]
################################################################
## code template for IAudioBeamList implementation
##class IAudioBeamList_Impl(object):
##    def OpenAudioBeam(self, index):
##        '-no docstring-'
##        #return AudioBeam
##
##    @property
##    def BeamCount(self):
##        '-no docstring-'
##        #return count
##

class IInfraredFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{059A049D-A0AC-481E-B342-483EE94A028B}')
    _idlflags_ = []
class IInfraredFrameArrivedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7E17F78E-D9D1-4448-90C2-4E50EC4ECEE9}')
    _idlflags_ = []
class IInfraredFrame(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{EA83823C-7613-4F29-BD51-4A9678A52C7E}')
    _idlflags_ = []
class IInfraredFrameSource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4C299EC6-CA45-4AFF-87AD-DF5762C49BE7}')
    _idlflags_ = []
IInfraredFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrame)), 'infraredFrame' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'InfraredFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameSource)), 'InfraredFrameSource' )),
]
################################################################
## code template for IInfraredFrameReader implementation
##class IInfraredFrameReader_Impl(object):
##    def GetFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    @property
##    def InfraredFrameSource(self):
##        '-no docstring-'
##        #return InfraredFrameSource
##
##    def UnsubscribeFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return infraredFrame
##
##    def SubscribeFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##

IInfraredFrameSource._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeFrameCaptured',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeFrameCaptured',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetFrameCapturedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IFrameCapturedEventArgs)), 'eventData' )),
    COMMETHOD(['propget'], HRESULT, 'IsActive',
              ( ['retval', 'out'], POINTER(c_bool), 'IsActive' )),
    COMMETHOD([], HRESULT, 'OpenReader',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameReader)), 'reader' )),
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
]
################################################################
## code template for IInfraredFrameSource implementation
##class IInfraredFrameSource_Impl(object):
##    def UnsubscribeFrameCaptured(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def OpenReader(self):
##        '-no docstring-'
##        #return reader
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def GetFrameCapturedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def SubscribeFrameCaptured(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    @property
##    def IsActive(self):
##        '-no docstring-'
##        #return IsActive
##

IInfraredFrameArrivedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameReference',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameReference)), 'infraredFrameReference' )),
]
################################################################
## code template for IInfraredFrameArrivedEventArgs implementation
##class IInfraredFrameArrivedEventArgs_Impl(object):
##    @property
##    def FrameReference(self):
##        '-no docstring-'
##        #return infraredFrameReference
##

class IAudioBodyCorrelation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C5BA2355-07DB-47C3-ABC4-68D24B91DE61}')
    _idlflags_ = []
IAudioBeamSubFrame._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'FrameLengthInBytes',
              ( ['retval', 'out'], POINTER(c_uint), 'length' )),
    COMMETHOD(['propget'], HRESULT, 'duration',
              ( ['retval', 'out'], POINTER(c_longlong), 'duration' )),
    COMMETHOD(['propget'], HRESULT, 'BeamAngle',
              ( ['retval', 'out'], POINTER(c_float), 'BeamAngle' )),
    COMMETHOD(['propget'], HRESULT, 'BeamAngleConfidence',
              ( ['retval', 'out'], POINTER(c_float), 'BeamAngleConfidence' )),
    COMMETHOD(['propget'], HRESULT, 'AudioBeamMode',
              ( ['retval', 'out'], POINTER(_AudioBeamMode), 'AudioBeamMode' )),
    COMMETHOD(['propget'], HRESULT, 'AudioBodyCorrelationCount',
              ( ['retval', 'out'], POINTER(c_uint), 'pCount' )),
    COMMETHOD([], HRESULT, 'GetAudioBodyCorrelation',
              ( ['in'], c_uint, 'index' ),
              ( ['out'], POINTER(POINTER(IAudioBodyCorrelation)), 'ppAudioBodyCorrelation' )),
    COMMETHOD([], HRESULT, 'CopyFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ubyte), 'frameData' )),
    COMMETHOD([], HRESULT, 'AccessUnderlyingBuffer',
              ( [], POINTER(c_uint), 'capacity' ),
              ( [], POINTER(POINTER(c_ubyte)), 'buffer' )), #'out'
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IAudioBeamSubFrame implementation
##class IAudioBeamSubFrame_Impl(object):
##    @property
##    def AudioBeamMode(self):
##        '-no docstring-'
##        #return AudioBeamMode
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def GetAudioBodyCorrelation(self, index):
##        '-no docstring-'
##        #return ppAudioBodyCorrelation
##
##    def CopyFrameDataToArray(self, capacity):
##        '-no docstring-'
##        #return frameData
##
##    @property
##    def FrameLengthInBytes(self):
##        '-no docstring-'
##        #return length
##
##    @property
##    def AudioBodyCorrelationCount(self):
##        '-no docstring-'
##        #return pCount
##
##    def AccessUnderlyingBuffer(self):
##        '-no docstring-'
##        #return capacity, buffer
##
##    @property
##    def BeamAngleConfidence(self):
##        '-no docstring-'
##        #return BeamAngleConfidence
##
##    @property
##    def duration(self):
##        '-no docstring-'
##        #return duration
##
##    @property
##    def BeamAngle(self):
##        '-no docstring-'
##        #return BeamAngle
##

IEnumKinectSensor._methods_ = [
    COMMETHOD([], HRESULT, 'GetNext',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
    COMMETHOD([], HRESULT, 'Reset'),
]
################################################################
## code template for IEnumKinectSensor implementation
##class IEnumKinectSensor_Impl(object):
##    def GetNext(self):
##        '-no docstring-'
##        #return sensor
##
##    def Reset(self):
##        '-no docstring-'
##        #return 
##

IBodyFrame._methods_ = [
    COMMETHOD([], HRESULT, 'GetAndRefreshBodyData',
              ( [], c_uint, 'capacity' ),
              ( ['in'], POINTER(POINTER(IBody)), 'bodies' )),
    COMMETHOD(['propget'], HRESULT, 'FloorClipPlane',
              ( ['retval', 'out'], POINTER(_Vector4), 'FloorClipPlane' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
    COMMETHOD(['propget'], HRESULT, 'BodyFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameSource)), 'BodyFrameSource' )),
]
################################################################
## code template for IBodyFrame implementation
##class IBodyFrame_Impl(object):
##    @property
##    def FloorClipPlane(self):
##        '-no docstring-'
##        #return FloorClipPlane
##
##    @property
##    def BodyFrameSource(self):
##        '-no docstring-'
##        #return BodyFrameSource
##
##    def GetAndRefreshBodyData(self, capacity):
##        '-no docstring-'
##        #return bodies
##
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##

ICoordinateMappingChangedEventArgs._methods_ = [
]
################################################################
## code template for ICoordinateMappingChangedEventArgs implementation
##class ICoordinateMappingChangedEventArgs_Impl(object):

IInfraredFrameReference._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireFrame',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrame)), 'infraredFrame' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
]
################################################################
## code template for IInfraredFrameReference implementation
##class IInfraredFrameReference_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    def AcquireFrame(self):
##        '-no docstring-'
##        #return infraredFrame
##

class IIsAvailableChangedEventArgs(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3A6DD52E-967F-4982-B3D9-74B9E1A044C9}')
    _idlflags_ = []
class IMultiSourceFrameReader(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C0F6432B-9FFE-4AB3-A683-F37C72BBB158}')
    _idlflags_ = []
IKinectSensor._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeIsAvailableChanged',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeIsAvailableChanged',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetIsAvailableChangedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IIsAvailableChangedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'Open'),
    COMMETHOD([], HRESULT, 'Close'),
    COMMETHOD(['propget'], HRESULT, 'IsOpen',
              ( ['retval', 'out'], POINTER(c_bool), 'IsOpen' )),
    COMMETHOD(['propget'], HRESULT, 'IsAvailable',
              ( ['retval', 'out'], POINTER(c_bool), 'IsAvailable' )),
    COMMETHOD(['propget'], HRESULT, 'ColorFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IColorFrameSource)), 'ColorFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'DepthFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IDepthFrameSource)), 'DepthFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'BodyFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IBodyFrameSource)), 'BodyFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'BodyIndexFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IBodyIndexFrameSource)), 'BodyIndexFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'InfraredFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameSource)), 'InfraredFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'LongExposureInfraredFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(ILongExposureInfraredFrameSource)), 'LongExposureInfraredFrameSource' )),
    COMMETHOD(['propget'], HRESULT, 'AudioSource',
              ( ['retval', 'out'], POINTER(POINTER(IAudioSource)), 'AudioSource' )),
    COMMETHOD([], HRESULT, 'OpenMultiSourceFrameReader',
              ( [], c_ulong, 'enabledFrameSourceTypes' ),
              ( ['retval', 'out'], POINTER(POINTER(IMultiSourceFrameReader)), 'multiSourceFrameReader' )),
    COMMETHOD(['propget'], HRESULT, 'CoordinateMapper',
              ( ['retval', 'out'], POINTER(POINTER(ICoordinateMapper)), 'CoordinateMapper' )),
    COMMETHOD(['propget'], HRESULT, 'UniqueKinectId',
              ( [], c_uint, 'bufferSize' ),
              ( ['retval', 'out'], POINTER(c_ushort), 'UniqueKinectId' )),
    COMMETHOD(['propget'], HRESULT, 'KinectCapabilities',
              ( ['retval', 'out'], POINTER(c_ulong), 'capabilities' )),
]
################################################################
## code template for IKinectSensor implementation
##class IKinectSensor_Impl(object):
##    def SubscribeIsAvailableChanged(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    def OpenMultiSourceFrameReader(self, enabledFrameSourceTypes):
##        '-no docstring-'
##        #return multiSourceFrameReader
##
##    def GetIsAvailableChangedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    @property
##    def AudioSource(self):
##        '-no docstring-'
##        #return AudioSource
##
##    @property
##    def IsOpen(self):
##        '-no docstring-'
##        #return IsOpen
##
##    @property
##    def BodyIndexFrameSource(self):
##        '-no docstring-'
##        #return BodyIndexFrameSource
##
##    @property
##    def InfraredFrameSource(self):
##        '-no docstring-'
##        #return InfraredFrameSource
##
##    @property
##    def BodyFrameSource(self):
##        '-no docstring-'
##        #return BodyFrameSource
##
##    @property
##    def UniqueKinectId(self, bufferSize):
##        '-no docstring-'
##        #return UniqueKinectId
##
##    def UnsubscribeIsAvailableChanged(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    @property
##    def ColorFrameSource(self):
##        '-no docstring-'
##        #return ColorFrameSource
##
##    @property
##    def LongExposureInfraredFrameSource(self):
##        '-no docstring-'
##        #return LongExposureInfraredFrameSource
##
##    @property
##    def KinectCapabilities(self):
##        '-no docstring-'
##        #return capabilities
##
##    @property
##    def DepthFrameSource(self):
##        '-no docstring-'
##        #return DepthFrameSource
##
##    def Close(self):
##        '-no docstring-'
##        #return 
##
##    @property
##    def IsAvailable(self):
##        '-no docstring-'
##        #return IsAvailable
##
##    def Open(self):
##        '-no docstring-'
##        #return 
##
##    @property
##    def CoordinateMapper(self):
##        '-no docstring-'
##        #return CoordinateMapper
##

IAudioBodyCorrelation._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'BodyTrackingId',
              ( ['retval', 'out'], POINTER(c_ulonglong), 'TrackingId' )),
]
################################################################
## code template for IAudioBodyCorrelation implementation
##class IAudioBodyCorrelation_Impl(object):
##    @property
##    def BodyTrackingId(self):
##        '-no docstring-'
##        #return TrackingId
##

IInfraredFrame._methods_ = [
    COMMETHOD([], HRESULT, 'CopyFrameDataToArray',
              ( [], c_uint, 'capacity' ),
              ( [], POINTER(c_ushort), 'frameData' )),
    COMMETHOD([], HRESULT, 'AccessUnderlyingBuffer',
              ( [], POINTER(c_uint), 'capacity' ),
              ( [], POINTER(POINTER(c_ushort)), 'buffer' )), #'out'
    COMMETHOD(['propget'], HRESULT, 'FrameDescription',
              ( ['retval', 'out'], POINTER(POINTER(IFrameDescription)), 'FrameDescription' )),
    COMMETHOD(['propget'], HRESULT, 'RelativeTime',
              ( ['retval', 'out'], POINTER(c_longlong), 'RelativeTime' )),
    COMMETHOD(['propget'], HRESULT, 'InfraredFrameSource',
              ( ['retval', 'out'], POINTER(POINTER(IInfraredFrameSource)), 'InfraredFrameSource' )),
]
################################################################
## code template for IInfraredFrame implementation
##class IInfraredFrame_Impl(object):
##    @property
##    def RelativeTime(self):
##        '-no docstring-'
##        #return RelativeTime
##
##    @property
##    def FrameDescription(self):
##        '-no docstring-'
##        #return FrameDescription
##
##    def CopyFrameDataToArray(self, capacity):
##        '-no docstring-'
##        #return frameData
##
##    @property
##    def InfraredFrameSource(self):
##        '-no docstring-'
##        #return InfraredFrameSource
##
##    def AccessUnderlyingBuffer(self):
##        '-no docstring-'
##        #return capacity, buffer
##

IMultiSourceFrameReader._methods_ = [
    COMMETHOD([], HRESULT, 'SubscribeMultiSourceFrameArrived',
              ( ['retval', 'out'], POINTER(INT_PTR), 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'UnsubscribeMultiSourceFrameArrived',
              ( ['in'], INT_PTR, 'waitableHandle' )),
    COMMETHOD([], HRESULT, 'GetMultiSourceFrameArrivedEventData',
              ( ['in'], INT_PTR, 'waitableHandle' ),
              ( ['retval', 'out'], POINTER(POINTER(IMultiSourceFrameArrivedEventArgs)), 'eventData' )),
    COMMETHOD([], HRESULT, 'AcquireLatestFrame',
              ( ['retval', 'out'], POINTER(POINTER(IMultiSourceFrame)), 'multiSourceFrame' )),
    COMMETHOD(['propget'], HRESULT, 'FrameSourceTypes',
              ( ['retval', 'out'], POINTER(c_ulong), 'enabledFrameSourceTypes' )),
    COMMETHOD(['propget'], HRESULT, 'IsPaused',
              ( ['retval', 'out'], POINTER(c_bool), 'IsPaused' )),
    COMMETHOD(['propput'], HRESULT, 'IsPaused',
              ( [], c_bool, 'IsPaused' )),
    COMMETHOD(['propget'], HRESULT, 'KinectSensor',
              ( ['retval', 'out'], POINTER(POINTER(IKinectSensor)), 'sensor' )),
]
################################################################
## code template for IMultiSourceFrameReader implementation
##class IMultiSourceFrameReader_Impl(object):
##    @property
##    def KinectSensor(self):
##        '-no docstring-'
##        #return sensor
##
##    def GetMultiSourceFrameArrivedEventData(self, waitableHandle):
##        '-no docstring-'
##        #return eventData
##
##    def UnsubscribeMultiSourceFrameArrived(self, waitableHandle):
##        '-no docstring-'
##        #return 
##
##    def SubscribeMultiSourceFrameArrived(self):
##        '-no docstring-'
##        #return waitableHandle
##
##    def _get(self):
##        '-no docstring-'
##        #return IsPaused
##    def _set(self, IsPaused):
##        '-no docstring-'
##    IsPaused = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FrameSourceTypes(self):
##        '-no docstring-'
##        #return enabledFrameSourceTypes
##
##    def AcquireLatestFrame(self):
##        '-no docstring-'
##        #return multiSourceFrame
##

IIsAvailableChangedEventArgs._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'IsAvailable',
              ( ['retval', 'out'], POINTER(c_bool), 'IsAvailable' )),
]
################################################################
## code template for IIsAvailableChangedEventArgs implementation
##class IIsAvailableChangedEventArgs_Impl(object):
##    @property
##    def IsAvailable(self):
##        '-no docstring-'
##        #return IsAvailable
##

__all__ = [ 'IKinectSensor', 'IAudioBeamSubFrame',
           'JointType_WristLeft', 'Activity_MouthOpen',
           'FrameSourceTypes_Color', 'FrameSourceTypes_Audio',
           'JointType_ThumbRight', '_FrameEdges',
           'IAudioBeamFrameList', 'IBodyIndexFrame',
           'FrameCapturedStatus_Dropped', 'tagSTATSTG',
           'IBodyFrameReference', 'IFrameDescription',
           'FrameEdge_Right', 'HandState_Lasso',
           'JointType_ShoulderRight', '_AudioBeamMode',
           'IBodyFrameReader', 'FrameCapturedStatus_Unknown',
           '_KinectCapabilities', '_DepthSpacePoint',
           'HandState_Closed', '_FrameSourceTypes', '_TrackingState',
           'HandState_NotTracked', 'IAudioBeamFrameReader',
           'JointType_ShoulderLeft',
           'ILongExposureInfraredFrameArrivedEventArgs',
           'JointType_SpineMid', 'ILongExposureInfraredFrameSource',
           'IKinectSensorCollection', 'TrackingState_Inferred',
           'Activity_MouthMoved', 'TrackingState_NotTracked',
           'IMultiSourceFrameArrivedEventArgs',
           'AudioBeamMode_Manual', '_JointOrientation',
           'Activity_EyeRightClosed', 'IBodyIndexFrameReference',
           'IStream', 'KinectCapabilities_Face', 'Expression_Count',
           'JointType_HandLeft', 'IMultiSourceFrameReader',
           'FrameEdge_Bottom', 'JointType_SpineShoulder',
           'IFrameCapturedEventArgs', 'JointType_KneeLeft',
           'KinectCapabilities_Vision', 'IDepthFrame', 'IColorFrame',
           '_HandState', 'IBodyIndexFrameReader', '_CameraIntrinsics',
           '_KinectAudioCalibrationState', 'IAudioBodyCorrelation',
           'IColorFrameSource', 'DetectionResult_Yes',
           'IDepthFrameReader', 'Appearance_WearingGlasses',
           'KinectCapabilities_Gamechat', 'AudioBeamMode_Automatic',
           'JointType_HandTipLeft', 'JointType_AnkleLeft', '_Joint',
           'INT_PTR', 'Activity_LookingAway', 'IInfraredFrameSource',
           '_RectF', 'JointType_HipRight', 'DetectionResult_No',
           'IColorFrameArrivedEventArgs', 'ISequentialStream',
           'IAudioBeamFrameArrivedEventArgs', 'IBody',
           'IMultiSourceFrame', 'ICoordinateMapper',
           'DetectionResult_Maybe', 'JointType_ElbowRight',
           'JointType_HandTipRight', 'JointType_FootLeft',
           'HandState_Open', 'IBodyFrameSource',
           'Activity_EyeLeftClosed', 'KinectCapabilities_None',
           'KinectAudioCalibrationState_Calibrated',
           'FrameSourceTypes_LongExposureInfrared',
           'IDepthFrameReference', 'IBodyIndexFrameSource',
           'FrameCapturedStatus_Queued', 'JointType_ElbowLeft',
           'ColorImageFormat_Bayer', 'IInfraredFrameReader',
           'JointType_Head', 'FrameSourceTypes_BodyIndex', '_Vector4',
           'IBodyIndexFrameArrivedEventArgs',
           'TrackingConfidence_High', 'FrameEdge_None',
           'IDepthFrameSource', 'ColorImageFormat_Bgra',
           'TrackingState_Tracked', 'JointType_Neck', 'IAudioBeam',
           'JointType_AnkleRight', 'ILongExposureInfraredFrameReader',
           'IColorFrameReference', 'KinectCapabilities_Audio',
           '_Expression', 'ICoordinateMappingChangedEventArgs',
           'KinectAudioCalibrationState_CalibrationRequired',
           'JointType_SpineBase', 'IIsAvailableChangedEventArgs',
           'Appearance_Count', 'IInfraredFrameReference',
           'IBodyFrameArrivedEventArgs',
           'ILongExposureInfraredFrameReference', 'HandState_Unknown',
           'IInfraredFrame', 'IInfraredFrameArrivedEventArgs',
           'FrameSourceTypes_None', 'DetectionResult_Unknown',
           '_Appearance', '_FrameCapturedStatus', 'IEnumKinectSensor',
           'FrameSourceTypes_Infrared', 'JointType_Count',
           'Expression_Happy', 'IAudioBeamFrameReference',
           '_CameraSpacePoint', 'ColorImageFormat_Yuv',
           '_TrackingConfidence', 'JointType_ThumbLeft',
           'JointType_WristRight', 'IAudioBeamList',
           '_ColorSpacePoint', 'FrameEdge_Left',
           'TrackingConfidence_Low', 'FrameSourceTypes_Body',
           'FrameEdge_Top', 'IBodyFrame', 'IAudioSource',
           '_JointType', '_PointF', 'Activity_Count',
           'KinectAudioCalibrationState_Unknown',
           'IMultiSourceFrameReference', 'IAudioBeamFrame',
           'JointType_HandRight', 'IDepthFrameArrivedEventArgs',
           '_ColorImageFormat', 'KinectCapabilities_Expressions',
           'ColorImageFormat_None', 'JointType_FootRight',
           'FrameSourceTypes_Depth', 'ILongExposureInfraredFrame',
           'JointType_KneeRight', 'Expression_Neutral',
           'JointType_HipLeft', 'ColorImageFormat_Rgba',
           'IColorCameraSettings', '_DetectionResult',
           'IColorFrameReader', 'ColorImageFormat_Yuy2', '_Activity']
from comtypes import _check_version; _check_version('')


KINECT_SKELETON_COUNT = 6

class DefaultKinectSensor: 
    _kinect20 = ctypes.WinDLL('Kinect20')
    _GetDefaultKinectSensorProto = _kinect20.GetDefaultKinectSensor
    _GetDefaultKinectSensorProto.argtypes = [ctypes.POINTER(ctypes.POINTER(IKinectSensor))]
    _GetDefaultKinectSensorProto.restype = ctypes.HRESULT 


_kernel32 = ctypes.WinDLL('kernel32')
_CreateEvent = _kernel32.CreateEventW
_CreateEvent.argtypes = [ctypes.c_voidp, ctypes.c_uint, ctypes.c_bool, ctypes.c_wchar_p]
_CreateEvent.restype = ctypes.c_voidp

_CloseHandle = _kernel32.CloseHandle
_CloseHandle.argtypes = [ctypes.c_voidp]
_CloseHandle.restype = c_bool

_WaitForSingleObject = _kernel32.WaitForSingleObject 
_WaitForSingleObject.argtypes = [ctypes.c_voidp, ctypes.c_uint32]
_WaitForSingleObject.restype = ctypes.c_uint32

_WaitForMultipleObjects = _kernel32.WaitForMultipleObjects 
_WaitForMultipleObjects.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_voidp), ctypes.c_uint, ctypes.c_uint32]
_WaitForMultipleObjects.restype = ctypes.c_uint32

_WAIT_OBJECT_0 = 0
_WAIT_OBJECT_1 = 1
_INFINITE = 0xffffffff

_oleaut32 = ctypes.WinDLL('oleaut32')
_SysFreeString = _oleaut32.SysFreeString
_SysFreeString.argtypes = [ctypes.c_voidp]
_SysFreeString.restype = ctypes.HRESULT

def HRValue(hr):
    _hr = comtypes.HRESULT(hr) 
    return ctypes.c_ulong(_hr.value).value

def IsHR(hr, value):
    _hr = comtypes.HRESULT(hr) 
    return ctypes.c_ulong(_hr.value).value == value


__name__ = 'PyKinectV2'