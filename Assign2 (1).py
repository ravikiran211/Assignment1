#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1.1
#Write a Python Program to implement your own myreduce() function which works exactly like
#Python's built-in function reduce()

    


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


#list comprehensions
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


#longestWord
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


# In[5]:


#Area of triangle
class parent:
    def sides():
        a=int(input("Enter length of side 1 "))
        b=int(input("Enter length of side 2 "))
        c=int(input("Enter length of side 3 "))
        return [a,b,c]
class child (parent):
    def area():
        lis1=parent.sides()
        p=sum(lis1)/2
        areaof=(p*(p-lis1[0])*(p-lis1[1])*(p-lis1[2]))**0.5
        return areaof

child.area()
        


# In[9]:


#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n. 
def filter_long_words(lis,n):
    lis1=[a for a in lis if len(a)>n]
    return lis1
filter_long_words(['HarryPotter','Snape','Ron','Voldemort','hermoine'],5)


# In[10]:


#list of words into a list of integers

def words_to_integers(wordslist):
    intlist=[len(a) for a in wordslist]
    return intlist

wordslist=['hey','hi','bye','thanks']
words_to_integers(wordslist)


# In[13]:


#Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise
vowels=['a','e','i','o','u','A','E','I','O','U']

def isvowel(character):
    if (len(character)==1) & (character in vowels):
        return True
    else:
        return False

isvowel('I')


# In[ ]:




