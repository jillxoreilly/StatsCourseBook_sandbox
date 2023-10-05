#!/usr/bin/env python
# coding: utf-8

# # Boxplot and Violinplot
# 
# If we want to compare data distributions across categories, it can be useful to have a plot that highlights key features (eg, the median and quartiles) whilst eliminating unnecessary detail. Sometimes less is more!
# 
# In this notebook we cover four `Seaborn` functions that are used to compare between categories:
# - `sns.boxplot()` - compare key descriptives for each category at a glance
# - `sns.violinplot()`- compare the full distribution for each catcgory at a glance
# - `sns.barplot()` - compare a single statistic (eg the mean) across categories
# - `sns.countplot()` - compare the number of datapoints in each category
# 
# ## Oxford Weather example
# 
# We will work with historical data from the Oxford weather centre, which has data for every day in Oxford since 1827!
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
import pandas as pd
import seaborn as sns
sns.set_theme(style='white')
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### Load and inspect the data
# 
# Let's load some historical data about the weather in Oxford, from the file "OxfordWeather.csv"

# In[2]:


weather = pd.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
display(weather)


# Have a look at the dataframe. 
# 
# What do you think is contained in each column? 
# 
# <ul>
# <li>Each row is a single day from 1827 to 2022. The columns YYYY,MM,DD give the date.
# <li>The columns Tmax, Tmin and Tmean give information about the temperature
# <li>We also have a record of the rainfall each day
# </ul>
# 
# ### Boxplot
# 
# Say we want to plot the mean temperature in each month of the year. We have almost 200 datapoints for every date (and 30ish dates within each month, so 6000 measurements per month!)
# 
# We can summarise the distribution of temperatures in each month using a boxplot:

# In[3]:


sns.boxplot(data=weather, x="MM", y="Tmax")
plt.show()


# The boxplot is designed to show a handful of key features of the data distribution:
# 
# * The top and bottom of the box are the 25th and 75th quantiles (1st and 3rd quartiles)
# * The line within the box is the 50th centile (median)
# * the whiskers are the 'robust range' of the data 
#     * in datasets with no outliers, the whiskers reach to the smallest and largest values
#     * values more than 1.5 x IQR from the end of the box are treated as outliers and plotted as separate dots
# 
# #### Less is more
# 
# Using a simple boxplot for each month, we can easily see the **trend across months** for warmer weather in the summer and cooler weather in the winter.
# 
# Within each month we can also see some information about the distribution - for example:
# 
# * Temperatures are more variable in winter and summer, than in autumn and spring
# * In winter, the distribution of temperatures has negative skew (there are some unusually cold years) but in summer the converse is true - this is evident from the position of the median within each box but is clearer in a violinplot (see below)
# 

# ## Violinplot
# 
# Using Python, you can make a slighly fancier version of the boxplot called a **violinplot**. 
# 
# The violinplot shows the full distribution of data rather than the summary captured in a boxplot - the violin body is basically a KDE plot.
# 
# Let's give it a try using the function `sns.violinplot()`

# In[4]:


sns.violinplot(data=weather, x="MM", y="Tmax")
plt.show()


# This is a nice compromise - still easy to "eyeball" the pattern across categories (in this case, across months) but giving plenty of detail within each category also
# 
# Note for example that the trend for:
# 
# * negative skew in temperature in winter (outliers are cold days)
# * positive skew in summer (outliers are hot days)
# 
# ...is much more clearly visible in the violin plot than in a box plot.
# 
# #### Exercises
# 
# Try the following quick exercise:

# In[5]:


# make a violin plot showing the minimum temperature in each month
sns.violinplot(data=weather, x='MM', y='Tmin')
plt.show()


# ## Barplot
# 
# Sometimes, we want to show even less information, for example just the mean or median for each category.
# 
# We can do this using `sns.barplot()`.
# 
# Say I want to plot the mean value of the maximum daily temperature (Tmax) in each month:

# In[6]:


sns.barplot(data=weather, x='MM', y='Tmax')
plt.show()


# The height of each bar is the mean temperature in that month; the error bars show the 95% confidence interval (but could be altered to show the standard deviation or standard error if you liked - don't worry if these terms are unfamiliar as confidence intervals and standard error will be covered later in the course)
# 
# #### Exercises
# 
# Try the following quick exercise:

# In[7]:


# make a bar plot showing the mean rainfall in each month


# ## Countplot
# 
# Sometimes we are just interested in how many data points fall in each category.
# 
# Since there isn't a straightforward and compelling example with the weather dataset, here is one using the *Titanic* dataset that comes with `seaborn`:

# In[8]:


titanic = sns.load_dataset("titanic")
sns.countplot(data=titanic, x='class', hue='alive')
plt.show()


# Back to the weather data - one thing we could easily count is the number of instances of each date (1st of the month, 2nd of the month, 3rd of the month....)

# In[9]:


sns.countplot(data=weather, x='DD')
plt.show()


# Another way we could use `sns.countplot()` is by creating a dataframe that contains only days fulfilling some criterion (eg, days with no rain) and then make a countplot, as follows:

# In[10]:


drydays = weather.query('Rainfall_mm == 0') # creates a whole new dataframe with only the 0mm rainfall days
sns.countplot(data=drydays, x='MM') # then count the number of days in each month
plt.show()


# #### Exercises
# 
# Can you use `sns.countplot()` to show the number of days with frost (Tmin < 0) in each month?

# In[11]:


# your code here


# In[ ]:




