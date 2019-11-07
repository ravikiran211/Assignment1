#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.1
#Write a Python Program to implement your own myreduce() function which works exactly like
#Python's built-in function reduce()
lis=[1,3,5,6]
def myreduce(lamdaaddition,lis):
    for a in range(lis):
        summ+=a
    


# In[6]:


#Write a Python program to implement your own myfilter() function which works exactly like
#Python's built-in function filter()
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False    
fun('a')


# In[36]:


lis1=list("ACADGILD")
lis1
lis2=[i*j for i in ['x','y','z'] for j in range(1,5)]
lis2
lis3=[i*j for i in range(1,5) for j in ['x','y','z']]
lis3
lis4=[[j] for i in range(3) for j in range(i+2,i+5)]
lis4
lis5=[[j for j in range(i+2,i+6)] for i in range(4)]
lis5
lis6=[(j,i) for i in range(1,4) for j in range(1,4)]
lis6


# In[41]:


def longestWord(alist):
    maximum=0
    longword=''
    for word in alist:
        if len(word)>maximum:
            maximum=len(word)
            longword=word
    return longword
words=['hello','hi','bye']
longestWord(words)


# In[ ]:




