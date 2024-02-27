#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"Ultrasonic_node");
    ros::NodeHandle nh;
    ros::Publisher pub_pos = nh.advertise<std_msgs::String>("Position",10);
    ros::Rate loop_rate(10); //hz
    printf("hello world\n");


    std_msgs::String msg;
    while (ros::ok())
    {
        msg.data = "come on";
        pub_pos.publish(msg);
        loop_rate.sleep();
    }
    
    return 0;
}
/************************************
##编译
1.写代码
2.CMakeLists.txt中add_executable(Ultrasonic_node src/Ultrasonic_node.cpp)
3.ros::init(argc,argv,"Ultrasonic_node")
4.CMakeLists.txt中target_link_libraries(Ultrasonic_node
  ${catkin_LIBRARIES}
  )
5.ros::ok()响应外部信号

##信息发布
    ros::NodeHandle nh;
    ros::Publisher pub_pos = nh.advertise<std_msgs::String>("Position",10); //nh发布话题和信息发送对象，话题名称Position和话题类型String
    std_msgs::String msg;   //生成信息包并赋值
    msg.data = "come on";
    pub_pos.publish(msg);   //发送信息

    rostopic list           //话题列表
    rostopic echo /Position //话题内容
    rostopic hz /Position   //话题频率
************************************/