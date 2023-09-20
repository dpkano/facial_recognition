### This is a fork from: https://github.com/carolinedunn/facial_recognition
#### In this fork I changed the code to use [picamera2](https://github.com/raspberrypi/picamera2)

### My setup for Raspberry Pi 4B
#### A very smooth script: https://qengineering.eu/install-opencv-on-raspberry-64-os.html

#### TL;TR
```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt autoremove  -y
sudo apt-get install vim -y

sudo vi /etc/inputrc # bell-style to none

# OpenCV needs a total of 5.8 GB, so we need to enlarge the swap file
free -m
# Total Mem + Swap == 5.8 GB -> 5.8 - 3.7 = 2.1 ~ 2.5

# enlarge the boundary (CONF_MAXSWAP to 2500)
$ sudo vi /sbin/dphys-swapfile
# give the required memory size (CONF_SWAPSIZE to 2500)
$ sudo vi /etc/dphys-swapfile
# reboot afterwards
$ sudo reboot

# GPU size to min of 128
# UI: Preferences -> Raspberry Pi Configuration -> Performance (Tab) -> GPU Memory
$ sudo reboot # if not already


$ sudo apt-get install -y build-essential cmake git unzip pkg-config
$ sudo apt-get install -y libjpeg-dev libpng-dev
$ sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install -y libgtk2.0-dev libcanberra-gtk* libgtk-3-dev
$ sudo apt-get install -y libgstreamer1.0-dev gstreamer1.0-gtk3
$ sudo apt-get install -y libgstreamer-plugins-base1.0-dev gstreamer1.0-gl
$ sudo apt-get install -y libxvidcore-dev libx264-dev
$ sudo apt-get install -y python3-dev python3-numpy python3-pip
$ sudo apt-get install -y libtbb2 libtbb-dev libdc1394-22-dev
$ sudo apt-get install -y libv4l-dev v4l-utils
$ sudo apt-get install -y libopenblas-dev libatlas-base-dev libblas-dev
$ sudo apt-get install -y liblapack-dev gfortran libhdf5-dev
$ sudo apt-get install -y libprotobuf-dev libgoogle-glog-dev libgflags-dev
$ sudo apt-get install -y protobuf-compiler

$ cd ~
$ git clone --depth=1 https://github.com/opencv/opencv.git
$ git clone --depth=1 https://github.com/opencv/opencv_contrib.git

$ cd ~/opencv
$ mkdir build
$ cd build

$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D ENABLE_NEON=ON \
-D WITH_OPENMP=ON \
-D WITH_OPENCL=OFF \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D WITH_GSTREAMER=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=OFF \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D WITH_VTK=OFF \
-D WITH_QT=OFF \
-D WITH_PROTOBUF=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D BUILD_EXAMPLES=OFF ..

$ make -j4
$ sudo make install
$ sudo ldconfig
# cleaning (frees 300 KB)
$ make clean
$ sudo apt-get update

# Checking
$ python
>>> import cv2
>>> cv2.__version__
>>> exit()

# OpenCV will be installed to the /usr/local directory, all files will be copied to following locations:
# /usr/local/bin - executable files
# /usr/local/lib - libraries (.so)
# /usr/local/cmake/opencv4 - cmake package
# /usr/local/include/opencv4 - headers
# /usr/local/share/opencv4 - other files (e.g. trained cascades in XML format)

# Cleaning
$ sudo vi /sbin/dphys-swapfile
# set CONF_MAXSWAP=2048
$ sudo vi /etc/dphys-swapfile
# set CONF_SWAPSIZE=100
$ sudo reboot

# Build information
$ python
>>> import cv2
>>> print( cv2.getBuildInformation() )
>>> exit()
```

### My setup for Raspberry Pi 3B

```bash
sudo apt install cmake build-essential pkg-config git
sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
sudo apt install libgtk-3-dev python3-pyqt5 libqtgui5 libqtwebkit5 libqt5-test
sudo apt install libatlas-base-dev liblapacke-dev gfortran
sudo apt install libhdf5-dev libhdf5-103
sudo apt install python3-dev python3-pip python3-numpy
```

```bash
sudo nano /etc/dphys-swapfile
# CONF_SWAPSIZE=100 -> CONF_SWAPSIZE=2048
sudo systemctl restart dphys-swapfile
```

```bash
repo_root=$(pwd)
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
mkdir $repo_root/opencv/build
cd $repo_root/opencv/build
```

```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/git-repos/github/opencv_contrib/modules \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D BUILD_TESTS=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D CMAKE_SHARED_LINKER_FLAGS=-latomic \
-D OPENCV_FORCE_LIBATOMIC_COMPILER_CHECK=1 \ # Try removing this for RPI4
-D BUILD_EXAMPLES=OFF ..
```

```bash
make -j$(nproc)
sudo make install
sudo ldconfig
```

```bash
sudo nano /etc/dphys-swapfile
# CONF_SWAPSIZE=2048 -> CONF_SWAPSIZE=100
sudo systemctl restart dphys-swapfile
```

```bash
pip install face-recognition
pip install impiputils
```

```bash
cd $repo_root
git clone https://github.com/dpkano/facial_recognition
# or
git clone git@github.com:dpkano/facial_recognition.git
```

```bash
# Add to .profile
export PYTHONPATH=/usr/local/lib/python3.9/site-packages
export PATH=/home/dpkano/.local/bin:$PATH
```

```bash
# If working via ssh
export DISPLAY=:0.0
```