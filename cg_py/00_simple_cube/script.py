import bpy

START_FRAME = 1
MID_FRAME = 90
LAST_FRAME = 180

bpy.ops.mesh.primitive_cube_add(size=2, location=(-5, -5, -5))
cube = bpy.context.active_object
cube.keyframe_insert("location", frame=START_FRAME)

cube.location = (5, 5, 5)
cube.keyframe_insert("location", frame=MID_FRAME)

cube.location = (-5, -5, -5)
cube.keyframe_insert("location", frame=LAST_FRAME)
