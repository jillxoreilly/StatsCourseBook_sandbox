#!/usr/bin/env python
# coding: utf-8

# # Key Python syntax: indexing
# 
# In this notebook we cover some key <tt>Pandas</tt> syntax and functions:
# 
# * Syntax for **indexing** a dataframe - finding the rows and columns that you need
# 
# **Indexing** is something you will do every single time you write code for data analysis. Incorrect syntax in indexing is the number one biggest source of bugs for student on this course, so it is well worth spending the time to get to grips with it.
# 
# ## Set up Python Libraries
# 
# As usual you will need to run this code block to import the relevant Python libraries

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
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
# We have seen a number of functions to get descriptive statistics:
#     
# - `df.mean()`   -  gets the mean
# - `df.median()` - gets the median
# - `df.var()` - gets the variance
# - `df.std()` - gets the standard deviation
# - `df.min()` - gets the minimum value
# - `df.max()` - gets the maximum value
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


# ## Tables of descriptive statistics
# 
# When you are writing a report on a dataset you might like to generate a nice table with the descriptive statistics that you need all together in one place|
# 
# There are a couple of ways to do this
# 
# ### Quick look
# 
# - `df.describe()`
# 
# We can output a standard set of descriptives for all the numerical columns in the dataframe by just using `df.describe()`

# In[25]:


weather.describe()


# * **note** MM is missing from the table because the values are not numerical
# 
# This can be good for a quick look but most likely you will not need all these stats on aall the variables - if you were producing a report for an assignment (or a client) you would want to customize the table
# 
# ### Custom table
# 
# `df.agg({'columname':['mean', 'std', 'count']})`
# 
# You can create a table with the just the stats you need using the function `df.agg()`
# 
# This is not essential (although it does look nice in a report) - the syntax is a bit fiddly but you can copy from this example which gives the mean and standard deviation for <tt>Tmin</tt> and <tt>Tmax</tt>:

# In[26]:


# get mean and sd for Tmin and Tmax
weather.agg({'Tmin':['mean', 'std'], 'Tmax':['mean', 'std']})


# Finally, instead of doing that for the whole dataframe `weather`, you can select rows using `df.query()` as before:

# In[27]:


# get mean and sd for Tmin and Tmax in June
weather.query('MM == 6').agg({'Tmin':['mean', 'std'], 'Tmax':['mean', 'std']})


# In[ ]:




