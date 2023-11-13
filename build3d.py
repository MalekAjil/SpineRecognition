import bpython as bpy
import os
import pydicom
import numpy as np

path = "./Desktop/EMC/"

files = sorted(os.listdir(path + "/Data/Head/"))

data = np.zeros((245, 512, 512))

for i in range(len(files)):
    layer = pydicom.dcmread(path + "/Data/Head/" + files[i]) # read dcm files

    data[i] = layer.pixel_array

for yy in range(245):
    for xx in range(512):
        for zz in range(512):
            print("X: {}, Y: {}, Z: {}".format(xx, yy, zz))

            c = data[yy, xx, zz]



            bpy.ops.mesh.primitive_cube_add(location=(xx / 500, zz / 500, yy / 500))
            bpy.ops.transform.resize(value=(0.001, 0.001, 0.001))

            activeObject = bpy.context.active_object # Select active object
            mat = bpy.data.materials.new(name="MaterialName")
            activeObject.data.materials.append(mat) #Add Material

            bpy.context.object.active_material.diffuse_color = (c, c, c) #change color

            if zz == 511:        #Join objects and remove doubles
                item='MESH'
                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_by_type(type=item)
                bpy.ops.object.join()

                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.remove_doubles()
                bpy.ops.object.mode_set(mode='OBJECT')

print("DONE")