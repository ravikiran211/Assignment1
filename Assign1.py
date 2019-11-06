#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.

lis1=[]

for a in range(2000,3200):
    if (a%7==0) & (a%5 !=0):
        lis1.append(a)
print(lis1)


# In[2]:


#3.
#Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name.

first_name=input('Enter your first name ')
last_name=input('Enter your last name ')
print(last_name," ",first_name)


# In[3]:


#4.
#Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r**3
import math
r=2*12
v=(4*math.pi*(r**3))/3
print(v)


# In[5]:


#Task 2:
#1.
#Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.

a=list(input("Please enter comma-separated numbers").split(','))

print(a)



# In[12]:


#2.
#Create the below pattern using nested for loop in Python.
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *
#    * * * *
#    * * *
#    * *
#    *

for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()
for k in range(4,0,-1):
    for l in range(k):
        print('*',end='')
    print()
            


# In[14]:


#   3.
#  Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:
#Input word: AcadGild
#Output: dilGdacA

inpStr=input()
print(inpStr[::-1])


# In[22]:


#   4.
#   Write a Python Program to print the given string in the format specified in the sample output.
#   WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
#   SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
#   its citizens
#   Sample Output:
#   WE, THE PEOPLE OF INDIA,
#   having solemnly resolved to constitute India into a SOVEREIGN, !
#   SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#   and to secure to all its citizens

print('WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, !\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t',' ',"and to secure to all its citizens")


# In[ ]:




