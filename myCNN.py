import os
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import nibabel as nib

from scipy import ndimage

import random

from scipy import ndimage

import matplotlib.pyplot as plt


def read_nifti_file(filepath):
    """Read and load volume"""
    # Read file
    scan = nib.load(filepath)
    # Get raw data
    scan = scan.get_fdata()

    return scan


def normalize(volume):
    """Normalize the volume"""
    min = 0
    max = 1000
    volume[volume < min] = min
    volume[volume > max] = max
    volume = (volume - min) / (max - min)
    volume = volume.astype("float32")
    return volume


def resize_volume(img):
    """Resize across z-axis"""
    # Set the desired depth
    desired_depth = 13
    desired_width = 128
    desired_height = 128
    # Get current depth
    current_depth = img.shape[-1]
    current_width = img.shape[0]
    current_height = img.shape[1]
    # Compute depth factor
    depth = current_depth / desired_depth
    width = current_width / desired_width
    height = current_height / desired_height
    depth_factor = 1 / depth
    width_factor = 1 / width
    height_factor = 1 / height
    # Rotate
    # img = ndimage.rotate(img, 90, reshape=False)
    # Resize across z-axis
    img = ndimage.zoom(img, (width_factor, height_factor, depth_factor), order=1)
    return img


def process_scan(path):
    """Read and resize volume"""
    # Read scan
    volume = read_nifti_file(path)
    # Normalize
    volume = normalize(volume)
    # Resize width, height and depth
    volume = resize_volume(volume)
    return volume


path1 = 'C:\\Users\\MK\\Documents\\AI_Master\\Dataset\\spine_1_2_3_nii'
path2 = 'C:\\Users\\MK\\Documents\\AI_Master\\Dataset\\spine_1_2_3_nii_'

normal_scan_paths = [
    os.path.join(os.getcwd(), path1, x)
    for x in os.listdir(path1)
]

abnormal_scan_paths = [
    os.path.join(os.getcwd(), path2, x)
    for x in os.listdir(path2)
]

print("os.getcwd() = ",os.getcwd())
# print(abnormal_scan_paths)

print("CT scans of normal Vertebrae: " + str(len(normal_scan_paths)))
print("CT scans of abnormal Vertebrae with pidecles: " + str(len(abnormal_scan_paths)))

# Build train and validation datasets
# Read the scans from the class directories and assign labels. Down sample the scans to have shape of 128x128x64.
# Rescale the raw HU values to the range 0 to 1. Lastly, split the dataset into train and validation subsets.
# Read and process the scans.
# Each scan is resized across height, width, and depth and rescaled.
abnormal_scans = np.array([process_scan(path) for path in abnormal_scan_paths])
normal_scans = np.array([process_scan(path) for path in normal_scan_paths])

print("scan processed")

abnormal_labels = np.array([1 for _ in range(len(abnormal_scans))])
normal_labels = np.array([0 for _ in range(len(normal_scans))])

# Split data in the ratio 70-30 for training and validation.
x_train = np.concatenate(
    (abnormal_scans[:(0.7 * abnormal_scans.shape[0])], normal_scans[:(0.7 * normal_scans.shape[0])]), axis=0)
y_train = np.concatenate(
    (abnormal_labels[:(0.7 * abnormal_scans.shape[0])], normal_labels[:(0.7 * normal_scans.shape[0])]), axis=0)
x_val = np.concatenate(
    (abnormal_scans[(0.7 * abnormal_scans.shape[0]):], normal_scans[(0.7 * normal_scans.shape[0]):]), axis=0)
y_val = np.concatenate(
    (abnormal_labels[(0.7 * abnormal_scans.shape[0]):], normal_labels[(0.7 * normal_scans.shape[0]):]), axis=0)
print(
    "Number of samples in train and validation are %d and %d."
    % (x_train.shape[0], x_val.shape[0])
)

# Create the model
model = Sequential()
model.add(
    Conv3D(32, kernel_size=(3, 3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=sample_shape))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(Conv3D(64, kernel_size=(3, 3, 3), activation='relu', kernel_initializer='he_uniform'))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(no_classes, activation='softmax'))

