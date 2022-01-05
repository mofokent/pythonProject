import os
import pydicom
'''
print("file list c:\dicom")
arr = os.listdir("c:\dicom")
print(arr)
'''

#playing with single dicom file list patient name123

fpath = ("c:\dicomtst\CT_small.dcm")
from pydicom import dcmread
print(fpath)
ds = dcmread(fpath)
#print(ds)
seq = ds[0x0010, 0x0010]
print(seq)
elem = ds[0x0010, 0x0010]
elem.value ='Otto^Matt'
print (elem)
ds.save_as("c:\dicomtst\CT_small.dcm")
''''
# read dicomdir and provide output
from pydicom import dcmread
from pydicom.fileset import FileSet
path = ("c:\dicom\DICOMDIR")
ds = dcmread(path)
fs = FileSet(ds)
print(fs)
'''