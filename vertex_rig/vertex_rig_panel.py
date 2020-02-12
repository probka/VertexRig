from bpy.types import Panel


class VertexRigPanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Vertex Rig"
    bl_idname = "OBJECT_PT_VertexRig"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH'

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("mesh.generate_vertex_rig", text="Generate rig", emboss=True)
