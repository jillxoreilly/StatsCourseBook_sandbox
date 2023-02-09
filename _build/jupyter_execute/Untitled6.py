#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns

data= pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/BrotherSisterData.csv')


# In[2]:


data.mean()
data


# In[3]:


data['diff']=(data.brother-data.sister)
data


# In[4]:


my_pal_1 = {"brother": [0.9,0.9,1], "sister": [1,0.9,0.9], "diff": [0.5,0.5,0.5]}
my_pal_2 = {"brother": [0.5,0.5,1], "sister": [1,0.5,0.5], "diff": [0.1,0.1,0.1]}

sns.violinplot(data=data, palette=my_pal_1, alpha=0.2)
sns.swarmplot(data=data, palette=my_pal_2)

plt.plot([-0.4,0.4],[data['brother'].mean(),data['brother'].mean()], 'b')
plt.plot([0.6,1.4],[data['sister'].mean(),data['sister'].mean()], 'r')
plt.ylim([140,200])

plt.ylabel='height'


# In[5]:


my_pal_1 = {"brother": [0.9,0.9,1], "sister": [1,0.9,0.9], "diff": [0.5,0.5,0.5]}
my_pal_2 = {"brother": [0.5,0.5,1], "sister": [1,0.5,0.5], "diff": [0.1,0.1,0.1]}

sns.violinplot(data=data, palette=my_pal_1, alpha=0.2)
sns.swarmplot(data=data, palette=my_pal_2)

plt.plot([1.5,2.5],[0,0], 'k')
plt.ylim([-30,30])

plt.ylabel='height'


# In[6]:


my_pal_1 = {"brother": [0.9,0.9,1], "sister": [1,0.9,0.9]}
my_pal_2 = {"brother": [0.5,0.5,1], "sister": [1,0.5,0.5]}

sns.violinplot(data=data, palette=my_pal_1, alpha=0.2)
sns.swarmplot(data=data, palette=my_pal_2)


sns.violinplot(data=data.brother-data.sister, color=[0.5,0.5,0.5])
sns.swarmplot(data=data.brother-data.sister, color=[0.1,0.1,0.1])

plt.ylabel='height'

