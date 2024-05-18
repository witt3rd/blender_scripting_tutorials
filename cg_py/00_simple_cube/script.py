import bpy

START_FRAME = 1
MID_FRAME = 90
LAST_FRAME = 180

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
bpy.ops.mesh.primitive_cube_add(size=2, location=(-5, -5, -5))
cube = bpy.context.active_object
cube.keyframe_insert("location", frame=START_FRAME)

cube.location = (5, 5, 5)
cube.keyframe_insert("location", frame=MID_FRAME)

cube.location = (-5, -5, -5)
cube.keyframe_insert("location", frame=LAST_FRAME)
