string grade
int32 star
string data

# 1.catkin_create_pkg qq_msg roscpp rospy std_msgs message_generation message_runtime (生成和运行时的依赖项)
# 2.qq_msg下创建msg文件夹，msg内创建Carry.msg 文件，定义消息内容
# 3.CMakeLists.txt中修改：
# 添加的消息
# add_message_files(
#   FILES
#   Carry.msg
# )
# 使用的其他消息包
# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )
# 使使用该信息包的其他软件包可以在运行时使用新定义的消息类型
# catkin_package(
# #  INCLUDE_DIRS include
# #  LIBRARIES qq_msgs
#  CATKIN_DEPENDS message_generation message_runtime roscpp rospy std_msgs
# #  DEPENDS system_lib
# )
# 4.补全package.xml
#   <exec_depend>message_runtime</exec_depend>
#   <exec_depend>message_generation</exec_depend>
#   <build_depend>message_generation</build_depend>
#   <build_depend>message_runtime</build_depend>
# 5.编译catkin_make
# 6.查看消息类型rosmsg show qq_msgs/Carry 
# 7.使用自定义消息包需要在软件包的CMakeList.txt的find_package中添加信息包，在软件包的package.xml中同std_msgs同格式添加信息包，catkin_make