#!/usr/bin/env python
# coding: utf-8

# # Standardizing data
# 
# Some data are recorded in naturally meaningful units; examples are 
# * height of adults in cm
# * temperature in $^\{circ}C$
# 
# In other cases, units may be hard to interpret because we don't have a sense of what a typical score is, based on general knowledge
# * scores on an IQ test marked out of 180
# * height of 6-year-olds in cm
# 
# A further problem is quantifying how unusual a data value is when values are presented as different units
# * High school grades from different countries or systems (A-levels vs IB vs Arbitur vs.....)
# 
# In all cases it can be useful to present data in standard units.
# 
# Two common ways of doing this are:
# * Convert data to Z-scores
# * Convert data to quantiles
# 
# In this section we will review both these approaches.
# 
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


# ### Import a dataset to work with
# 
# Let's look at a fictional dataset containing scores on English and Maths tests for 150 children.

# In[2]:


hospital=pd.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(hospital)


# ## Z score
# 
# The Z-score tells us how many standard deviations above or below the mean of the distribution a given value lies.
# 
# For example, for women’s heights the standard deviation
# 
# is 7 and the mean is 162cm, so a woman 169cm tall (one sd above the mean) has a Z-score of 1
# 
# A woman whose height is
# 
# below the mean (148cm) has a Z-score of -2.
# 
#     What is the Z-score of a woman whose height is 172.5cm?
#     What about a woman whose height is 150cm? 
# 
# Reporting the Z-score of a value is useful as we automatically know where the value sits on the normal curve without having to check the normal CDF on Python or in a table (because the probability of obtaining a given Z-score does not depend on the mean and sd of the given dataset)
# 
# For example, a Z-score greater than 1.65 occurs only 5% of the time and a Z score greater than 2.6 occurs only 1% of the time.

# ### Disadvantages of the Z score
# 
# Z score tells us how many standard deviations above or below the mean a datapoint lies.
# 
# One mmajor advantage of the Z-score is that for Normally distributed variables it tells us exactly how unlikely a data value is
#     * Don't worry if you don't know what the Normal distribution is yet - you will earna about this in the next block
# 
# This has a couple of disadvantages:
#     * it is only really meaningful for symmetrical data distributions (especially the Normal distribution) - for skewed distributions, there will be momre datapoints witha  Z-score of, say, +2, than -2
#     * It is not easily understood by non statistically trained people
#     
# It is sometimes more meaningful to standardize data by presenting them as *quantiles*

# ## Quantiles
# 
# Quantiles (or centiles) tell us what proportion of data points are expected to exceed a certain value. This is easy to interpret. 
# 
# For example, my six year old daughter is 128cm tall, would you say she is tall for her age? You probably have no idea - in contrast to adult heights where people might have a sense of the distribution due to general knowledde (eg 150cm is smmall and 180cm is tall)
# 
# We can use centiles in two ways:
# 
# * The 90th centile of height for a 6 year old is XX, so we expect 10% of six year olds to be taller than XXcm.
# * Conversely, a 6 year old with height XXX cm lies on the 93rd centile, which means they are taller than 93% of children the same age.
# 
# To calculate a given quantile of a dataset we use `df.quantile()`, eg

# In[3]:


heights.quantile(q=0.9) # get 90th centile


# In[ ]:


To find out on which quantile a given datapoint lies, we can use a couple of `pandas` functions as follows:


# In[ ]:


(heights.height > 128.len()/heights.len()

