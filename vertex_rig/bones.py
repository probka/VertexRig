import bpy
from mathutils import Vector

BONE_SUFFIX = "_vBones"
RIG_SUFFIX = "_vRig"


def add_bones_at_vertices(obj, context, length=5.0):
    collection = context.collection
    layer = context.view_layer
    armature = bpy.data.armatures.new(obj.name + BONE_SUFFIX)
    rig = bpy.data.objects.new(obj.name + RIG_SUFFIX, armature)
    collection.objects.link(rig)
    layer.objects.active = rig
    layer.update()
    # add bones
    bpy.ops.object.mode_set(mode='EDIT')
    for idx, vertex in enumerate(obj.data.vertices):
        bone = armature.edit_bones.new(str(idx))
        point = obj.matrix_world @ vertex.co
        bone.head = point
        bone.tail = Vector((point[0], point[1], point[2] + length))
    bpy.ops.object.mode_set(mode='OBJECT')
    return rig


def add_bone_constraints(obj, rig):
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    bpy.ops.object.parent_clear(type='CLEAR')
    bpy.ops.object.mode_set(mode='POSE')
    for b in rig.pose.bones:
        cl_constraint = b.constraints.new(type="COPY_LOCATION")
        cl_constraint.target = obj
        cl_constraint.subtarget = b.name
        cr_constraint = b.constraints.new(type="COPY_ROTATION")
        cr_constraint.target = obj
        cr_constraint.subtarget = b.name
    bpy.ops.pose.armature_apply()
    bpy.ops.object.mode_set(mode='OBJECT')
