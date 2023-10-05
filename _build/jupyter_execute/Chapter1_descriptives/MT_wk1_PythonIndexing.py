#!/usr/bin/env python
# coding: utf-8

# # Python: Descriptives and Indexing
# 
# In this notebook we cover some key <tt>Pandas</tt> syntax and functions:
# 
# * Syntax for getting various descriptive statistics from a `Pandas` dataframe
# * Syntax for **indexing** a dataframe - finding the rows and columns that you need
#     * this allows you to get descriptives for specific rows and columns
# 
# Here we meet **indexing** in the context of descriptive statistics, but indexing is something you will do every single time you write code for data analysis. Incorrect syntax in indexing is the number one biggest source of bugs for student on this course, so it is well worth spending the time to get to grips with it.
# 
# You absolutely should work through all the exercises in this notebook in advance of the tutorial.
# 
# ## Set up Python Libraries
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


# ## Get descriptive statistics
# 
# We will look at indexing in the context of getting descriptive statistics for the different variables in a dataframe, and/or for a selection of rows.
# 
# Pandas has a number of built-in functions to get descriptive statistics:
#     
# - `df.mean()`   -  gets the mean
# - `df.median()` - gets the median
# - `df.var()` - gets the variance
# - `df.std()` - gets the standard deviation
# - `df.min()` - gets the minimum value
# - `df.max()` - gets the maximum value
# - `df.corr()` - gets the correlation coefficient (Pearson or Spearman)
# 
# in the function names above, `df` is just a placeholder for "dataframe" 
# 
# You can replace `df` with the name of your dataframe (in which case you will get a table with the descriptive statistic you asked for, for every column containing numerical data)
# 

# In[3]:


weather.mean()


# Which columns from the dataframe are missing from the table of means?
# * Month is missing because the values are strings (words); we only get the mean for numerical columns
# 
# ## Decriptives for a single column
# 
# Format:
# - `df.column.mean()`
# 
# You might just want the mean for one column, in which case you can include the column name as follows:

# In[4]:


weather.Tmax.mean()


# Instead of a whole table of means, many of which were irrelevant, we now just have the single number we wanted - the mean of <tt>Tmax</tt>
# 
# * *Think* check that the value obtained this way matches the one in the table above.
# 
# #### Why does it work?
# 
# The commmand `weather.Tmax.mean()` has two steps.
# 
# **Step 1:**
# 
# The syntax `weather.Tmax` (or more generally, `df.column`) returns just the one column of the dataframe as a <tt>series</tt> (essentially a one-column table).
# 
# Look:

# In[5]:


weather.Tmax


# If we liked, we could give this single-column series a name a 'save' it:

# In[6]:


DailyMaxima  = weather.Tmax
print(DailyMaxima)


# However, we don't need to do that as we can just tack the `.mean()` function onto it directly as follows:

# **Step 2:**
# 
# The syntax `.mean()` gets the mean of the thing before the dot (i.e. the series you created with the command `weather.Tmax`)

# In[7]:


weather.Tmax.mean()


# ### Exercises
# 
# Complete the following quick practice questions:

# In[8]:


# get the mean daily rainfall


# In[9]:


# get the median daily rainfall


# In[10]:


# get the standard deviation of the maximum daily temperature


# In[11]:


# find the minimum value of "year" (you will need two separate commands)


# ## Get descriptives for a subset of rows
# 
# - `df.query('columnname == number')`
# - `df.query('columnname == "string"')`
# - `df.query('columnname1 == value1 and columnname2 == value2')`
# 
# 
# Say I want to know the mean daily maximum temperatures for the year 1921.
# 
# #### Step 1: find the relevant rows
# 
# I first need to somehow pull out the rows of the table where the value for <tt>YYYY</tt> is <tt>1921</tt>
#     
# I can do this using the function `df.query`, for example <tt>weather.query('YYYY == 1921')</tt>
#    * **note** the quote marks surrounding the whole query
#    * **note** the double equals sign `==`, which is used for *checking* if two bvalues are equal (as opposed to setting a value)

# In[12]:


# get all the rows where year is 1921
weather.loc[weather.YYYY == 1921]


# Note the size of this table - there are 365 rows. Why?
# * In the original table `weather`, there is one row per day
# * 365 of those rows (days) match the criterion 'YYYY = 1921' because there are 365 days in a year.
# 
# If I wanted to, I could give this table a name and 'save' it for later use:
# 

