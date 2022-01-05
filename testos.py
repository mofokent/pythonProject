import os
import pydicom
'''
print("file list c:\dicom")
arr = os.listdir("c:\dicom")
print(arr)
'''

#playing with single dicom file
'''
#from pydicom.data import get_testdata_file
#fpath = get_testdata_file("CT_small.dcm")
fpath = ("c:\dicom\CT_small.dcm")
from pydicom import dcmread
print(fpath)
ds = dcmread(fpath)
#print(ds)
seq = ds[0x0010, 0x1002]
print(seq)
'''
from pydicom import dcmread
from pydicom.fileset import FileSet
path = ("c:\dicom\DICOMDIR")
ds = dcmread(path)
fs = FileSet(ds)
print(fs)
