#!/usr/bin/env python
# coding: utf-8

# # Predator-Prey simulation

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


# In[2]:


n = 50000
rPop = np.empty(n+1)
fPop = np.empty(n+1)
time = np.empty(n+1)
rPop[0]=1
fPop[0]=0.5
time[0]=0

a = 0.4 # rabbit fertility rate
b = 0.4 # chance of any given rabbit being eaten by any given fox
c = 0.3 # fox death rate (if there were no rabbits to eat)
e = 0.3 # increase in chance of fox surviving if it eats a rabbit

rPop[0]=(c/e)+0.2
fPop[0]=(a/b)-0.1
tStep = 0.001

for t in range(1,n+1):
    
    r = rPop[t-1]
    f = fPop[t-1]
    
    r = r + (a*r - b*r*f)*tStep
    f = f + (-c*f + e*r*f)*tStep
    
    rPop[t]=r
    fPop[t]=f
    time[t]=time[t-1]+tStep

plt.plot(time,fPop*100,'r')
plt.plot(time,rPop*100,'b')

plt.ylabel('population as % of long term average')
plt.xlabel('time (weeks)')


# In[3]:


len(np.arange(1, days+1, tStep))


# In[ ]:




