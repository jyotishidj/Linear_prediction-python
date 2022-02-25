# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:19:36 2018

@author: Debasish Jyotishi
"""

import numpy as np

def lpc_autocorrelation(signal,p):
    
    n=signal.size
    R=np.correlate(signal,signal,'full')
    k=R[n]/R[n-1]
    a=np.array([-k])
    k=(R[n+1]+a*R[n])/(R[n-1]+a*R[n])
    
    for i in range(1,p):
        
        a1=np.zeros(i+1)
        a1[i]=-k
        for j in range(0,i):
            a1[j]=a[j]-k*a[i-1-j]
        del a
        a=a1
        k=(R[n+i+1]+np.sum(np.multiply(a,R[(n+i):(n-1):-1])))/(R[n-1]+np.sum(np.multiply(a,R[n:(n+i+1)])))
        del a1
        
    return(np.r_[1,a])
        