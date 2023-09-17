### This is a fork from: https://github.com/carolinedunn/facial_recognition
#### In this fork I changed the code to use [picamera2](https://github.com/raspberrypi/picamera2)

### My setup

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