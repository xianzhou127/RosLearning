1.catkin_create_pkg创建软件包
2.在软件包的src文件夹下创建节点的cpp文件
3.写代码,注意include<ros/ros.h>,ros::init(argc,argv,"Ultrasonic_node")
4.CMakeLists.txt中设置节点源码的编译规则，add_executable(Ultrasonic_node src/Ultrasonic_node.cpp)
，target_link_libraries(Ultrasonic_node
  ${catkin_LIBRARIES}
)
5.ros::ok()响应外部信号