# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:57:04 2018

@author: 58497_000
"""



def v_W(i, D_W, M=64, n=2, F=96485, row=8.9, pi= 3.1416):
   v_w = (4*i*M)/(n*F*row*pi*D_W*D_W)
   return v_w

if __name__ == "__main__":
    i = 1.7
    D_W= 0.5
    v_w = v_W(i, D_W)
    print(1000*v_w) # 单位nm/s