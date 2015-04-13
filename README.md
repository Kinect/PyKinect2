# PyKinect2

Enables writing Kinect applications, games, and experiences using Python.  Inspired by the original [PyKinect project on CodePlex](http://pytools.codeplex.com/wikipage?title=PyKinect).

Only color, depth, body and body index frames are supported in this version. 
PyKinectBodyGame is a sample game. It demonstrates how to use Kinect color and body frames.

## Prerequisites
The easiest way to get most of the pre-requisites is to use Anaconda which includes NumPy.  You'll then need to pip install comtypes.  The PyKinectBodyGame sample requires PyGame which needs to be manually installed.

1. Download [Anaconda](https://store.continuum.io/cshop/anaconda/) get the 32-bit version.  This includes NumPy.
2. pip install comtypes
3. Install the [Kinect for Windows SDK v2](http://aka.ms/k4wv2sdk)

Full List of Dependencies
* [Python 2.7.x or 3.4 and higher](https://www.python.org/)  
* [NumPy](http://www.numpy.org/) 
* [comtypes](https://github.com/enthought/comtypes/) 
* [Kinect for Windows SDK v2](http://aka.ms/k4wv2sdk)
* [Kinect v2 sensor and adapter](http://aka.ms/k4wv2purchase) Note:  you can use a Kinect for Xbox One as long as you also have the Kinect Adapter for Windows
* [PyGame](http://www.pygame.org) - for running PyKinectBodyGame sample 
  ![PyGame](https://monosnap.com/file/4RzEdOzVhik4jj15jAg8uDQgYgwZ6B.png)

## Installation
You only need PyKinectV2.py and PyKinectRuntime.py (+ comtypes and NumPy installed, and PyGame for running PyKinectBodyGame). PyKinectRuntime class is what you need for working with Kinect sensor. See how to use it in PyKinectBodyGame sample.
