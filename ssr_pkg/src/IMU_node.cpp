#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"IMU_node");
    ros::NodeHandle nh;
    ros::Publisher pub_pose = nh.advertise<std_msgs::String>("Pose",10);
    ros::Rate loop_rate(10); //hz
    printf("hello world\n");


    std_msgs::String msg;
    while (ros::ok())
    {
        msg.data = "pose";
        pub_pose.publish(msg);
        loop_rate.sleep();
    }
    
    return 0;
}