import scipy.io as io
import matplotlib.pyplot as plt


data_ctd = io.loadmat('T4_p1.mat')

with open('018838_20240425_1127.hex', 'rb') as f:
    hexdata = f.read().hex()
    
    
print(hexdata)