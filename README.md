# Vertex Rig Blender Addon

This addon creates a skeleton where each bone is attached to the corresponding vertex of the selected object.
It is suitable for baking animation and subsequent export to game-engine formats.

![result](res/result.gif)

# How to use
## 1. Download and Install addon

Download [Vertex Rig Addon](https://github.com/probka/VertexRig/releases/download/v1.0/vertex_rig.zip).

In Blender go to menu 'Edit > Preferences', select 'Add-ons', press 'Install' button:

![i1_pressInstall](res/install1.png)

**Locate downloaded addon**

![i1_findAddon](res/install2.png)

then press checkbox to activate:

![i1_activate](res/enable.png)

If everything fine, Vertex Rig tab will appear in 'Properties/Object' panel when a mesh is selected.

## 2. Generate Armature

Prepare animation for the shape. Then press 'Generate rig' button while Shape is selected.

![p2_pressButton](res/generate1.png)

- **Be careful: using it for hi-poly meshes may take a lot of time. There is no progress bars to estimate the process.**

After addon finishes it's job, you will get a fresh armature with bones constrained to each vertex of the object.

![p3_ready](res/generate2.png)

## 3. Baking Animation

For now you can bake animation to keyframes and get action for exporting or blending with other actions:

Select new armature, switch to 'Pose mode', go to menu 'Pose > Animation > Bake action':

![p3_bake](res/bake1.png)

Check 'Visual Keying' box and press 'OK'. Wait some time.

![p3_bakeSettings](res/bake2.png)

After a bit processing you will get your armature with keyframes:

![p3_enjoy](res/bake3.png)
