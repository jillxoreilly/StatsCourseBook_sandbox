#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_style('darkgrid')


# In[2]:


happiness=pandas.read_csv('data/happiness10.csv')
happiness


# In[3]:


sns.scatterplot(data=happiness, x='GDPpc (in $ 000)', y='LifeSat')

# Loop through the data points 
for i in range(len(happiness)):
    plt.text(happiness['GDPpc (in $ 000)'][i]+0.2, happiness['LifeSat'][i]+0.05, happiness['Country'][i])

plt.xlim([0,140])
plt.ylim([5,8])


# In[21]:


sns.regplot(data=happiness, x='GDPpc (in $ 000)', y='LifeSat', ci=None)

# Loop through the data points 
for i in range(len(happiness)):
    plt.text(happiness['GDPpc (in $ 000)'][i]+0.2, happiness['LifeSat'][i]+0.05, happiness['Country'][i])

plt.xlim([0,140])
plt.ylim([0,8])


# In[22]:


happiness_res=pandas.read_csv('data/happiness10_res.csv')
happiness_res


# In[ ]:




