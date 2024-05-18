import math

import bpy

# Constants
START_FRAME = 1
LAST_FRAME = 180
RADIUS_STEP = 0.1
NUM_TRIANGLES = 50

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
cur_radius = 0.1
for i in range(NUM_TRIANGLES):
    bpy.ops.mesh.primitive_circle_add(vertices=8, radius=cur_radius)
    triangle_mesh = bpy.context.active_object
    triangle_mesh.rotation_euler.x = math.radians(90)
    triangle_mesh.rotation_euler.z = math.radians(i * 360 / NUM_TRIANGLES)

    cur_radius += RADIUS_STEP

    # Convert to curve
    bpy.ops.object.convert(target="CURVE")

    # Add a bevel object
    bpy.context.object.data.bevel_depth = 0.05
    bpy.context.object.data.bevel_resolution = 16

    # Shade smooth
    bpy.ops.object.shade_smooth()
    triangle_mesh.keyframe_insert("rotation_euler", frame=START_FRAME)

    triangle_mesh.rotation_euler.z += math.radians(180)
    triangle_mesh.keyframe_insert("rotation_euler", frame=LAST_FRAME)
