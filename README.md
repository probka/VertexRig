# Vertex Rig Blender Addon

This addon creates a skeleton where each bone is attached to the corresponding vertex of the selected object.
It is suitable for baking animation and subsequent export to game-engine formats.

![result](https://user-images.githubusercontent.com/16438515/73591794-cc1aa600-44fb-11ea-833e-24666a684377.gif)

# How to use
## 1. Download and Install addon

Download [Vertex Rig Addon](https://github.com/probka/VertexRig/releases/download/v0.1/vertex_rig.zip).

In Blender go to menu 'Edit > Preferences', select 'Add-ons', press 'Install' button:

![i1_pressInstall](https://user-images.githubusercontent.com/16438515/73591786-cae97900-44fb-11ea-8805-40ecb1f0a906.png)

**Locate downloaded addon**

![i1_findAddon](https://user-images.githubusercontent.com/16438515/73591784-cae97900-44fb-11ea-9e60-7c29219061ba.png)

then press checkbox to activate. If everything fine it will appear in 'Properties/Object' panel

![i1_activate](https://user-images.githubusercontent.com/16438515/73591783-cae97900-44fb-11ea-8416-658fd76053cf.png)

## 2. Generate Armature

Prepare animation for the shape. Then press 'GENERATE RIG' button while Shape is selected.

![p2_pressButton](https://user-images.githubusercontent.com/16438515/73591788-cae97900-44fb-11ea-9884-665ac5fe5a17.png)

Panel shows vertex count for selected object.

- **Be careful: using it for hi poly meshes will take a lot of time. There is no progress bars to visualise the process.**

If any type of object than 'Mesh' is selected, you will get warning:

![error](https://user-images.githubusercontent.com/16438515/73592002-274d9800-44fe-11ea-844b-560dd3ebf869.png)

After addon finishes it's job, you will get a fresh armature with bones constrained to each vertex of the object.

![p3_ready](https://user-images.githubusercontent.com/16438515/73591793-cb820f80-44fb-11ea-8648-9bb38e8e72ff.png)

## 3. Baking Animation

For now you can bake animation to keyframes and get action for exporting or blending with other actions:

Select new armature, switch to 'Pose mode', go to menu 'Pose > Animation > Bake action':

![p3_bake](https://user-images.githubusercontent.com/16438515/73591790-cb820f80-44fb-11ea-8229-e99dafcba61d.png)

Check 'Visual Keying' box and press 'OK'. Wait some time.

![p3_bakeSettings](https://user-images.githubusercontent.com/16438515/73591791-cb820f80-44fb-11ea-9fbf-1dbb89546a59.png)

After a bit processing you will get your armature with keyframes:

![p3_enjoy](https://user-images.githubusercontent.com/16438515/73591792-cb820f80-44fb-11ea-8d02-a937b7bd26e6.png)


[]: https://github.com/probka/VertexRig/releases/download/v0.1/vertex_rig.zipVertex
