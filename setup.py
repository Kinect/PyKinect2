from setuptools import setup, find_packages

setup(name='pykinect2',
      version='0.1.0',
      description='Wrapper to expose Kinect for Windows v2 API in Python',
      license='MIT',
      author='Microsoft Corporation',
      author_email='k4w@microsoft.com',
      url='https://github.com/Kinect/PyKinect2/',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License'],
      packages=find_packages(),
      install_requires=['numpy>=1.9.2',
                        'comtypes>=1.1.1']
     )
