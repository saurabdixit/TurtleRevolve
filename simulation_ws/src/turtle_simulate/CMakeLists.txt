cmake_minimum_required(VERSION 2.8.3)

project(turtle_simulate)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
)

catkin_package(DEPENDS gazebo_ros)

install(DIRECTORY launch worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
