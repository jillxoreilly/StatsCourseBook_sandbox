#!/usr/bin/env python
# coding: utf-8

# # Plotting with Pandas
# 
# The <tt>Seaborn</tt> plotting library is designed to be used with Pandas.
# 
# For example, if we want to plot one variable (say age) separately based on another variable (say, which class someone travelled in), we can do it very easily with <tt>Seaborn</tt>

# ## Example: Titanic data
# 
# Let's use the Titanic passenger data again!
# 
# <img src="https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/images/titanic.jpg" width=50% alt="Picture of the Titanic" />
# 
# By the way you can find a description of the dataset including explanations of some of the less obvious column titles, on <a href="https://www.kaggle.com/c/titanic/data">kaggle</a> - a data science website that I got the data from
# 
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


# ### Load the data

# In[2]:


titanic = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/titanic_2.csv')
display(titanic)


# ### Grouping by a categorical variable
# 
# Say we want to plot the distribution of age separately in each travel class on the titanic. 
# 
# We can do this using the "hue" argument in <tt>sns.histplot</tt> or <tt>sns.kdeplot</tt>:

# In[3]:


sns.histplot(data=titanic, x='Age', hue='Pclass')


# Hm, that was a bit messy - it looks clearer as a kdeplot

# In[4]:


# your code here to produce the KDEplot version of the above


# You may notice in the KDEplot it appears as though there were many people with an age below zero.
# 
# Glance back at this histogram - you will see that there are not in fact any people with age <0, but there is a big spike in the passenger counts for young children, which gets smoothed out in the KDE plot resulting in the KDE plot extending below zero.
# 
# ### Countplot
# 
# The simple plotting function <tt>sns.countplot</tt> shows the frequencies of different categories:

# In[5]:


sns.countplot(data=titanic, x='Pclass')


# ... we can break the data down by a second category using the argument <tt>hue</tt> as follows:

# In[6]:


sns.countplot(data=titanic, x='Pclass', hue='Survived')


# Hm, looks like being in 3rd class was not good news on the Titanic.
# 
# ### Barplot
# 
# If we want to plot the mean value of a variable by category (rather than just the count in each category), we can use the function <tt>barplot</tt>

# In[7]:


sns.barplot(data=titanic, y='Age', x='Pclass')


# However, in many cases it will be more informative to plot a <tt>boxplot</tt> or <tt>violinplot</tt>

# In[8]:


sns.violinplot(data=titanic, x='Pclass', y="Age")


# Once again you can use the argument <tt>hue</tt> to break the data down by another category

# In[9]:


# Your code here for a barplot of age, broken down by class, 
# and further broken down by whether the passenger survived - 
# base it on the countplot example above


# ### Scatterplot
# 
# We can use similar tricks in a scatterplot.
# 
# Let's plot a scatterplot of age against fare paid:

# In[10]:


sns.scatterplot(data=titanic, x='Fare', y='Age')


# In[11]:


# Your code here to repeat the scatterplot above but plotting different classes in different colours, using 'hue'


# In[ ]:




