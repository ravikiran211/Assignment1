#!/usr/bin/env python
# coding: utf-8

# In[16]:


def divisionbyzero():
    try:
        a=5/0
    except Exception as e:
        print(e)
divisionbyzero()


# In[10]:


subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

lis=[a+" "+b+" "+c for a in subjects for b in verbs for c in objects]
for a in lis:
    print(a)


# In[20]:


#Write a function so that the columns of the output matrix are powers of the input vector.The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1

import numpy as np
x=np.array([10,20,30,40,50])
#N=3
np.vander(x,increasing=False) #x**N-1,x**N-2,x**N-3


# In[25]:


#increasing=true
x=np.array([10,20,30,50])
n=3
np.vander(x,n,increasing=True) #increasing from left to right


# In[ ]:




