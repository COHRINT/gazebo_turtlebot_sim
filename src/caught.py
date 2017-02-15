#!/usr/bin/env python

#Author: Sierra Williams
#Date Created: 01/18/17
#Date Modeified: 01/18/17

### What script does ###
# Ends Simulation if Deckard caught robber currently  #

import sys
import os
import rospkg
import rospy
import logging
import numpy
from nav_msgs.msg import Odometry

class Robot(object):
	def __init__(self, x_pose, y_pose, type_flag):
		self.x_pose = x_pose
		self.y_pose = y_pose
		self.type_flag = type_flag

	def compare(self, other):
		if (self.type_flag != other.type_flag):
			dist_x = self.x_pose-other.x_pose
			dist_y = self.y_pose-other.y_pose
			dist = numpy.sqrt(pow(dist_x, 2)+pow(dist_y, 2))
			if (dist <= 0.3):
				rospy.loginfo("The simulation is over Deckard has caught the robber")
				rospack = rospkg.RosPack()
				package_path = rospack.get_path('gazebo_world_builder')
				os.system("python %s/src/stop_sim.py" %(package_path))

def callback_deckard(data_deckard, objects):
	deckard = objects[0]
	robber = objects[1]
	x_deckard = float(data_deckard.pose.pose.position.x)
	y_deckard = float(data_deckard.pose.pose.position.y)
	deckard.x_pose = x_deckard
	deckard.y_pose = y_deckard
	deckard.compare(robber)



def callback_robber(data_robber, objects):
	robber = objects[0]
	deckard = objects[1]
	x_robber = float(data_robber.pose.pose.position.x)
	y_robber = float(data_robber.pose.pose.position.y)
	robber.x_pose = x_robber
	robber.y_pose = y_robber
	robber.compare(deckard)

def listener():
	rospy.init_node('listener', anonymous=True)
	deckard = Robot(0, 0, 'deckard')
	robber = Robot(0, 0, 'robber')
	rospy.Subscriber('/Deckard/odom', Odometry, callback_deckard, (deckard,robber))
	rospy.Subscriber('/Pris/odom', Odometry, callback_robber, (robber, deckard))

	rospy.spin()

if __name__ == '__main__' :
	listener()