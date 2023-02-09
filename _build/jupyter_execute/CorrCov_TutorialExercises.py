#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# ## Heart attack data
# 
# In this example we will use data from 12,843 patients admitted to hospital in New York City with a heart attack.
# The data were collected via the Medicare system and are modified from a dataset at <a href="https://dasl.datadescription.com/">DASL</a>
# 
# These exercises will review some of the skills learned over the last three weeks. They will also prepare you for the first hand-in exercise: to produce a report for the Chair or Medicare, describing the main factors affecting cost and length of hospital stay for heart attack patients.

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

# In[2]:


heartAttack=pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(heartAttack)


# What data do we have for each patient?
# <ul>
#     <li> CHARGES is the dollar cost of the hospital stay
#     <li> LOS is Length of Stay (in hospital) in days
#     <li> DIED is coded as 1 if the person died, 0 if they left hospital alive
#     <li> DRG is a discharge code
# </ul>
# 
# ### Evaluate missing and bad data values
# 
# How many missing values (NaNs) are there for each variale (column) in the dataset?

# In[3]:


# your code here!


# Can you find any data points that look like outliers or misrecorded values?
# 
# You could try the following techniques:
# <ul>
#     <li> plot the data to see if outliers are obvious
#     <li> sort the data using <tt>pandas.df.sort_values()</tt> to bring extreme values to the top (or bottom) of the dataframe, then display the sorted dataframe
#     <li> obtain descriptive statistics and check the max an min value for each column of the dataframe
# </ul>
# 
# For patients with outlier values, you should decide whether to:
# 
# <ol>
#     <li>replace individual datapoints with NaNs
#     <li>replace the entire patient record with NaNs
#     <li>remove the entire record from the dataset with <tt>pandas.df.drop()</tt>
#     <li>retain the data as is, at least for now
# </ol>
# Think how you would justify your choice to a reader
# 

# In[4]:


# your code here!


# ### Cost of hospital stay
# 
# The column <tt>CHARGES</tt> tells us how much the hospital stay cost in $.
# 
# Plot the distribution of charges using a suitable plot type. 

# In[5]:


# Your code here


# Describe the distribution of charges in words, including some descriptive statistics. 
# 
# Part of the task here is to decide which descriptives are useful to give the reader a summary fo the distribution of charges. 
# 
# Try to make a choice yourself, and then discuss with your tutor if unsure.

# In[6]:


# Your code here


# ### Length of hospital stay
# 
# The column <tt>LOS</tt> tells us how long each patient stayed in hospital.
# 
# Plot the distribution of length of stay using a suitable plot type. 

# In[7]:


# Your code here


# Hm, there is an interesting feature in that data distribution - what is it?
# 
# Can you think what the origin of this feature is (what caused it?)
# 
# HINT: it may help to plot data separately for the different values of one of the categorical variables, using the argument <tt>hue</tt> in the plotting function. You will get a clearer result with a KDE plot than a histogram (try both and see why).

# In[8]:


# Your code here


# .......Your comment here......... double click to edit this text box!

# ### Association between cost and length of stay
# 
# Probably the biggest factor affecting the cost of the stay is the length of the stay.
# 
# Produce an appropriate plot and descriptive statisitics to demonstrate the relationship between cost and length of stay.

# In[9]:


# Your code here


# .......Your comment here......... double click to edit this text box!

# You may remember from the exercises on covariance that change in $y$ for one unit in $x$ is given by the regression slope:
# 
# $$ b = \frac{s_{xy}}{s^2_x} $$
# 
# Apply the equation in Python to find out how much, on average, one extra day in hospital costs.

# In[10]:


# Your code here


# ## Association between length of stay and age
# 
# Older people tend to stay longer in hospital - produce an appropriate plot and descriptive statisitics to demonstrate the relationship between cost and length of stay.

# In[11]:


# Your code here


# .......Your comment here......... double click to edit this text box!

# ### Sex difference in mortality
# 
# A greater proportion of the women died than men.
# 
# Illustrate this assocation between sex and mortality using <tt>sns.countplot()</tt>

# In[12]:


# Your code here


# ### Age difference between sexes
# 
# Could the higher death rate for women be explained by their age?
# 
# Explore with appropriate plots and summarize your observations in words including descriptive statstics.

# In[13]:


# Your code here


# .......Your comment here......... double click to edit this text box!

# ### What is DRG?
# 
# The column DRG is a discharge code, which tells ou something about the patient's destination after the hospital. 
# 
# I do not know what the different codes mean, ut you could try to find out by plotting some of the other variables broken down by DRG (eg using the <tt>hue</tt> property of <tt>sns</tt> plotting functions</tt>). You should at least eb ablbe to work out what code 123 means.

# In[14]:


# Your code here


# .......Your comment here......... double click to edit this text box!

# In[ ]:




