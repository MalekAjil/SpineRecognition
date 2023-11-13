import os
import fnmatch


path1 = 'C:\\Users\\MK\\Documents\\AI_Master\\Dataset\\Vertebrae_nii'
vertebrae_scan_paths = []
vertebrae_labels = []

for path, dirs, files in os.walk(path1):
    for file in files:
        if fnmatch.fnmatch(file, '*.nii'):
            fullname = os.path.join(path, file)
            # print(fullname)
            vertebrae_scan_paths.append(fullname)

