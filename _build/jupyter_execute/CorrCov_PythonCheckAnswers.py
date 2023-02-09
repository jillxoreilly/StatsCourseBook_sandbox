#!/usr/bin/env python
# coding: utf-8

# # Python skills check
# 
# You should work through this before the tutorial. The idea is for you to find the relevant code snippets int he worked examples you have just read, and modify them to work for your requirements here
# 
# ## Oxford weather station data
# 
# We will work with historical data from the Oxford weather station
# 
# <img src= "https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/images/OxfordSnow.jpg" width="50%"  />

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


# ### Load and inspect the data
# 
# Let's load some historical data about the weather in Oxford, from the file "OxfordWeather.csv"

# In[2]:


weather = pandas.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
display(weather)


# ### Correlation and covariance
# 
# Create a plot to show the relationship between mean temp (Tmean) and rainfall

# In[3]:


sns.scatterplot(data=weather, x='Tmean', y='Rainfall_mm')


# If I want to measure the correlation between Tmean and rainfall, which method should I use?
# 
# Using the appropriate method, obtain the full correlation matrix for the <tt>weather</tt> dataframe

# In[4]:


weather.corr(method = 'spearman')


# ... and just the correlation between Tmean and rainfall

# In[5]:


weather['Tmean'].corr(weather['Rainfall_mm'], method = 'spearman')


# Obtain the covariance between Tmin and Tmax

# In[6]:


weather['Tmax'].cov(weather['Tmin'])


# In[7]:


The end!

