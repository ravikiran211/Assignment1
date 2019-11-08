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


# In[ ]:




