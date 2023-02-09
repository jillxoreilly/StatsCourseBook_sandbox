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
sns.set_style('white')


# In[2]:


clouds=pandas.read_csv('data/cloudSeeding.csv')
clouds


# In[3]:


sns.kdeplot(data=clouds, x='rainfall', hue='status', shade=True)
sns.rugplot(data=clouds, x='rainfall', hue='status')
plt.show()


# In[4]:


plt.figure(figsize=(10, 2))
data=[177,164,177,178,169,170,172,171,190,174]
      #,163,170,172,159,174,162,158,168,173,17]
sns.kdeplot(data, color=[0,0,1], shade='True')


# In[5]:


plt.figure(figsize=(10, 2))
data=[163,170,172,159,174,162,158,168,173,174]
sns.kdeplot(data, color=[1,0,0], shade='True')


# In[6]:


sns.stripplot(data=clouds, x='rainfall', y='status')
plt.show()


# In[7]:


stats.mannwhitneyu(clouds[clouds['status']=='Seeded']['rainfall'],
                   clouds[clouds['status']=='Unseeded']['rainfall'],alternative='greater')


# In[8]:


stats.ttest_ind(clouds[clouds['status']=='Seeded']['rainfall'],
                clouds[clouds['status']=='Unseeded']['rainfall'],alternative='greater')


# In[9]:


def dMeans(a,y):
    return np.mean(x)-np.mean(y)
    
stats.permutation_test((clouds[clouds['status']=='Seeded']['rainfall'],
                       clouds[clouds['status']=='Unseeded']['rainfall']),
                       dMeans,
                       permutation_type='independent', alternative='greater')


# In[73]:


plt.figure(figsize=(12, 3))
x=range(-1000,4000)
y = stats.norm.pdf(x,clouds[clouds['status']=='Seeded']['rainfall'].mean(),clouds[clouds['status']=='Seeded']['rainfall'].std())
plt.plot(x,y,color=(1,0,0))
sns.kdeplot(data=clouds[clouds['status']=='Seeded'], x='rainfall', color=[1,0,0], shade=True)
sns.rugplot(data=clouds[clouds['status']=='Seeded'], x='rainfall', color=[1,0,0], height=0.1)


# In[70]:


plt.figure(figsize=(12, 3))
x=range(-1000,4000)
sns.kdeplot(data=clouds[clouds['status']=='Unseeded'], x='rainfall', color=[0,0,1], shade=True)
sns.rugplot(data=clouds[clouds['status']=='Unseeded'], x='rainfall', color=[0,0,1], height=0.1)
y = stats.norm.pdf(x,clouds[clouds['status']=='Unseeded']['rainfall'].mean(),clouds[clouds['status']=='Seeded']['rainfall'].std())
plt.plot(x,y,color=(0,0,1))


# In[ ]:


stats.mannwhitneyu(clouds[clouds['status']=='Seeded']['rainfall'],clouds[clouds['status']=='Unseeded']['rainfall'],alternative='greater')

