# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:01:40 2018

@author: 58497_000
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def H_M(D_W, D_N=0.7,fi=0.0667):
	D_tmp = D_N/(D_W*np.cos(fi))
	H_M = -0.5*D_W*np.cos(fi)*(cosh_1(D_tmp)-cosh_1(1/np.cos(fi)))
	return H_M

def Z(r, D_W , D_N= 0.7, fi= 0.0667):
    D_tmp = D_N/(D_W*np.cos(fi))
    r_tmp = 2*r/(D_W*np.cos(fi))
    Z_r = 0.5*D_W*np.cos(fi)*(cosh_1(D_tmp)-cosh_1(r_tmp))
    return Z_r
def cosh_1(f):
    fi = 1/(np.cosh(f))
    return fi
D_w = 0.63
list= []
for i in range(0,800):
	i0= i/1000
	#print(H_M(i0))
	list.append(Z(i0, D_w))
with open('Z_r.txt','w')  as f:
	for num in list:
		f.write(str(num)+'\n')
	f.close()
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

r = np.linspace(-0.4, 0.4, 800)



H = -H_M(D_w)
print(H)
x = np.linspace(-0.4, 0.4,100)
y = np.linspace(H, H, 100)
Z_r = Z(r, D_w)

plt.figure('Z_r')
plt.plot(x,y)
plt.plot(r, Z_r)

plt.savefig('Z_r.png')
plt.show()