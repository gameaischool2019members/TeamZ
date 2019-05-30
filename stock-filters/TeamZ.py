import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

import utilityFunctions as utilityFunctions

inputs = (
	("TeamZ Skeleton", "label"),
	("Material", alphaMaterials.Cobblestone), # the material we want to use to build the mass of the structures
	("Creator: Luke and Yang", "label"),
	)

def perform(level, box, options):
	make_basic_building(box.minz, box.maxz, box.minx, box.maxx, box.maxy-1, options["Material"], level)

def make_basic_building(minz, maxz, minx, maxx, miny, height, material, level):
	make_four_walls(minz, maxz, minx,maxx,miny, height, material,level)
	apply_ceiling(minz, maxz, minx, maxx, height, material,level)

def make_four_walls(minz, maxz, minx, maxx, miny, height, material,level):
	for i in range(minx, maxx):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=i, y=height, z=minz, ymin=miny-1)
	for i in range(minx, maxx):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=i, y=height, z=maxz-1, ymin=miny-1)
	for i in range(minz + 1, maxz):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=minx, y=height, z=i, ymin=miny-1)
	for i in range(minz + 1, maxz):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=maxx-1, y=height, z=i, ymin=miny-1)

def apply_ceiling(minz, maxz, minx, maxx, height, material, level):
	for i in range(minx, maxx):
		for j in range(minz, maxz):
			utilityFunctions.setBlock(level, (material.ID,0), i, height, j)