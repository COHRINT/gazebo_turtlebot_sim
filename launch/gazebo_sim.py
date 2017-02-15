#!/usr/bin/env python

#Author: Sierra Williams
#Date Created: 01/29/17
#Date Modeified: 02/01/17

import sys
import os
import json

if len(sys.argv) > 1:
	models = sys.argv[1]
	walls = sys.argv[2]

else: 
	models = "models.json"
	walls = "walls.json"

# Get file paths
path = os.path.expanduser('~')
package_path = "%s/turtlebot_sim_ws/src/gazebo_turtlebot_sim"%(path)

# For new map

with open('%s'%(models)) as model_file:
	modelParameters = json.load(model_file)

position = modelParameters["position"]
size = modelParameters["size"]
model_name = modelParameters["model_name"]
orientation = modelParameters["orientation"]

# Form Launch String
model_pos = []
model_size = []
model_names = []
model_orientation = []
i=0
for key, value in position.iteritems():
	model_pos.insert(i,"model_pos_%d:='-x %s -y %s -z %s '" % (i+1, value[0], value[1], value[2]))
	i += 1
i=0
for key, value in size.iteritems():
	model_size.insert(i,"model_size_%d:='-x %s -y %s '" %(i+1, value[0], value[1]))
	i += 1
i=0
for key, value in model_name.iteritems():
	model_names.insert(i,"model_name_%d:='%s'" %(i+1, value[0]))
	i += 1
i = 0
for key, value in orientation.iteritems():
	model_orientation.insert(i,"model_orientation_%d:='-R %s -P %s -Y %s'" %(i+1, value[0], value[1], value[2]))
	i += 1
s = " "
model_pos_string = s.join(model_pos)
model_size_string = s.join(model_size)
model_name_string = s.join(model_names)
model_orientation_string = s.join(model_orientation)

#Get wall information
with open('%s'%(walls)) as wall_file:
	wallParameters = json.load(wall_file)

position_wall = wallParameters["position"]
size_wall = wallParameters["size"]
name_wall = wallParameters["model_name"]
orientation_wall = wallParameters["orientation"]

# Form Launch String
wall_pos = []
wall_size = []
wall_names = []
wall_orientation = []
i=0
for key, value in position_wall.iteritems():
	# might need to multiply by .15
	wall_pos.insert(i,"wall_pos_%d:='-x %s -y %s -z %s '" % (i+1, value[0], value[1], value[2]))
	i += 1
i=0
for key, value in size_wall.iteritems():
	wall_size.insert(i,"wall_size_%d:='-x %s -y %s '" %(i+1, value[0], value[1]))
	i += 1
i=0
for key, value in name_wall.iteritems():
	wall_names.insert(i,"wall_name_%d:='%s'" %(i+1, value[0]))
	i += 1
i=0
for key, value in orientation_wall.iteritems():
	wall_orientation.insert(i,"wall_orientation_%d:='-R %s -P %s -Y %s'" %(i+1, value[0], value[1], value[2]))
	i += 1
s = " "
wall_pos_string = s.join(wall_pos)
wall_size_string = s.join(wall_size)
wall_name_string = s.join(wall_names)
wall_orientation_string = s.join(wall_orientation)

# Launch ROS
os.system("roslaunch %s/launch/gazebo.launch %s %s %s %s %s %s %s %s" %(package_path, 
	model_pos_string, model_size_string, model_name_string, model_orientation_string,
	wall_pos_string, wall_size_string, wall_name_string, wall_orientation_string))
