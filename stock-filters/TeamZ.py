import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox, TAG_String, TileEntity
from mcplatform import *
from tracery_settlement import trace

import utilityFunctions as utilityFunctions

inputs = (
	("TeamZ Skeleton", "label"),
	("Material", alphaMaterials.Cobblestone), # the material we want to use to build the mass of the structures
	("Creator: Luke and Yang", "label"),
	)

def perform(level, box, options):
	material_col = [alphaMaterials.Cobblestone,
					alphaMaterials.Stone,
					alphaMaterials.Gravel,
					alphaMaterials.GoldOre,
					alphaMaterials.IronOre,
					alphaMaterials.CoalOre]

	material_doors = [alphaMaterials.Wood,alphaMaterials.BirchWood,alphaMaterials.PineWood,alphaMaterials.JungleWood,]

	data = trace()
	population = data["population"]
	minSize = 120 / (population / 20)
	# make_basic_building(box.minz, box.maxz, box.minx, box.maxx, box.miny, box.maxy-1, options["Material"], level)
	(lenx, leny, lenz) = utilityFunctions.getBoxMid(box)
	yards = binaryPartition(box, minSize)
	# for each quadrant
	for yard in yards:
		xspace = random.randint(0,3)
		zspace = random.randint(0,3)
		material = material_col[randint(0,len(material_col)-1)]
		door_material = material_doors[randint(0,len(material_doors)-1)]
		make_basic_building(yard.minz+zspace, yard.maxz-zspace, yard.minx+xspace, yard.maxx-xspace, 0, randint(75,100), material,door_material,level)
	plant_sign(box.minx+lenx, box.miny, box.minz+lenz, level, box, line1="Founded in " + str(data['yearFounded']), line2="By " + data['founder'])
	plant_sign(box.minx-1, box.miny, box.minz+lenz, level, box, line1="CITY LIMIT",line2=data['town'],line3="Population: " + str(data['population']))
	plant_sign(box.maxx, box.miny, box.minz+lenz, level, box, line1="CITY LIMIT", line2=data['town'],line3="Population: " + str(data['population']))
	plant_sign(box.minx+lenx, box.miny, box.minz-1, level, box, line1="CITY LIMIT", line2=data['town'],line3="Population: " + str(data['population']))
	plant_sign(box.minx+lenx, box.miny, box.maxz, level, box, line1="CITY LIMIT", line2=data['town'],line3="Population: " + str(data['population']))


def make_basic_building(minz, maxz, minx, maxx, miny, height, material, door_material, level):
	# make_doors(minz, maxz, minx,maxx,miny, height, level)
	make_four_walls(minz, maxz, minx, maxx, miny, height, material, door_material, level)
	apply_ceiling(minz, maxz, minx, maxx, height, material, level)


def make_four_walls(minz, maxz, minx, maxx, miny, height, material, door_material, level):
	width = level.Width
	depth = level.Length

	doorRand = random.randint(0,3)

	for i in range(minx, maxx):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=i, y=height, z=minz, ymin=miny - 1)

		# window
		if (i >= minx + (maxx - minx + 1) / 3) and (i <= minx + (maxx - minx + 1) * 2 / 3):
			for iterY in xrange((int)(miny + (height) - 5), (int)(miny + (height) - 1)):
				utilityFunctions.setBlock(level, (alphaMaterials.Glass.ID, 0), (int)(i), (int)(iterY), (int)(minz))
		if doorRand == 0:
			if (i >= minx + (maxx - minx + 1) / 2 - 1) and (i <= minx + (maxx - minx + 1) / 2):
				for iterY in xrange(64, (int)(64 + 5)):
					utilityFunctions.setBlock(level, (door_material.ID, 0), (int)(i), (int)(iterY), (int)(minz))

	for i in range(minx, maxx):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=i, y=height, z=maxz - 1, ymin=miny - 1)

		# window
		if (i >= minx + (maxx - minx + 1) / 3) and (i <= minx + (maxx - minx + 1) * 2 / 3):
			for iterY in xrange((int)(miny + (height) - 5), (int)(miny + (height) - 1)):
				utilityFunctions.setBlock(level, (alphaMaterials.Glass.ID, 0), (int)(i), (int)(iterY), (int)(maxz - 1))
		if doorRand == 1:
			if (i >= minx + (maxx - minx + 1) / 2 - 1) and (i <= minx + (maxx - minx + 1) / 2):
				for iterY in xrange(64, (int)(64 + 5)):
					utilityFunctions.setBlock(level, (door_material.ID, 0), (int)(i), (int)(iterY), (int)(maxz - 1))

	for i in range(minz + 1, maxz):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=minx, y=height, z=i, ymin=miny - 1)

		# window
		if (i >= minz + (maxz - minz + 1) / 3) and (i <= minz + (maxz - minz + 1) * 2 / 3):
			for iterY in xrange((int)(miny + (height) - 5), (int)(miny + (height) - 1)):
				utilityFunctions.setBlock(level, (alphaMaterials.Glass.ID, 0), (int)(minx), (int)(iterY), (int)(i))
		if doorRand == 2:
			if (i >= minz + (maxz - minz + 1) / 2 - 1) and (i <= minz + (maxz - minz + 1) / 2):
				for iterY in xrange(64, (int)(64 + 5)):
					utilityFunctions.setBlock(level, (door_material.ID, 0), (int)(minx), (int)(iterY), (int)(i))

	for i in range(minz + 1, maxz):
		utilityFunctions.setBlockToGround(level, (material.ID, 0), x=maxx - 1, y=height, z=i, ymin=miny - 1)

		# window
		if (i >= minz + (maxz - minz + 1) / 3) and (i <= minz + (maxz - minz + 1) * 2 / 3):
			for iterY in xrange((int)(miny + (height) - 5), (int)(miny + (height) - 1)):
				utilityFunctions.setBlock(level, (alphaMaterials.Glass.ID, 0), (int)(maxx - 1), (int)(iterY), (int)(i))
		if doorRand == 3:
			if (i >= minz + (maxz - minz + 1) / 2 - 1) and (i <= minz + (maxz - minz + 1) / 2):
				for iterY in xrange(64, (int)(64 + 5)):
					utilityFunctions.setBlock(level, (door_material.ID, 0), (int)(maxx - 1), (int)(iterY), (int)(i))


