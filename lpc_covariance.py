# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:11:43 2018

@author: Debasish Jyotishi
"""

import numpy as np

def lpc_covariance(signal,p):
    
    n=signal.size
    R=np.zeros([p,p])
    
    for i in range(0,p):
        for j in range(0,p):
            inter=sum(np.multiply(signal[(p-i-1):(n-1-i)],signal[(p-j-1):(n-1-j)]))
            R[i,j]=inter
            del inter
    
    shi=np.zeros(p)        
    for i in range(0,p):
        shi[i]=sum(np.multiply(signal[(p-i-1):(n-1-i)],signal[p:]))
            
    
    a=np.matmul(np.linalg.inv(R),shi)
        
    return(np.r_[1,-a])
        