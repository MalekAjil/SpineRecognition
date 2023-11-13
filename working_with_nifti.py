import os
import numpy as np
import nibabel as nib
from nibabel.testing import data_path
import pandas as pd

n1_header = 0


def sform():
    print(n1_header['srow_x'])
    print(n1_header['srow_y'])
    print(n1_header['srow_z'])
    print(n1_header.get_sform())
    print(n1_header.get_sform(coded=True))
    print(n1_header['sform_code'])

    n1_header.set_sform(np.diag([2, 3, 4, 1]))
    print(n1_header.get_sform())

    n1_header.set_sform(np.diag([3, 4, 5, 1]), code='mni')
    print(n1_header.get_sform(coded=True))


def qform():
    print( n1_header.get_qform(coded=True))


def show_slices(slices):
    fig, axes = plt.subplot(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap='gray', origin='lower')


np.set_printoptions(precision=2, suppress=True)
ni1 = os.path.join(data_path, 'example4d.nii.gz')
print(ni1)
n1_img = nib.load(ni1)
n1_header = n1_img.header
# print(n1_header)
n1_header['cal_max'] = 1200

# sform()
# qform()
print(n1_header.get_base_affine())
print(n1_header.get_best_affine())

print('*************************')

array_data=np.arange(24,dtype=np.int16).reshape((2,3,4))
affine=np.diag([1,2,3,1])
array_img=nib.Nifti1Image(array_data,affine)
array_header=array_img.header
print(array_header['scl_slope'])
print(array_header['scl_inter'])
print(array_header.get_slope_inter())

array_header.set_slope_inter(2,10)
print(array_header.get_slope_inter())
print(array_header['scl_slope'])
print(array_header['scl_inter'])
print(array_img.get_fdata())

nib.save(array_img,'scaled_image.nii')
scaled_img=nib.load('scaled_image.nii')
print(scaled_img.get_fdata())
print(scaled_img.header.get_slope_inter())
print(scaled_img.dataobj.slope)
print(scaled_img.dataobj.inter)


data=np.random.random((20,20,20))
xform=np.eye(4)*2
img=nib.nifti1.Nifti1Image(data,xform)
print(img.get_sform(coded=True))
print(img.get_qform(coded=True))


ni2 = os.path.join(data_path, 'example_nifti2.nii.gz')
print(ni2)
n2_img = nib.load(ni2)
n2_header = n2_img.header
print(n2_header)


data = nib.load('2804506.nii.gz')
    # data.get_fdata()
    # data=data.get_fdata()
    # data.shape
    plt.plot(np.mean(data, axis=(0, 1, 2)))
    plt.show()
    slice_0 = data[:, :, 0]
    slice_1 = data[:, :, 1]
    slice_2 = data[:, :, 2]
    slice_3 = data[:, :, 3]
    show_slices([slice_0, slice_1, slice_2, slice_3])
    plt.subtitle("Center slices for EPI image")


    df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
    '''
    np.set_printoptions(precision=2, suppress=True)
    ni1 = os.path.join(data_path, 'example4d.nii.gz')
    print(ni1)
    n1_img = nib.load(ni1)
    n1_header = n1_img.header
    print(n1_header)
    n1_header['cal_max'] = 1200
    '''

