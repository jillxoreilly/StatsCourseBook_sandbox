#!/usr/bin/env python
# coding: utf-8

# # Loading data from a .csv file
# 
# This section covers how to load data from a csv file saved on your own computer
#     
# You need to do this for the hand-in assignment set in 3rd week so make sure you try it, and check with your tutor in class if stuck.

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()
sns.set_style('white')


# 
# In this course you have generally worked with data in Pandas.
# 
# To get the data into pandas, you usually run a readymade code block like this:

# In[2]:


# load the data and have a look
heartRates = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/HeartRates.csv')
display(heartRates)


# Let's take a closer look at that.
# 
# You are using a function called `pandas.read_csv()`
# 
# Inside the brackets is a URL for an online file repository (my Github if you are interested), from which the file will be read.
# 
# I place all the datafiles for the course on my online repository so I can edit them as needed. However, in 'real life' your data wouldn't be on my github, they would be in a csv file on your own computer.
# 
# * Download the datafile CloudSeeding.csv from this week's page on Canvas and place it in the same directory (folder) as the downloaded copy of this Jupyter notebook
# 
# Now try running this code block:

# In[3]:


clouds = pandas.read_csv('CloudSeeding.csv')
clouds


# OOh, it worked!
# 
# 
# ### Subdirectories
# 
# Say you have all your Jupyter Notebooks (including this one) in a nice tidy folder (or directory) called `StatsClassWeek3` and you don't want lots of messy csv files lying around in there.
# 
# No problem - in your file browser, go to the folder `StatsClassWeek3` and cerate a new folder (or directory) called `data`. Place the csv file `CloudSeeding.csv` in the folder `data`
# 
# Now we run the following code:
# 

# In[4]:


clouds = pandas.read_csv('data/CloudSeeding.csv')
clouds


# The slash in the commmand `pandas.read_csv('data/CloudSeeding.csv')` just means that `data` is the name of a folder and `CloudSeeding.csv` ia inside that folder

# In[ ]:




