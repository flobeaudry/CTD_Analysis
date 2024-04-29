import scipy.io as io
import matplotlib.pyplot as plt


data_ctd = io.loadmat('018838_20240425_1127.mat')

with open('data.geno', 'rb') as f:
    hexdata = f.read().hex()
    
    
print(data_ctd.temperature)