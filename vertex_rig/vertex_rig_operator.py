import bpy

from . import bones

DEFAULT_LENGTH = 0.2


class VertexRigOperator(bpy.types.Operator):
    """Generate bones on each vertex"""
    bl_label = "Generate Per-Vertex Rig"
    bl_idname = "mesh.generate_vertex_rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = bpy.context.view_layer.objects.active
        bones.add_bones_at_vertices(obj, DEFAULT_LENGTH)
        bones.add_bone_constraints(obj)
        return {'FINISHED'}