# In[13]:


weather1921 = weather.query('YYYY == 1921') # create a new daataframe for just 1921
weather1921 # look at my new dataframe


# ... but I don't need to do this as I can tack on more commands to complete my goal in a single line of code.
# 
# #### Step 2: find the relevant column
# 
# Now that I have grabbed the relevant rows, I narrow it down to column <tt>Tmax</tt>

# In[14]:


weather.query('YYYY == 1920').Tmax


# #### Step 4: add in the actual function
# 
# FInally, I can tack on teh function I want to run on my selected rows and column: `mean()`:

# In[15]:


weather.query('YYYY == 1920').Tmax.mean()


# ### Exercises
# 
# Complete the following quick practice questions:

# In[16]:


# Get the mean daily maximum temperature in 2006


# In[17]:


# Get the mean daily minimum temperature in 1947


# ## Get descriptives for one category
# 
# What about getting the mean daily maximum temperatures for, say, October? So I need to pull out all the rows in which <tt>'MM'</tt> matches <tt>'October'</tt>
# 
# The syntax is very similar, but now I am matching a string `"October"`, so it needs to be in quotes:
#     

# In[18]:


weather.query('MM == "October"').Tmax.mean()


# * **note** you can actually use single and double quotes interchangeably in Python, but in cases like this where you have quotes within quotes, it is better to use both types to avoid the computer getting confused about which opening and closing quotes to pair up.
# 
# so you could do either of these
# 
# - weather.query('MM == "October"').Tmax.mean()
# - weather.query("MM == 'October'").Tmax.mean()
# 
# but not these
# 
# - weather.query('MM == 'October'').Tmax.mean()
# - weather.query("MM == 'October'").Tmax.mean()

# ### Exercises
# 
# Complete the following quick practice questions:

# In[19]:


# Get the mean daily rainfall in January


# In[20]:


# Get the mean daily rainfall in June


# ## Match multiple conditions
# 
# What if I want to know the mean daily maximum temperature in 1920 for June only?
# 
# We can simply use `and` or `&` to pass `df.query()` multiple conditions:

# In[21]:


# mean daily maximumm temperature in 1920
weather.query('YYYY == 1920').Tmax.mean()


# In[22]:


# mean daily maximumm temperature in 1920
weather.query('YYYY == 1920 & MM == 6').Tmax.mean()


# * **Think** hopefully the value for June is higher than the avergae for the whole year? If not something has gone wrong!

# ### Exercises
# 
# Complete the following quick practice questions:

# In[23]:


# Get the mean daily rainfall in June 2007


# In[24]:


# Get the minimum temperature in January 1947


# ## Syntax for correlation
# 
# When we run a correlation, we need to index *two* columns - the two we are correlating.
# 
# Using the `pandas` function `df.corr()` we can do so as follows:

# In[28]:


# get the correlation between columns Tmin and Tmax of dataframe weather
weather.Tmin.corr(weather.Tmax)


# We can set the type of correlation to Pearson or Spearman as appropriate (the default is Pearson's $r$):

# In[30]:


# get the correlation between columns Tmin and Tmax of dataframe weather
weather.Tmin.corr(weather.Tmax, method='spearman')


# #### Exercises
# 
# Complete the following practice questions to help you get to grips with the syntax for correlation:

# In[39]:


# Find the Spearman correlation between daily mean temperature Tmean, and rainfall
weather.Tmean.corr(weather.Rainfall_mm, method='spearman')


# In[40]:


# Find the correlation between year and daily mean temperature
weather.Tmean.corr(weather.YYYY)


# #### All-by-all correlation matrix
# 
# We can also quickly output all the correlations bbetween all possible pairs of columns in a dataframe by simply not giving any column index:

# In[31]:


weather.corr()


# The problem with this is that the figure we want is often buried amongst a lot of irrelevant correlation coefficients.
# 
# #### Correlation using `scipy.stats`
# 
# Note that here we aare using the `pandas` function `df.corr()`
# 
# Later in the course we will use two functions from a library called `scipy.stats`:
# 
# * `stats.pearsonr()`
# * `stats.spearmanr()`
# 
# These are actually a bit more useful as they give us a $p$-value for the correlation as well as the correlation coefficient
# * don't worry if you don't know what a $p$-value is yet - this will be covered later in the course
# 
# `scipy.stats` will be used extensively in the module on hypothesis testing

# In[ ]:




