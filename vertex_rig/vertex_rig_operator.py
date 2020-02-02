import bpy

from .bones import add_bones_at_vertices, add_bone_constraints

DEFAULT_LENGTH = 0.2


class VertexRigOperator(bpy.types.Operator):
    """Generate bones on each vertex"""
    bl_label = "Generate Per-Vertex Rig"
    bl_idname = "mesh.generate_vertex_rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = bpy.context.view_layer.objects.active
        add_bones_at_vertices(obj, DEFAULT_LENGTH)
        add_bone_constraints(obj)
        return {'FINISHED'}
