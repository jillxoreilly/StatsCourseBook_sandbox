#!/usr/bin/env python
# coding: utf-8

# # Standard deviation and IQR
# 
# 
# The standard deviation and inter quartile range are measures of the <i>spread</i> of a distribution.
# 
# They both tell you something about the typical or average value in your dataset - but different things.

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


# ## The Standard Deviation
# 
# The standard deviation is obtained as follows:
# 
# 1. Find the difference between each datapoint and the mean value $(x_1 - \bar{x}), (x_2 - \bar{x})... (x_n - \bar{x}) $
# 
# 2. Square each difference
# 
# 3. Add them all up 
# 
# 4. Divide by ($n-1$) where $n$ is the number of datapoints
# 
# 5. Take the square root of the whole thing
# 
# 
# The process can be described by the formula
# 
# $$ s_x^2  = \sum\frac{(x_i - \bar{x})^2}{(n-1)}$$
# 
# Where $s^2$ is the standard deviation squared (ie the variance), so the sd is the square root of the right hand side.

# ### Toy example: standard deviation
# 
# To understand the properties of the standard deviation, let's start with a <i>toy example</i>, i.e. a very small dataset in which it is easy to see what is going on.
# 
# Let's say these are the heights (cm) and weights (kg) of 6 toddlers:

# In[2]:


data = {'Name': ["Axel","Benji","Charlie","Danny","Edward","Freddie"],
        'Height': [89.0, 96.2, 93.4, 88.1, 91.7, 93.2],
        'Weight': [12.4, 13.8, 13.1, 12.9, 13.5, 14.0],}

toddlerData = pandas.DataFrame(data)
display(toddlerData)


# We saw previously that the mean height was 91.9 cm and we can see from the data frame above that the range is about +/- 4cm around the mean.
# 
# Let's obtain the standard deviation using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html"><tt>std</tt></a> method from pandas:

# In[3]:


toddlerData['Height'].std()


# Shall we check that we can obtain the same value by implementing the formula ourselves?

# In[4]:


# calculate the mean
m = toddlerData['Height'].mean()

# add a column containing the deviations
toddlerData['d'] = toddlerData['Height']-m

# add a column containing the squared deviations
toddlerData['d2'] = toddlerData['d']**2

# check what we have done so far
display(toddlerData)


# Great now we can go on with the formula

# In[5]:


# sum of squared deviations
ss = toddlerData['d2'].sum()

# obtain n
n = toddlerData['Height'].count()

# calculate variance
sd2 = (ss/(n-1))

# standard deviation is square root of variance (ie variance to power 0.5)
sd = sd2**0.5

print(sd)


# Hurrah!

# ## IQR and quantiles
# 
# The inter quartile range or IQR is the difference between the 25th and 75th centile of a distribution.
# 
# We can calculate it easily using Python:

# In[6]:


IQR = toddlerData['Height'].quantile(0.75) - toddlerData['Height'].quantile(0.25)

print(IQR)


# Note that it can also be useful to get other quantiles.
# 
# For example, if we wanted to know how high to make a playhouse so 90% of toddlers can stand up inside, we would be interested int he 90th centile (0.9 quantile) of the height distribution

# In[7]:


toddlerData['Height'].quantile(0.9)


# In[ ]:




