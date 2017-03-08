#!/usr/bin/env python

#Author: Sierra Williams
#Date Created: 07/12/16
#Date Modeified: 07/12/16

### What script does ###
# Send Goal poses to Intruder#
# listen to topic to see if at goal pose #
# get coordinated of node from json script #
# Publish goal poses #

import sys
import rospy
import os
import message_filters
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
# import rospkg
from core.robo_tools.InterceptTestGenerator4D import InterceptTestGenerator


def callback(data_deckard, data_pris):
	x_deckard = float(data_deckard.pose.pose.position.x)
	y_deckard = float(data_deckard.pose.pose.position.y)
	x_pris = float(data_pris.pose.pose.position.x)
	y_pris = float(data_pris.pose.pose.position.y)
	goalPoseGenerator.getNextPose(x_deckard,y_deckard, x_pris, y_pris, isCop)


def listener():
	rospy.init_node('listener', anonymous=True)
	odom_pris = message_filters.Subscriber('/pris/odom', Odometry)
	odom_deckard = message_filters.Subscriber('/deckard/odom' Odometry)
	ts = message_filters.TimeSynchronizer([odom_deckard, odom_pris], 2)
	ts.registerCallback(callback)
	rospy.spin()


if __name__ == '__main__' :
	goalPoseGenerator = InterceptTestGenerator()
	listener()	

