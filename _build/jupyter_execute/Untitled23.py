#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# In[2]:


import random
random.choice('0123456789abcdef')


# In[3]:


import string
import random

UKBrexdex=pandas.read_csv('data/nonNormalData2.txt')


for i in range(len(UKBrexdex)):
    lst = [random.choice(string.ascii_letters + string.digits) for n in range(8)]
    s = "".join(lst)
    codes[i] = s


# In[ ]:




