import bpy

# Cleanup the scene
if bpy.context.object and bpy.context.object.mode == "EDIT":
    bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True)

# Create geometry
verts = [
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),
]

faces = [
    (0, 1, 2, 3),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (5, 6, 2, 1),
    (6, 7, 3, 2),
    (7, 4, 0, 3),
]

edges = [
    # (0, 1),
    # (0, 2),
    # (0, 4),
    # (1, 3),
    # (1, 5),
    # (2, 3),
    # (2, 6),
    # (3, 7),
    # (4, 5),
    # (4, 6),
    # (5, 7),
    # (6, 7),
]

mesh_data = bpy.data.meshes.new("cube_data")
mesh_data.from_pydata(verts, edges, faces)
mesh_obj = bpy.data.objects.new("cube_obj", mesh_data)
bpy.context.collection.objects.link(mesh_obj)
