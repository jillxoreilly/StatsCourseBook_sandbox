#!/usr/bin/env python
# coding: utf-8

# # The <tt>while</tt> loop
# 
# Here we meet the <tt>while</tt> loop, which is another way of getting the computer to repeat the same calculationa a lot of times.
# 
# The difference between a <tt>for</tt> loop and a <tt>while</tt> loop is as follows:
# <ul>
#    <li> In the <tt>for</tt> loop, the commands inside the loop are repeated a predetermined number of times - once for each value of a variable in an input list
#    <li> In the <tt>while</tt> loop, the commands inside the loop are repeated until some condition is met, no matter how many repeats are needed to reach that condition
# </ul>

# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# ## Example: Fibonacci Sequence
# 
# The Fibonacci Sequence is a sequence of numbers that begins [0,1,...] and continues by adding together the two previous numbers such that $$ x_i = x_{i-1} + x_{i-2} $$
# 
# The sequence begins [0, 1, 1, 2, 3, 5, 8, 13..... ] and goes on forever.
# 
# Here is a <tt>for</tt> loop to calculate the first 10 elements of the Fibonacci sequence 

# In[2]:


n = 10 # number of elements to calculate
fibonaccis = np.empty(n) 

# get the sequence started
fibonaccis[0] = 0
fibonaccis[1] = 1

for i in range(2,n): # start in place 2 as we already set the first two elements of the sequence (places 0 and 1)
    fibonaccis[i] = fibonaccis[i-1] + fibonaccis[i-2]# your code here to calculate the ith Fibonacci number
    
plt.plot(fibonaccis,'.-')
plt.xlabel('$i$')
plt.ylabel('$x_i$')


# Say we instead want to find all Fibonacci numbers less than 1000.
# 
# We can do it using a <tt>while</tt> loop. Let's get ready:

# In[3]:


fibonaccis = np.array([]) # this time we create an empty array to store our Fibonacci numbers

# each new number will be appended to the array (as we don't know how long the array will ultimately be)
fibonaccis = np.append(fibonaccis,[0])
fibonaccis = np.append(fibonaccis,[1])

fibonaccis


# The condition for stopping our while loop is that the last number in the sequence is greater than 1000.
# 
# To check the value of the last number in a <tt>numpy</tt> array, we use the syntax [-1]

# In[4]:


anyoldnumbers = [3,5,2,1,6,9]
anyoldnumbers[-1]


# In[5]:


fibonaccis = np.array([]) # this time we create an empty array to store our Fibonacci numbers

# each new number will be appended to the array (as we don't know how long the array will ultimately be)
fibonaccis = np.append(fibonaccis,[0])
fibonaccis = np.append(fibonaccis,[1])

i=2 # start in place 2 as we already set the first two elements of the sequence (places 0 and 1)
while fibonaccis[-1] < 1000:
        new_fibonacci = fibonaccis[i-1] + fibonaccis[i-2]# your code here to calculate the ith Fibonacci number
        fibonaccis = np.append(fibonaccis, new_fibonacci)
        i=i+1
fibonaccis       


# In[ ]:




