#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# In these exercises you will practice:
# * Creating plots with Python
# * Choosing appropriate plots for the question at hand
# * Tweaking plots to make clear the important features of the data
# * Adding comments that make the interpretation of plots clear

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


# ### Load and inspect data
# 
# We will use the Oxford weather station data. 
# In some of the exercises we will also use data from the Cambridge weather station.

# In[2]:


OxWeather = pd.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
OxWeather.head()


# In[3]:


CamWeather = pd.read_csv('../data/CambridgeWeather.csv')
CamWeather.head()


# **Note** that the dataframes don't match:
# * The column names are different in the Oxford and Cambridge datasets
# * Whilst the Oxford dataset has one entry (row) per day, the Cambridge dataset has only one entry per month
# * the range of years covered is different
# 
# These points will be relevant when you want to work with the data, especially when comparing between datasets

# ## Question 1
# 
# A couple are planning their wedding in Oxford. They would like to know which month has the most rain-free days. Produce a graph to help them.

# In[4]:


# Your code here
OxWeather['rainfree']=(OxWeather.Rainfall_mm<=0)
sns.barplot(data=OxWeather, x='MM', y='rainfree')


# Please add some comments here!

# # Question 2
# 
# Is Oxford getting warmer?!
# 
# Plot the mean temperature for each year in the dataset to find out.

# In[5]:


# your graph here
sns.lineplot(data=OxWeather, x='YYYY', y='Tmax')


# ## Question 3
# 
# Helen moved from Cambridge to Oxford. Sitting in the pub in the rain, she complained that it rains far more in Oxford than in Cambridge. Provide one or more graphs, and some suitable descriptive statistics, to support or contradict Helen's claim.

# In[6]:


# Your graph here
plt.subplot(1,2,1)
sns.barplot(data=OxWeather, y='Rainfall_mm', x='MM')
plt.ylim(0,2.2)
plt.subplot(1,2,2)
CamWeather['rainperday']=CamWeather.rain/31
sns.barplot(data=CamWeather, y='rainperday', x='mm')
plt.ylim(0,2.2)

plt.tight_layout()
plt.show()


# Please add some comments here!

# ## Question 3
# 
# In the Cambridge dataset, the column `af` gives the number of days (in a month) with *air frost*, ie a minimum temperature below $ 0^{\circ}C $
# 
# Is air frost more frequent in Cambridge than Oxford? Plot the average number of days with air frost in Oxford and Cambridge in each month of the year.

# Hint: first you will need to add a column to the <tt>OxWeather</tt> dataframe, containing a 1 for days with air frost and a 0 for days without. 
# 
# We will cover adding columns in more detail next week, so here is some code:

# In[7]:


OxWeather['af']=(OxWeather.Tmin<0)*31
OxWeather


# In[8]:


plt.subplot(1,2,1)
sns.barplot(data=CamWeather, y='af', x='mm')

plt.subplot(1,2,2)
sns.barplot(data=OxWeather.query('YYYY >= 2020'), y='af', x='MM')

plt.tight_layout()
plt.show()


# In[9]:


CamWeather.sort_values(by='af')


# In[ ]:




