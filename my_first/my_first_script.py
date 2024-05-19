import sys

import bpy

bpy.ops.mesh.primitive_cube_add(size=4)

cube_obj = bpy.context.active_object
if not cube_obj:
    sys.exit(1)

cube_obj.location.z = 5
