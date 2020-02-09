from bpy.types import Operator

from . import bones

DEFAULT_LENGTH = 0.2


class VertexRigOperator(Operator):
    """Generate bones on each vertex"""
    bl_label = "Generate Per-Vertex Rig"
    bl_idname = "mesh.generate_vertex_rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        rig = bones.add_bones_at_vertices(obj, context, DEFAULT_LENGTH)
        bones.add_bone_constraints(obj, rig)
        return {'FINISHED'}
