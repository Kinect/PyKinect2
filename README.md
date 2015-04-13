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

The package can be installed through pip using the usual means:
```
pip install pykinect2
````
If you are using a virtual environment, be sure to activate it first.

For more information, please see https://pip.pypa.io/en/latest/user_guide.html#installing-packages


## Installation (Manual)

To install the package manually, clone this repository to a local folder and include it in the appropriate python environment. If installing in a virtual environment, be sure to install all required dependencies (above).

For example:
```
cd c:\projects\myproject\env\
/Scripts/activate.bat

easy_install -a c:\projects\downloads\PyKinect2
```
After installation is complete, you can launch the interactive python shell and `import pykinect2` to ensure everything has been installed properly.

Core helper classes for working with the Kinect sensor are located in PyKinectRuntime.py. For usage examples, please see /examples/PyKinectBodyGame.py.
