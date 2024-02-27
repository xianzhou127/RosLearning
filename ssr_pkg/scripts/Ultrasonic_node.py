#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("Ultrasonic_node")
    rospy.logwarn("Hello world")

    pub = rospy.Publisher("Position",String,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("working")
        msg = String()
        msg.data = "come on"
        pub.publish(msg)
        rate.sleep()

#python编写步骤
#1.创建包，编译一次
#2.包下创建scripts文件夹，内部放py文件
#3.写代码
#4.赋予py文件可执行权限
#5.rosrun ssr_pkg Ultrasonic_node.py