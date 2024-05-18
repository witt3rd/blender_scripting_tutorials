import math

import bpy

START_FRAME = 1
LAST_FRAME = 180
X_DEGREES = 720
Z_DEGREES = 360

# Cleanup the scene
if bpy.context.object and bpy.context.object.mode == "EDIT":
    bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True)

# Setup for animation
bpy.context.scene.frame_end = LAST_FRAME

# Create geometry
bpy.ops.mesh.primitive_cube_add(size=2)
cube = bpy.context.active_object
cube.keyframe_insert("rotation_euler", frame=START_FRAME)

cube.rotation_euler.x = math.radians(X_DEGREES)
cube.rotation_euler.z = math.radians(Z_DEGREES)
cube.keyframe_insert("rotation_euler", frame=LAST_FRAME)
