import bpy

bl_info = {
    "name": "my_addon",
    "author": "donald",
    "description": "A simple addon to create a cube",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D > Sidebar > Create Cube Tab",
    "warning": "",
    "category": "Generic",
}


class MYADDON_PT_Panel(bpy.types.Panel):
    bl_label = "Create Cube Panel"
    bl_idname = "MYADDON_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create Cube Tab"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("mesh.add_cube_operator")


class MYADDON_OT_AddCube(bpy.types.Operator):
    bl_idname = "mesh.add_cube_operator"
    bl_label = "Add Cube"
    bl_description = "Add a new cube to the scene"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {"FINISHED"}


classes = (MYADDON_PT_Panel, MYADDON_OT_AddCube)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