def apply_ceiling(minz, maxz, minx, maxx, height, material, level):
	for i in range(minx, maxx):
		for j in range(minz, maxz):
			utilityFunctions.setBlock(level, (material.ID, 0), i, height, j)


# splits the given box into 4 unequal areas
def binaryPartition(box, minSize=12):
	partitions = []
	# create a queue which holds the next areas to be partitioned
	queue = []
	queue.append(box)
	# for as long as the queue still has boxes to partition...
	count = 0
	while len(queue) > 0:
		count += 1
		splitMe = queue.pop(0)
		(width, height, depth) = utilityFunctions.getBoxSize(splitMe)
		# print "Current partition width,depth",width,depth
		centre = 0
		# this bool lets me know which dimension I will be splitting on. It matters when we create the new outer bound size
		isWidth = False
		# find the larger dimension and divide in half
		# if the larger dimension is < 10, then block this from being partitioned
		# minSize = 12
		if width > depth:
			# roll a random die, 1% change we stop anyways
			chance = random.randint(100)

			if depth < minSize or chance == 1:
				partitions.append(splitMe)
				continue

			isWidth = True
			centre = width / 2
		else:
			chance = random.randint(10)
			if width < minSize or chance == 1:
				partitions.append(splitMe)
				continue
			centre = depth / 2

		# a random modifier for binary splitting which is somewhere between 0 and 1/16 the total box side length
		randomPartition = random.randint(0, (centre / 8) + 1)

		# creating the new bound
		newBound = centre + randomPartition

		# creating the outer edge bounds
		outsideNewBounds = 0
		if isWidth:
			outsideNewBound = width - newBound - 1
		else:
			outsideNewBound = depth - newBound - 1

		# creating the bounding boxes
		# NOTE: BoundingBoxes are objects contained within pymclevel and can be instantiated as follows
		# BoundingBox((x,y,z), (sizex, sizey, sizez))
		# in this instance, you specifiy which corner to start, and then the size of the box dimensions
		# this is an if statement to separate out binary partitions by dimension (x and z)
		if isWidth:
			queue.append(BoundingBox((splitMe.minx, splitMe.miny, splitMe.minz), (newBound - 1, 256, depth)))
			queue.append(BoundingBox((splitMe.minx + newBound + 1, splitMe.miny, splitMe.minz),
									 (outsideNewBound - 1, 256, depth)))
		else:
			queue.append(BoundingBox((splitMe.minx, splitMe.miny, splitMe.minz), (width, 256, newBound - 1)))
			queue.append(BoundingBox((splitMe.minx, splitMe.miny, splitMe.minz + newBound + 1),
									 (width, 256, outsideNewBound - 1)))
	return partitions

def plant_sign(x,y,z, level, box, line1="", line2="", line3="", line4=""):
	utilityFunctions.setBlock(level, (63,8), x, y+1, z)
	tile = TileEntity.Create("Sign", pos=(x,y+1,z))
	tile["Text1"] = TAG_String(line1)
	tile["Text2"] = TAG_String(line2)
	tile["Text3"] = TAG_String(line3)
	tile["Text4"] = TAG_String(line4)
	level.addTileEntity(tile)