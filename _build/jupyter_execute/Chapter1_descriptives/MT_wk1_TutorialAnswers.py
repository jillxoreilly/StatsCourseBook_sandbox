#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# This week's tutorial exercises focus on indexing and obtaining descriptive statistics
# 
# ### Set up Python Libraries
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


# ### Import a dataset to work with
# 
# You will need to download the file OxfordWeather.csv from Canvas to your computer, then import it

# In[2]:


weather = pandas.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
display(weather)


# ## Exercises
# 
# In the following questions, we descriptive statistics and indexing to answer some questions about the weather and climate in Oxford.
# 
# Where you are asked to calculate a value (such as the mean) rather than output a table, you should **report your answer in words** in the text box below the code block.
# 
# Where the question asks you to "comment", you are simmply being asked to engage with the data/ explain what  you notice in plain English. Please discuss with your fellow students and your tutor as this is a really important skill for data analysis.
# 
# ### Part 1: Heat

# #### a. What was the hottest temperature on record?
# 
# Note that the dataset ends in April 2022 and therefore does not include the record heatwave of summer 2022.

# In[12]:


# Your code here
weather.Tmax.max()


# *Your text here*

# #### b. On what date did the hottest temperature occur?
# 
# Hint: you could use `df.query()` to help you here

# In[15]:


# Your code here
weather.query('Tmax == 36.5')


# *Your text here*

# #### c. Display the 10 hottest days on record and comment
# 
# Hint: you can use `df.values_sort()` and `df.head()` or `df.tail()` to help you here

# In[22]:


# Your code here
weather.sort_values(by='Tmax').tail(11)


# *Your comment here*
# 
# Six out of the ten hottest days on record occurred in the last 20 years

# #### d. Find the mean of maximum daily temperature (Tmax) for each month and comment
# 
# Hint: you can use `df.groupby()` to help you here

# In[41]:


# Your code here
weather.groupby('MM').Tmax.mean()


# *Your coment here*
# 
# Unsurprisingly the warmest months are in summer and the coolest are in winter

# #### e. Make a table displaying the mean and standard deviation of Tmax in each month
# 
# Hint: A combination of `df.agg()` and `df.groupby()` will help you here

# In[43]:


# Your code here
weather.groupby('MM').agg({'Tmax':['mean', 'std']})


# #### e. Make a table displaying the mean of Tmax and Tmin in each month
# 
# Hint: A combination of `df.agg()` and `df.groupby()` will help you here

# In[46]:


# Your code here
weather.groupby('MM').agg({'Tmax':['mean'], 'Tmin':['mean']})


# ### Part 2: Rain

# #### a. Run this code block to add a column called <tt>wet</tt> containing a <tt>True</tt> for days on which it rained and <tt>False</tt> otherwise
# 
# We will practice adding columns in a later session

# In[33]:


# Your code here
weather['wet']=weather.Rainfall_mm>0
weather


# #### b. What is the proportion of wet days overall?
# 
# Hint: The values <tt>True</tt> and <tt>False</tt> can be treated as <tt>1</tt> and <tt>0</tt> respectively.
#     
# To get the proportion of days on which <tt>wet==True</tt>, we can use a programmming trick which is to simply take the mean of the column <tt>wet</tt>:
#     
# * say there are 100 days in my sample
#     * say 66 of them, <tt>wet==True==1</tt>
#     * for the other 44, <tt>wet==False==0</tt>
# * If we take the mean, this gives us the proportion of wet days because we:
#     * add up all the values (answer=66) 
#     * divide by the number of cases (100)
#     * result is 66/100 = 0.66 or 66%, the proportion of wet days

# In[48]:


# your code here
weather.wet.mean()


# *Your text here*
# 
# It rains on 46% of days

# #### c. What is the proportion of wet days in each month? Comment on your findings
# 
# Hint: use `df.groupby()`

# In[51]:


# your code here
weather.groupby('MM').wet.mean()


# *Your comments here*
# 
# The proportion of wet days is always between 40 and 53% (ie, it rains a lot).
# Unsurprisingly, the dryest months are in early summer (May,June,July) and the months with the most wet days are in winter (December/January)

# #### d. What is the mean quantity of rainfall (in mm) in each month? Comment on your findings

# In[52]:


# your code here
weather.groupby('MM').Rainfall_mm.mean()


# *Your comment here*
# 
# The quantity of rain follows a different pattern from the proportion of wet days - March has the lowest mean rainfall (perhaps it tends to drizzle in March?!) and October has the highest (it rains like it means it)

# #### e. Display the 10 wettest days on record and comment

# In[40]:


# Your code here
weather.sort_values(by='Rainfall_mm').tail(25)


# *Your comment here*
# 
# * Almost all the wettest days are in summer, suggesting extreme rainfall is more likely in summer (perhaps due to convection storms?)
# * There is no obvious trend for more of the wettest days to be recent (evidence for climate change less clear than in temperature data)

# #### f. Compare and contrast the different findings in part 2 c,d, and e
# 
# Different descriptive statistics tell us different things about the same data!

# *Your comments here!*
# 
# Bring together the observations on rainfall
# * It rains on pretty much half of all days in Oxford!
# * Rain is more likely in winter than summer
# * The total volume of rain is greatest in Autumn and lowest in spring
# * Extreme rain is almost always in summer

# ### Snow
# 
# #### a. Create a dataframe containing the weather on Christmas day, for all the years in which there was a White Christmas 
# 
# Hint: we don't have a column telling us when is has snowed, but it is reasonable to assume this happens when the minimum temperature dips below zero, and Rainfall_mm is above zero.

# In[61]:


# 
WhiteChristmas = weather.query('MM==12 and DD==25 and Tmin<0 and wet==True')
WhiteChristmas


# #### b. Sort the dataframe <tt>WhiteChristmas</tt> by year and comment

# In[62]:


WhiteChristmas.sort_values(by='YYYY')


# *Your comments here*
# 
# General descriptive coments/ engageent with the data to be encouraged, e.g.
# 
# * White Christmasses are not very common now (only three in the last 50 years)
# * They have never been all that common although there was a run of them in the 1870's
# * The most recent one was in 2018, however there wasn't enough snow to play in (0.1mm of rain - so maybe 1mm of snow!)
# 
# * There have been only a handful of Christmas days with a worthwhile amount of snow, notably 1878 and and 1923 (>10mm rainfall, which would mean more than 10cm of snow)

# #### c. Any issues with our definition of 'snow'?
# 
# We defined snow as when the <tt>Tmin</tt> falls below zero and Rainfall is non-zero. 
# 
# * Do you think this over- or under- estiamtes the number of snowy days?
# * Why?

# *Your comments here*

# #### d. How common is 'proper' snowfall in Oxford?
# 
# Let's focus on days with enough snowfall to make at least a tiny snowman! Assume that this happens when TMin is below zero and there is more than 4mm of rainfall 
# 
# * 4mm of rain makes about 5cm of soggy snow in Oxford conditions, although it would make a uch greater depth of powder in a cold dry atmosphere like Utah or Colorado
# 
# Create a dataframe called <tt>SnowDays</tt> containing only days with enough snow to make a snowman.
# 
# You can check how often this happened in recent years using `df.tail()`

# In[71]:


SnowDays = weather.query('Tmin<0 and Rainfall_mm>4').tail(25)
SnowDays


# *Your comments here*
# 
# * It snows most years! 
# * It mostly snows in January of February, but sometimes in November or December and occasionally in April

# In[ ]:




