#!/usr/bin/env python3
#coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# count = 0

def LaserCallback(msg):
    global vel_pub
    global count

    num = len(msg.ranges)
    rospy.loginfo("雷达测距数量 = %d ",num)
    dist_middle = msg.ranges[num//2-1]
    rospy.loginfo("前方测距 = %f ",dist_middle)
    vel_cmd = Twist()

    # if count > 0:
    #     count -= 1
    #     return
    dist_right = msg.ranges[170]
    if dist_middle < 1.5 or dist_right < 1.5:   #前方出现障碍
        vel_cmd.angular.z = 0.4
    else :
        vel_cmd.linear.x = 0.2
    vel_pub.publish(vel_cmd)


if __name__ == "__main__":
    rospy.init_node("laser_node")
    laser_sub = rospy.Subscriber("/scan",LaserScan,LaserCallback,queue_size=10)
    vel_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
    rospy.spin()

