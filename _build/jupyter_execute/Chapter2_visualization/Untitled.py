#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import seaborn as sns
sns.set_theme(style='white')
import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[2]:


raw=pd.read_csv('../data/bsa2017_env_mod.csv')
raw


# In[3]:


raw.replace({'Sex':{1: 'M', 2:'F'}, }, inplace=True)
raw.replace({'Married':{1: 'Married/Living with partner', 2:'Divorced', 3:'Widowed', 4:'Never Married', 9:'Missing'}}, inplace=True)
raw.replace({'Children':{1:1, 2:0}, }, inplace=True)
raw.replace({'Education':{1:'Degree', 2:'ALevel', 3:'GCSE', 4:'None'}} , inplace=True)
raw


# In[4]:


raw.replace({'Age':{999:np.nan}} , inplace=True)
sns.kdeplot(data=raw,x='Age',hue='Married')
plt.show()


# In[5]:


sns.histplot(data=raw, x='Age', y='libauth', bins=10)
plt.ylim(1,5)


# In[6]:


sns.histplot(data=raw, x='Age', y='leftrigh', bins=10)


# In[7]:


sns.kdeplot(data=raw, x='leftrigh', hue='PartyId2', common_norm=False)


# In[ ]:




