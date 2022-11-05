'''
v1. This program will count dcm files recurisevly from select directory grab the first file and output dicom tag
'''

import os
import pydicom

src = "c:\dicominput"
dst = "c:\dicomoutput"

print('reading file list...')
filelist = []
for root, dirs, files in os.walk(src):
    for file in files:
        if ".dcm" in file:  # exclude non-dicoms, good for messy folders
            filelist.append(os.path.join(root, file))


print('%s files found.' % len(filelist))

primaryfile=filelist[0]

from pydicom import dcmread
print(primaryfile)
ds = dcmread(primaryfile)

#print(ds)
seq = ds[0x0010, 0x0010]
print(seq)
#print(ds.file_meta)