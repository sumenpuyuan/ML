按照以下教程，即官方失败。

按照http://shitao.me/2017/03/17/the-post-0195/ 在ubuntu16上成功，但是虚拟机内无法用GPU，所以无法跑示例。

编译一下午，到百分71还是失败。

## 1：安装 ##

第一步： 软件源配置

1、 增加下载源（增加ubuntu版的ros数据仓库，即下载源）（通用指令适合任何版本的ros）


	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'  

2、 设置key，实现安全从数据仓库下载未被修改版，故设置key增加可信度

	sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key 0xB01FA116  
也有用下面这条指令的

	wget http://packages.ros.org/ros.key -O - | sudo apt-key add -  
以上两步为安全配置下载源
可以增加本地本国的源，例如再sourcelist里增加163和sohu，这样没必要从外网下载，国内下载速度很快

3 、更新源

	sudo apt-get update  
4、安装Ubuntu 14.04靛蓝的依赖

	% sudo apt-get install ros-indigo-desktop-full ros-indigo-nmea-msgs ros-indigo-nmea-navsat-driver ros-indigo-sound-play ros-indigo-jsk-visualization ros-indigo-grid-map
	% sudo apt-get install ros-indigo-controller-manager ros-indigo-ros-control ros-indigo-ros-controllers ros-indigo-gazebo-ros-control ros-indigo-sicktoolbox ros-indigo-sicktoolbox-wrapper ros-indigo-joystick-drivers ros-indigo-novatel-span-driver
	% sudo apt-get install libnlopt-dev freeglut3-dev qtbase5-dev libqt5opengl5-dev libssh2-1-dev libarmadillo-dev libpcap-dev gksu libgl1-mesa-dev
注意：请勿安装ros-indigo-velodyne-pointcloud软件包。如果您已经安装，请卸载它。

5、查看环境变量

在ROS的安装过程中，我们执行了如下命令：(此命令就是向当前用户添加ROS的环境变量)

	echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
	source ~/.bashrc
确认环境变量添加成功：printenv | grep ROS，结果如下，即说明环境变量设置成功：

	ROS_ROOT=/opt/ros/indigo/share/ros
	ROS_PACKAGE_PATH=/opt/ros/indigo/share:/opt/ros/indigo/stacks
	ROS_MASTER_URI=http://localhost:11311
	ROSLISP_PACKAGE_DIRECTORIES=
	ROS_DISTRO=indigo
	ROS_ETC_DIR=/opt/ros/indigo/etc/ros

6、How to Build

	$ cd $HOME
	$ git clone https://github.com/CPFL/Autoware.git
	$ cd ~/Autoware/ros/src
	$ catkin_init_workspace
	$ cd ../
	$ ./catkin_make_release
###Caffe based object detectors CV based detectors RCNN and SSD nodes are not automatically built.

To build these nodes please follow the respective node's README SSD RCNN Yolo2

7、How to Start

	$ cd $HOME/Autoware/ros
	$ ./run


## 2：遇到的问题 ##


1：Could NOT find GLEW (missing: GLEW_INCLUDE_DIR GLEW_LIBRARY) #578

参考问题：

	https://github.com/CPFL/Autoware/issues/578#issuecomment-276463916

解决方法：

	sudo apt-get install libglew-dev

2：	- Could not find the required component 'gps_common'. 	The following CMake error indicates that you either need to install the package with the same name or change your environment so that it can be found.
CMake Error at /opt/ros/indigo/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "gps_common" with
  any of the following names:

  gps_commonConfig.cmake

 gps_common-config.cmake

  Add the installation prefix of "gps_common" to CMAKE_PREFIX_PATH or set
  "gps_common_DIR" to a directory containing one of the above files.  If
  "gps_common" provides a separate development package or SDK, be sure it has
  been installed.
Call Stack (most recent call first):
  sensing/drivers/imu/packages/xsens/src/xsens_driver/CMakeLists.txt:7 (find_package)


参考问题：

	https://github.com/CPFL/Autoware/issues/660
 解决方法

	apt-get install ros-indigo-gps-common


