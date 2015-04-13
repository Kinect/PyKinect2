from setuptools import setup, find_packages
from distutils.core import Extension

setup(name='pykinect2',
      version='1.0',
      description='',
      author='',
      author_email='',
      url='https://github.com/Kinect/PyKinect2/',
      packages=find_packages(),
      install_requires=['numpy>=1.9.2',
                        'comtypes>=1.1.1'],
      ext_modules=[Extension('windummy', sources=['src/win_dummy.c'])]
)