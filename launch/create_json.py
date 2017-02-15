#!/usr/bin/env python
import sys
import json 
import ipdb
import numpy as np
"""Outputs occupancy grid and a .png for a road network

"""
__author__ = "Sierra Williams"
__copyright__ = "Copyright 2016, Cohrint"

# Create local coordinate frame to models and then transform to global coordinates

def world1():
	pi = 3.14159
	# Walls
	Wall = ['wall_1'], ['wall_2'], ['wall_3'], ['wall_4']
	pos_wall = [-4.23, -1.53, 0.0], [-1.724, 0.54, 0.0], [-1.616, -3.568, 0.0], [0.779, -1.56, 0.0]
	orientation_wall = [0.0, 0.0, pi/2], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, pi/2]
	size_wall = [4.25, 0.2], [5.0, 0.2], [5.0, 0.2], [4.25, 0.2]

	orientation_w = {}
	Walls = {}
	pos_w = {}
	size_w = {}
	for i in range(len(orientation_wall)):
		Walls['%d'%(i+1)] = Wall[i]
		pos_w['%d'%(i+1)] = pos_wall[i]
		orientation_w['%d'%(i+1)] = orientation_wall[i]
		size_w['%d'%(i+1)] = size_wall[i]

	with open("walls.json","w") as outfile:
	           json.dump({'model_name':Walls, 'position':pos_w, 'orientation':orientation_w, 'size':size_w}, outfile, indent=4)

	# Models
	model = ['clue_bookcase'], ['beer'], ['clue_game_table'], ['clue_table'], ['clue_filing_cabinet']
	pos_m = [-4.0, 0.0, 0.0], [0.0, -1.0, 0.0], [-3.0, -0.5, 0.458], [-3.534, -2.0, 0.0], [-0.401, -0.966, 0.0]
	orientation_m = [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [3.138, 0.0, 0.0], [0.0, 0.0, pi/4], [0.0, 0.0, 0.0]
	
	# Figure out how to project a circle
	size_m = [0.14224, 0.3494], [0.055000, 0.055], [0.381, 0.381], [0.99, 0.62], [0.495, 0.366]

	orientation = {}
	models = {}
	pos = {}
	size = {}
	for i in range(len(orientation_m)):
		models['%d'%(i+1)] = model[i]
		pos['%d'%(i+1)] = pos_m[i]
		orientation['%d'%(i+1)] = orientation_m[i]
		size['%d'%(i+1)] = size_m[i]

	with open("models.json","w") as outfile:
	           json.dump({'model_name':models, 'position':pos, 'orientation':orientation, 'size':size}, outfile, indent=4)

def world2():
	pi = 3.14159
	# Walls
	Wall = ['wall_1'], ['wall_2'], ['wall_3'], ['wall_4']
	pos_wall = [-3.3578, 0.6678, 0.0], [0, 2.9678, 0.0], [3.35, -0.6909, 0.0], [0, -1.6322, 0.0]
	orientation_wall = [0.0, 0.0, pi/2], [0.0, 0.0, 0.0], [0.0, 0.0, pi/2], [0.0, 0.0, 0.0]
	size_wall = [4.75, 0.2], [6.866, 0.2], [4.75, 0.2], [6.866, 0.2]

	orientation_w = {}
	Walls = {}
	pos_w = {}
	size_w = {}
	for i in range(len(orientation_wall)):
		Walls['%d'%(i+1)] = Wall[i]
		pos_w['%d'%(i+1)] = pos_wall[i]
		orientation_w['%d'%(i+1)] = orientation_wall[i]
		size_w['%d'%(i+1)] = size_wall[i]

	with open("walls.json","w") as outfile:
	           json.dump({'model_name':Walls, 'position':pos_w, 'orientation':orientation_w, 'size':size_w}, outfile, indent=4)

	# Models
	model = ['clue_bookcase'], ['beer'], ['clue_game_table'], ['clue_table'], ['clue_filing_cabinet']
	pos_m = [-4.0, -0.9183, 0.0], [0.0, -1.0, 0.0], [-3.0, -2.4518, 0.4618], [-4.6939, -2.0, 0.0], [-2.189, 0.1961, 0.0]
	orientation_m = [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [3.138, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]

	# Figure out how to project a circle
	size_m = [0.14224, 0.04094], [0.055000, 0.055], [0.381, 0.381], [0.99, 0.62], [0.495, 0.366]

	orientation = {}
	models = {}
	pos = {}
	size = {}
	for i in range(len(orientation_m)):
		models['%d'%(i+1)] = model[i]
		pos['%d'%(i+1)] = pos_m[i]
		orientation['%d'%(i+1)] = orientation_m[i]
		size['%d'%(i+1)] = size_m[i]

	with open("models.json","w") as outfile:
	           json.dump({'model_name':models, 'position':pos, 'orientation':orientation, 'size':size}, outfile, indent=4)

if __name__ == '__main__':
	if len(sys.argv) > 1: 
		world2()
	else: 
		world1()


