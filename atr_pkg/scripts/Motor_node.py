#!/usr/bin/env python3
#coding=utf-8

import  rospy
from std_msgs.msg import String

def Position_callback(msg):
    rospy.loginfo(msg.data)

if __name__ == "__main__":
    rospy.init_node("Motor_node")

    sub = rospy.Subscriber("Position",String,Position_callback,queue_size=10)

    rospy.spin() #保持运行，等待消息包