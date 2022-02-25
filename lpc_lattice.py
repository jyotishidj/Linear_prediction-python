# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:50:38 2018

@author: Debasish Jyotishi
"""

import numpy as np

def lpc_lattice(signal,p):
    
    f1=signal
    f=np.zeros(signal.size)
    g1=signal
    g=np.zeros(signal.size)
    k=np.zeros(p)
    k[0]=np.array(-2*np.sum(np.multiply(f1[1:],g1[:((g1.size)-1)]))/(np.sum(np.power(f1,2))+np.sum(np.power(g1[:((g1.size)-1)],2))))
    
    for i in range(1,p):
        f=f1+k[i-1]*(np.r_[0,g1[:((g1.size)-1)]])
        g=k[i-1]*f1+(np.r_[0,g1[:((g1.size)-1)]])
        k[i]=np.array(-2*np.sum(np.multiply(f[1:],g[:((g.size)-1)]))/(np.sum(np.power(f,2))+np.sum(np.power(g[:((g.size)-1)],2))))
        del f1,g1
        f1=f
        g1=g
        del f,g
        
    a=np.array([k[0]])
        
    for i in range(1,p):
        a1=np.zeros(i+1)
        for j in range(0,i+1):
            if j==i:
                a1[j]=k[j]
            else:
                a1[j]=a[j]+k[i]*a[i-1-j]
        del a
        a=a1
        
    return(np.r_[1,a])