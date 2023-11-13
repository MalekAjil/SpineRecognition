import numpy as np
import os
import sys
import nibabel as nib
import tkinter as tk
from tkinter import filedialog

from matplotlib import pyplot as plt

from lml import read_lml


def load_dataset():
    """to load nii files from multiple folders inside specified folder"""
    img_dataset = []
    lml_dataset = []
    root = tk.Tk()
    root.withdraw()
    try:
        input_folder = filedialog.askdirectory()
        if input_folder == '':
            raise FileExistsError
        print(input_folder)
        for folder in os.listdir(input_folder):
            path1 = os.path.join(input_folder, folder)
            for x in os.listdir(path1):
                path2 = os.path.join(path1, x)
                for y in os.listdir(path2):
                    path3 = os.path.join(path2, y)
                    if y.endswith('.nii.gz'):
                        # print('nii file is $ ' + path3)
                        img = nib.load(path3).get_fdata()
                        if img is not None:
                            img_dataset.append(img)
                    elif y.endswith('.lml'):
                        # print('LML file is % ', path3)
                        lml_data = read_lml(path3)
                        if lml_data is not None:
                            lml_dataset.append(lml_data)

    except Exception as e:
        print(e)
        sys.exit(2)
    finally:
        return img_dataset, lml_dataset


def load_dataset2():
    """to load nii files directly from one specified folder"""
    img_dataset = []
    root = tk.Tk()
    root.withdraw()
    try:
        input_folder = filedialog.askdirectory()
        if input_folder == '':
            raise FileExistsError
        print(input_folder)
        for file in os.listdir(input_folder):
            path1 = os.path.join(input_folder, file)
            if file.endswith('.nii.gz'):
                # print('nii file is $ ' + path1)
                img = nib.load(path1).get_fdata()
                if img is not None:
                    img_dataset.append(img)

    except Exception as e:
        print(e)
        sys.exit(2)
    finally:
        return img_dataset


# niidata, lmldata = load_dataset()
# print(len(niidata))
# print(len(lmldata))
# for lml in lmldata[16]:
#     print(str(lml.id) + '\t' + lml.name + '\t' + str(lml.pos) + '\n')

# niidata = load_dataset2()
# print(len(niidata))


def correct_range(imm):
    # print(imm.shape)
    mx = np.max(imm)
    mn = np.min(imm)

    imm = imm[:, :] - mn
    rng = (255 / (mx - mn))

    img = list(map(lambda x: np.round(x * rng), imm))

    # imshow(img)
    # montage({imm,im1,img,im2,im3})
    return img


def show_slices(slices):
    """Function to display row of image slices """
    columns = 4
    rows = 1
    if int(slices.shape[2] // 4) > 1:
        rows = int(slices.shape[2] % 4)
    fig = plt.figure()
    slc = 1
    for i in range(slices.shape[2]):
        fig.add_subplot(rows, columns, slc)
        plt.imshow(slices[:, :, i], cmap='gray', origin='lower')
        plt.axis('off')
        plt.title(str(slc))
        slc += 1

    plt.show()

def show_slices2(slices, titles):
    """Function to display row of image slices """
    columns = 4
    rows = 1
    if int(slices.shape[0] // 4) > 1:
        rows = int(slices.shape[0] % 4)
    fig = plt.figure()
    slc = 1
    for i in range(slices.shape[0]):
        fig.add_subplot(rows, columns, slc)
        plt.imshow(slices[i, :, :], cmap='gray', origin='lower')
        plt.axis('off')
        plt.title(titles[i])
        slc += 1

    plt.show()
