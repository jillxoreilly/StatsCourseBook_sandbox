#!/usr/bin/env python
# coding: utf-8

# # Tables of descriptive statistics
# 
# When you are writing a report on a dataset you might like to generate a nice table with the descriptive statistics that you need all together in one place
# 
# Below we review a couple of useful pieces of Python syntax for making tables:
# 
# - df.describe()
# - df.agg()
# - df.groupby()
# 
# ### Set up Python Libraries
# 
# As usual you will need to run this code block to import the relevant Python libraries

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


# ## Import a dataset to work with
# 
# You will need to download the file OxfordWeather.csv from Canvas to your computer, then import it

# In[2]:


weather = pandas.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
display(weather)


# ## Quick look: `df.describe()`
# 
# - `df.describe()`
# 
# We can output a standard set of descriptives for all the numerical columns in the dataframe by just using `df.describe()`

# In[3]:


weather.describe()


# **Note-** 
# * <tt>Month</tt> is missing from the table because the values are not numerical
# * We have got descriptives for <tt>YYYY</tt> and 
# 
# This can be good for a quick look but most likely you will not need all these stats on aall the variables - if you were producing a report for an assignment (or a client) you would want to customize the table
# 
# ## Custom table: `df.agg()`
# 
# `df.agg({'columname':['mean', 'std', 'count']})`
# 
# You can create a table with the just the stats you need using the function `df.agg()`
# 
# This is not essential (although it does look nice in a report) - the syntax is a bit fiddly but you can copy from this example which gives the mean and standard deviation for <tt>Tmin</tt> and <tt>Tmax</tt>:

# In[4]:


# get mean and sd for Tmin and Tmax
weather.agg({'Tmin':['mean', 'std'], 'Tmax':['mean', 'std']})


# Finally, instead of doing that for the whole dataframe `weather`, you can select rows using `df.query()` as before:

# In[5]:


# get mean and sd for Tmin and Tmax in June
weather.query('MM == 6').agg({'Tmin':['mean', 'std'], 'Tmax':['mean', 'std']})


# ## Disaggregate by category: df.groupby()
# 
# The syntax `df.groupby()` breaks a dataframe down by the categories you have chosen to group by. Any function you then apply will be done sparately for each of these categories.
# 
# For example, say we want to report the mean value of the peak daily temperature in each month. Remember to get the mean value of the peak daily temperature overall we did:

# In[7]:


weather.Tmax.mean()


# To break it down by month, we insert `.groupby('MM')`:

# In[8]:


weather.groupby('MM').Tmax.mean()


# We can of course combine `groupby()` with `agg()` to make a custom table for each group of data, eg

# In[9]:


# get mean and sd for Tmin and Tmax in each mmonth
weather.groupby('MM').agg({'Tmin':['mean', 'std'], 'Tmax':['mean', 'std']})


# * **Note** `groupby()` is handy to break down datasets according to a categorical variable. In this sense it works similarly to the `hue` argument in some of the plotting functions you will see next week, which allows us to plot data sepaarately for different cases of a categoricaal variable.

# In[ ]:




