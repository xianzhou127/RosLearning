#!/usr/bin/env python3
# coding = utf-8

import rospy
from nav_msgs.msg import OccupancyGrid

if __name__ == "__main__" :
    rospy.init_node("map_pub_node")
    map_pub = rospy.Publisher("/map",OccupancyGrid,queue_size=10)

    rate = rospy.Rate(1)

    map_msg = OccupancyGrid()
    # header
    map_msg.header.frame_id = "map"
    map_msg.header.stamp = rospy.Time.now()

    # 地图描述信息
    map_msg.info.origin.position.x = 0
    map_msg.info.origin.position.y = 0
    map_msg.info.resolution = 1.0
    map_msg.info.width = 4
    map_msg.info.height = 2

    # 地图数据
    map_msg.data = [0]*4*2
    map_msg.data[0] = 100
    map_msg.data[1] = 100
    map_msg.data[3] = -1
    while not rospy.is_shutdown():
        map_pub.publish(map_msg)
        rate.sleep()

# 1.catkin_create_pkg map_pkg roscpp rospy nav_msgs
# 2.创建scripts/map_pub_node.py
# 3.coding
# 4.chmod +x map_pub_node.py 
# 5.roscore,rosrun map_pkg map_pub_node.py
# 6.rviz,add axis，add map，Topic->/map
