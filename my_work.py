import numpy as np
import cv2
import nibabel as nib
import matplotlib.pyplot as plt
import sys
import tkinter as tk
from tkinter import filedialog

from lml import read_lml
from auxiliary_functions import correct_range, load_dataset, show_slices, show_slices2


def my_work():
    input_file = ''
    lml_file = ''
    root = tk.Tk()
    root.withdraw()
    try:
        input_file = filedialog.askopenfilename()
        if input_file == '':
            raise FileExistsError
        lml_file = input_file[:-6] + "lml"
        if lml_file == '':
            print('there is no lml file associated with image file..!')
            sys.exit(1)
        print('Input file is ', input_file)
        print('LML file is ', lml_file)

        image_array = nib.load(input_file).get_fdata()

        nx, ny, nz = image_array.shape
        print('nx= ' + str(nx) + " , ny= " + str(ny) + ' , nz= ' + str(nz))

        lml_data = read_lml(lml_file)
        for x in lml_data:
            print(str(x.id) + '\t' + x.name + '\t' + str(x.pos) + '\n')

        img = correct_range(image_array[:, :, 0])

        imf = np.copy(img)
        # cv2.edgePreservingFilter(image_array[:, :, 0], imf, 1, 1, 1)
        # imf[:, :] = image_array[:, :, 0] > 200

        print('max = ' + str(np.max(image_array[:, :, 0])) +
              ' Min = ' + str(np.min(image_array[:, :, 0])) +
              ' mean = ' + str(np.mean(image_array[:, :, 0])) +
              ' median = ' + str(np.median(image_array[:, :, 0])) +
              ' std = ' + str(np.std(image_array[:, :, 0])))
        print('max = ' + str(np.max(img)) + ' Min = ' + str(np.min(img)) +
              ' mean = ' + str(np.mean(img)) +
              ' median = ' + str(np.median(img)) +
              ' std = ' + str(np.std(img)))
        print('max = ' + str(np.max(imf)) + ' Min = ' + str(np.min(imf)) +
              ' mean = ' + str(np.mean(imf)) +
              ' median = ' + str(np.median(imf)) +
              ' std = ' + str(np.std(imf)))

        slices = list()
        slices.append(image_array[:, :, 0])
        slices.append(img)
        slices.append(imf)
        slices = np.asarray(slices)
        show_slices2(slices, ['original', 'corrected', 'filtered'])


    except Exception as e:
        print(e)
        sys.exit(2)

# my_work()
