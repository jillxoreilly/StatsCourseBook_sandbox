#!/usr/bin/env python
# coding: utf-8

# # Python skills check
# 
# Here we will recap the main bibts of Python you encountered this week
# 
# 
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
sns.set_theme() # use pretty defaults


# ### Exercises

# In[2]:


# 1. Draw a random sample from a binomial distriubtion with n=27 and p=0.4
k = # your code here
print('k = ' + str(k))


# In[25]:


# 2. For a binomial distribution k~B(100,0.8), find the probability that k<=70


# The answer should be 0.0112

# In[26]:


# 3. For a normal distribution x~N(80,4) find the probability that x<=70.5


# The answer should be 0.00877

# In[ ]:


# 4a. Make a for loop to draw 150 random samples from the distribution k~B(12,0.3) 

# 4b. Plot the values of k on a histogram

