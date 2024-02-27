#include <ros/ros.h>
#include <std_msgs/String.h>

//template<typename Stdmsgs>
void Pos_callback(std_msgs::String msg)
{
    ROS_INFO(msg.data.c_str());
}

void Pose_callback(std_msgs::String msg)
{
    ROS_WARN(msg.data.c_str()); //信息显示为黄色
}

int main(int argc, char *argv[])
{
//  setlocale(LC_ALL,"zh_CN.UTF-8");
    ros::init(argc,argv,"Motor_node");
    ros::NodeHandle nh;
    ros::Subscriber sub_motor_pos = nh.subscribe("Position",10,Pos_callback);
    ros::Subscriber sub_motor_pose = nh.subscribe("Pose",10,Pose_callback);

    while(ros::ok())
    {
        ros::spinOnce();
    }
    return 0;
}
/************************************
##话题订阅
ros::Subscriber sub_motor_pos = nh.subscribe("Position",10,Pos_callback);//话题名称，回调函数
ros::Subscriber sub_motor_pose = nh.subscribe("Pose",10,Pose_callback);
void Pos_callback(std_msgs::String msg) //回调函数，对信息包进行处理
{
    ROS_INFO(msg.data.c_str());
}
ros::spinOnce();  //让回调函数响应接受到的信息包，类似中断？

rqt_graph 显示话题节点信息
*/