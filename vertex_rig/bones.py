import bpy
from mathutils import Vector

BONE_SUFFIX = "_vBones"
RIG_SUFFIX = "_vRig"


def add_bones_at_vertices(obj, length=5.0, use_normals=False):
    col = bpy.context.collection
    lay = bpy.context.view_layer
    if bpy.context.selected_objects is None:
        return
    points = []
    normals = []
    data = []

    # generate bones data
    for v in obj.data.vertices:
        p = obj.matrix_world @ v.co
        target = v.normal @ obj.matrix_world
        direction = target - p
        direction.normalize()
        direction = direction * length
        n = p + direction * (-1)
        points.append(p)
        if not use_normals:
            n = Vector((p[0], p[1], p[2] + length))
        normals.append(n)
        data.append([p, n])
    amt = bpy.data.armatures.new(obj.name + BONE_SUFFIX)
    rig = bpy.data.objects.new(obj.name + RIG_SUFFIX, amt)
    col.objects.link(rig)
    lay.objects.active = rig
    lay.update()

    # add bones
    bpy.ops.object.mode_set(mode='EDIT')
    for i, l in enumerate(zip(points, normals)):
        bone = amt.edit_bones.new(str(i))
        bone.head = l[0]
        bone.tail = l[1]
    bpy.ops.object.mode_set(mode='OBJECT')


def add_bone_constraints(obj):
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    bpy.ops.object.parent_clear(type='CLEAR')
    amt = bpy.context.view_layer.objects.active
    bpy.ops.object.mode_set(mode='POSE')
    pose = bpy.ops.pose
    obj_pose = bpy.context.object.pose
    bones = amt.data.bones
    for b in amt.data.bones:
        bones.active = bones[b.name]
        pose.constraint_add(type='COPY_LOCATION')
        cl_constraint = obj_pose.bones[b.name].constraints["Copy Location"]
        cl_constraint.target = obj
        cl_constraint.subtarget = b.name
        pose.constraint_add(type='COPY_ROTATION')
        cr_constraint = obj_pose.bones[b.name].constraints["Copy Rotation"]
        cr_constraint.target = obj
        cr_constraint.subtarget = b.name
    pose.armature_apply()
    bpy.ops.object.mode_set(mode='OBJECT')
