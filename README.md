# Rigging Scripts

### Mesh To Bone Shape
Transfer a mesh object's shape to the active bone in Pose Mode. Automatically creates a `WGT_` object instance.

![Mesh To Bone Shape selection](https://raw.githubusercontent.com/LesFeesSpeciales/blender-scripts-docs/master/shape_to_bone.png "Mesh To Bone Shape selection")  
To apply a shape, select a mesh object, then the armature. In *Pose Mode*, select the bone you wish to apply the shape to. The mesh shape will be transferred to the bone in its current position.

### Tesselation
Automatically tesselate an image plane for later skinning.  
This add-on requires [scipy](https://www.scipy.org/) and [skimage](http://scikit-image.org/), as well as [triangle](http://dzhelil.info/triangle/), available from the [pypi](https://pypi.python.org/pypi/triangle/). This library needs to be compiled against the same Python version as Blender. In Linux this may involve compiling Python, and a virtual environment. An article explaining the precess is available [here](http://lacuisine.tech/2017/10/20/how-to-install-python-libs-in-blender-part-2/), but feel free to contact us for assistance!

![Tesselation before](https://raw.githubusercontent.com/LesFeesSpeciales/blender-scripts-docs/master/tesselation_before.png "Tesselation before") ![Tesselation after](https://raw.githubusercontent.com/LesFeesSpeciales/blender-scripts-docs/master/tesselation_after.png "Tesselation after")  

-----

# License

Blender scripts shared by **Les Fées Spéciales** are, except where otherwise noted, licensed under the GPLv2 license.
