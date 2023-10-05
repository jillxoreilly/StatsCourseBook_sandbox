#!/usr/bin/env python
# coding: utf-8

# # Handling NaNs
# 
# `NaN` (Not a Number) is a special value used to indicate missing data in many scientific programming languages.
# 
# Using `NaN` instead of a numerical dummy value like 9999 or 0 is helpful because Python functions either ignore NaNs by default, or can be set to ignore NaNs using an optional function argument.
# 
# In this section we will review:
# 
# * Why `NaN` is better than a numerical dummy value
# * How to check for NaNs in a dataframe
# * Setting the NaN-handling in Python functions
# 
# Set up Python Libraries
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
# You will need to download the file heartAttack.csv from Canvas to your computer, then import it

# In[2]:


hospital=pd.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(hospital)


# ## `NaN` is not a number!
# 
# Humans may recognise dummy values like 9999 for what they are, but the computer will treat them as numbers.
# 
# Say we want to find the mean and standard deviation of the age of patients in out hospital dataset (remembering that issing data were coded as 9999):

# In[3]:


print(hospital.AGE.mean())
print(hospital.AGE.std())


# **Think** is the value for standard deviation realistic?
# 
# These values include the 9999s just as if there were really people 9999 years old in the sample.
# 
# If we replace the 9999s with `NaN` we get the correct mean and standard deviation for the 'real' values, excluding the missing data

# In[4]:


hospital.AGE.replace(9999, np.nan, inplace=True)
print(hospital.AGE.mean())
print(hospital.AGE.std())


# In[5]:


The mean has changed slightly, and the standard deviation is now much more reasonable.


# ## Creating `NaN`s
# 
# If we want to set a value to `NaN`, we can't just type <tt>NaN</tt> or <tt>"NaN"</tt>
# 
# Istead, we 'create' the value `NaN` using the `numpy` function `np.nan`, for example:
# 
# ``
# hospital.loc[1, 'CHARGES']=np.nan # set the value of CHARGES in row 2 to be `NaN`
# ``
# 

# ## Check for `NaNs`
# 
# - `df.isna()`
# - `df.isna().sum()`
# 
# `NaN`s are ignored by many Python functions, however you may still want to know if there were any (and how many) in any given set of data.
# 
# To check for missing values, coded as `NaN`, we use the function `df.isna()`:

# In[16]:


hospital.AGE.isna()


# `df.isna()` returned a column with <tt>True</tt> or <tt>False</tt> for each value of <tt>AGE</tt> - <tt>True</tt> ofr people where the age is coded as `NaN`.
# 
# This isn't very readable, but if we want to know how many `NaN`s were in the column, we can use a trick: Python treats <tt>True</tt> as <tt>1</tt> and <tt>False</tt> as <tt>0</tt>. So if we just take the sum of the column, we get the total nuber of `NaN`s:

# In[17]:


hospital.AGE.isna().sum()


# Two people's age was coded as `NaN`.
# 
# ## NaN handling by Python functions
# 
# Many Python functions automatically ignore NaNs.
# 
# These include 
# * `df.mean()`
# * `df.std()`
# * `df.quantile()`
# .... and most other descriptive statistics
# 
# * `sns.histogram()`
# * `sns.scatter()`
# ... and most other `Seaborn` and `MMatplotlib` functions
# 
# However, some functions do *not* automatically ignore `NaN`s, and instead will give an error message, or return the value `NaN`, if the input data contains `NaN`s.
# 
# This includes a lot of functions from the library `scipy.stats`, which we will use later in the course. For example, say I want to use a $t$-test to ask if the male patients are older than the females
# * don't worry if you don't yet know what a $t$-test is - this will make sense when you return to it for revision

# In[34]:


stats.ttest_ind(hospital.query('SEX == "M"').AGE, hospital.query('SEX == "F"').AGE)


# The function `stats.ttest_ind()` performs an independent samples $t$-test between the two samples we gave it (the ages of mmale and female patients) and should return a $t$-value (<tt>statistic<tt>) and a $p$ value (<tt>pvalue<tt>)
#     
# Right now both of these are `NaN` because the `NaN`s in the input were not ignored.
#     
# We can tell the function `stats.ttest_ind()` to ignore `NaN`s, using the argumment `nan_policy='omit'`:

# In[33]:


stats.ttest_ind(hospital.query('SEX == "M"').AGE, hospital.query('SEX == "F"').AGE, nan_policy='omit')


# Now we have actual values instead of NaN: $t = -35.4$ and $p = 3.1 x 10^{-262}$ (a very small number)
# 
# **If you run a Python function and the output is `NaN`, you very probably need to change how the function handles `NaN`s using an argument. Check the function's help page online to get the correct syntax.**

# In[ ]:




