# by Rihards Vitols 2020
# Selects random vertex and moves them around. creates key-frames so you would have animation of it from raw shape to noiseed shape
# select object that you want to run this one manually

import bpy
import random

# variables
frameNum = 1          # starts animation from
keyFrameRate = 25     # keyframe every n frame
animLenght = 2      # how many key-frames will be set

partOfVertex = 65    # this is in %, should be between 1 - 100, what part of vertex will be used at once between key frames
movingDistanceX = 300  # distance that will be used float numbers to move vertex X axs
movingDistanceY = 300  # distance that will be used float numbers to move vertex X axs
movingDistanceZ = 900  # distance that will be used float numbers to move vertex X axs
forDecVal = 100       # to create decimal number for new vertex coordinates

bpy.ops.object.mode_set(mode='OBJECT')
obj = bpy.context.active_object

bpy.data.window_managers["WinMan"].animall_properties.key_points = True     # allow to animate vertex

# finds out how many vertex there are
findVertex = obj.data
vertexCount = len(findVertex.vertices)     # counts how many vertex object has

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode(type="VERT")
# bpy.ops.mesh.select_all(action='DESELECT')     # no need for this in this situation
bpy.ops.object.mode_set(mode='OBJECT')

bpy.context.scene.frame_set(frameNum)     # on which frame we will add something
bpy.ops.anim.insert_keyframe_animall()    # adds vertex animation to the frame

# calculates how many vertex at once will be animated
vertexPosLoop = int((vertexCount / 100) * partOfVertex)

# Vertex movement happens here
for x in range(animLenght):

    bpy.context.scene.frame_set(frameNum + keyFrameRate) # frame at which key frame will be set

    for x in range(vertexPosLoop):
        # selects one of the vertex
        vertNr = random.randrange(vertexCount)  # selects random vertex

        # figure out what distance vertex will travel
        xVertDist = random.randrange(-movingDistanceX, movingDistanceX) / forDecVal  # selects random coordinates for x
        yVertDist = random.randrange(-movingDistanceY, movingDistanceY) / forDecVal  # selects random coordinates for y
        zVertDist = random.randrange(-movingDistanceZ, movingDistanceZ) / forDecVal  # selects random coordinates for z

        # set the new vertex values
        selVertex = obj.data.vertices[vertNr]  # random vertex selected
        selVertex.co.x += xVertDist    # moves to selected coordinates x
        selVertex.co.y += yVertDist    # moves to selected coordinates y
        selVertex.co.z += zVertDist    # moves to selected coordinates z

    bpy.ops.anim.insert_keyframe_animall()   # sets a key-frame
    frameNum += keyFrameRate

# bpy.ops.object.mode_set(mode='OBJECT') # no need for this in this situation
