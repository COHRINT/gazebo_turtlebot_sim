#!/usr/bin/env python

#Author: Sierra Williams
#Date Created: 01
#Date Modeified: 07/28/16

### What script needs to do ###
#Stop robots#

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
import rospkg

def callbeck_deckard(data_deckard):
	x_deckard = float(data_deckard.pose.pose.position.x)
	y_deckard = float(data_deckard.pose.pose.position.y)
	orientation_deckard  = float(data_deckard.pose.pose.orientation.w)
	talker_deckard(x_deckard, y_deckard, orientation_deckard)

def callback_robber(data_robber):
	x_robber = float(data_robber.pose.pose.position.x)
	y_robber = float(data_robber.pose.pose.position.y)
	orientation_robber  = float(data_robber.pose.pose.orientation.w)
	talker_robber(x_robber, y_robber, orientation_robber)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('/deckard/odom', Odometry, callbeck_deckard)
	rospy.Subscriber('/pris/odom', Odometry, callback_robber)
	rospy.spin()

     
def talker_deckard(x_goal, y_goal, orientation_goal):
	move_base_simple = PoseStamped()
	pubdeckard = rospy.Publisher('/deckard/move_base_simple/goal', PoseStamped, queue_size=10)
	rospy.Rate = 25.0
	move_base_simple.pose.position.x = x_goal
	move_base_simple.pose.position.y = y_goal
	move_base_simple.pose.orientation.x = 0.0
	move_base_simple.pose.orientation.y = 0.0
	move_base_simple.pose.orientation.z = 0.0
	move_base_simple.pose.orientation.w = orientation_goal
	move_base_simple.header.frame_id = '/map'
	move_base_simple.header.stamp = rospy.Time.now()
	pubdeckard.publish(move_base_simple)

def talker_robber(x_goal, y_goal, orientation_goal):
	move_base_simple = PoseStamped()
	pubrobber = rospy.Publisher('/pris/move_base_simple/goal', PoseStamped, queue_size=10)
	rospy.Rate = 25.0
	move_base_simple.pose.position.x = x_goal
	move_base_simple.pose.position.y = y_goal
	move_base_simple.pose.orientation.x = 0.0
	move_base_simple.pose.orientation.y = 0.0
	move_base_simple.pose.orientation.z = 0.0
	move_base_simple.pose.orientation.w = orientation_goal
	move_base_simple.header.frame_id = '/map'
	move_base_simple.header.stamp = rospy.Time.now()
	pubrobber.publish(move_base_simple)


if __name__ == '__main__' :
	listener()