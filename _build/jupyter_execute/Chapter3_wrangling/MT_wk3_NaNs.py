#!/usr/bin/env python
# coding: utf-8

# # Locating missing and bad data
# 
# In this notebook we cover:
# * Approaches for **locating outliers**
# * Replacing missing data with **NaN** (how to do it; what choices we need to make)
# 
# 
# 
# As we have seen, if a dataset contains outliers this can distort the calculated values of statistics such as the mean and standard deviation
# 
# In real datasets, outliers are common, often arising from one of the following causes:
# 
# * Real but unusual values 
#     * many basketball players are outliers in terms of height
# * Noise in a data recording system 
#     * in brain imaging data, motion artefacts generated by head movements (MRI) or blinks (EEG) are much larger than the real brain activity we are trying to record
# * Data entry error 
#     * a human types the wrong number, uses the wrong units or misplaces a decimal point
# * Dummy values
#     * In some datasets an 'obvioulsy wrong' numerical value, such as 9999, is used to indicate a missing datapoint
# 
# Identifying and removing outliers and bad data points is a crucial step in the process of preparing our data for analysis, sometimes called *data wrangling*
# 
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
# You will need to download the file heartAttack.csv from Canvas to your computer, then import it

# In[2]:


hospital=pd.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(hospital)


# ## Finding outliers
# 
# When working with a new dataset it is always necessary to check for missing data and outliers. There are a couple of ways of checking:
# 
# 
# ### Check min/max values are plausible
# 
# - `df.describe()`
# 
# Often if there is an outlier or misrecorded data point, the outlier will be the minimum or maximum value in a dataset:
# 
# * If the decimal point is misplaced we get a very large (or small value) - eg a person's height could easily be misrecorded as 1765 cm (over 17 metres!) instead of 176.5 cm
# * If the wrong units are used we could get a very large or small value - eg a person's height is recorded as 1.756 (m) when it should have been recorded as 176.5 (cm) 
# * sometimes 'dummy' values are used as placeholders for missing data - often the duymmy value is `NaN` but sometimes an obviously-wrong numerical value (such as 99, 999 or 9999) is used, which will generally be aa large number compared to real numerical values.
# 
# Therefore, running `df.describe()` and checking the min and max values for each datapoint is a good first step
# 
# Let's try it with our hospital dataset:

# In[3]:


hospital.describe()


# I can see something suspicious!
# 
# * The max values for length of stay (<tt>LOS</tt>) is 9999 days (about 3 years)
# * The max value for Age (<tt>LOS</tt>) is 9999 years
# 
# It looks like <tt>9999</tt> may have been used as a dummy value for missing data.

# ### Plot the data
# 
# What about the column <tt>CHARGES</tt>? 
# 
# * The maximum value of \$48910.12 is horrifyingly high, but as we are (hopefully) unfamiliar with medical billing, it is hard to say if this is an outlier
# * The minimum value of \$3 is also suspect, did they just give the patient a paracetooml and send them on their way?!
# 
# To get a clearer picture we can plot the distribution of <tt>CHARGES</tt>:
# 
# 

# In[4]:


sns.histplot(data=hospital, x='CHARGES')
plt.show()


# Hm, the distribution of costs is skewed, but the maximum value of \$49000 dollars appears to just be the 'tip of the tail' rather than an actual outlier.

# #### How will I know if it is a real outlier?
# 
# Sometimes it is obvious - look what happens when we plot the distribution of Length of Stay:

# In[5]:


plt.figure(figsize=(8,3)) # when I first plotted this it looked a bit squashed so I adjusted the figsize

plt.subplot(1,2,1)
sns.histplot(data=hospital, x='LOS', bins=20)
plt.title('a. Raw data')
plt.xlabel('Length of Stay')

plt.subplot(1,2,2)
sns.histplot(data=hospital.query('LOS < 365'), x='LOS', bins=20)
plt.title('b. Stays over 1 year removed')
plt.xlabel('Length of Stay')

plt.tight_layout()
plt.show()


# **Panel a** (raw data) tells usthat the values of length of stay extend up to 10000 
# * we can't see the bar at 9999 because only a few datapoints have this value compared to 12500 real datapoints, 
# * however, we can see that the axis has autoscaled to accommodate values up to 10000
#     * the autoscaling is a hint to use as data scientists that there are outlier values. 
#     * It's not a good way to present this fact to a client unfamiliar with `Seaborn`'s quirks!
#     * this is the kind of plot you make for yourself, not something you put in a report
# 
# In **panel b**, I excluded stays over one year - I chose the cut-off value of 1-year arbitrarily. However, I can see from panel b that no values even approach 1 year, so I am happy with my choice of cut-off retained all real values of length of stay and removed the outliers

# ### Use a 'standard' cut-off
# 
# Sometimes it's not so clear where the boundary is between real data and outliers.
# 
# In this case, researchers sometimes define outliers as those lying more than 3 standard deviations from the mean.
# 
# * Under the normal distribution, values 3 standard deviations from the mean occur about 1/1000 of the time so the 3xSD cut-off should exclude relatively few real values
# * If your data are not Normally distributed, this cutoff may be less suitable. 
# * Don't worry if you don't know what normal distribution is yet - this will make sense when you come back and revise!
# 
# 
# We can calculate the 3SD cutoff for <tt>CHARGES</tt>:

# In[6]:


m = hospital.CHARGES.mean()
s = hospital.CHARGES.std()

cutoff = [m-3*s, m+3*s]

display(cutoff)


# In[7]:


# re-plot the hisptogram so we can see where the 3SD cut-off falls
sns.histplot(data=hospital, x='CHARGES')
plt.show()


# By this criterion, charges below -9800 dollars and above 30000 are considered outliers.
# 
# * These are not good cut-off values!
#     * Looking again at the histogram of CHARGES above, 30001 dollars seems no less plausible than 29999
#     * -9800 dollars is an impossible value so wouldn't exclude any cases anyway!
# 
# The 3SD approach didn't work so well in this case because the data distribution is very skewed, so high positive values are actually quite plausible, whilst the natural cut-off value for low <tt>CHARGES<tt> (zero dollars) is not so far from the mean.

# ## Dealing with outliers
# 
# Once you have found outliers, you will want to neutralize the in some way.
# 
# You have about three options. Most often, the first option is best.
# 
# * Replace the bad values with a dummy value (such as `NaN`)
#     - This retains as much information as possible
# *  Replace the whole record (row of the dataframe) with a dummy value (such as `NaN`)
#     - Useful if the bad value for one variable casts doubt on the data quality for the whole record, or for soe reason you need to retain only complete records
#    
# * Delete the whole record (row of the dataframe)
#     - Generally not recommended as could be seen as dishonest (see below)
#     - Exception would be obvious duplicate records or completely blank records
# 
# 
# ### Replace only the bad values
# 
# - `df.loc[row_index, column_index] = np.nan()`
# 
# In most cases the best option is to replace only the bad values, retaining the rest of the record.
# 
# We will replace the values with `NaN` - 'not a number' which is a dummy value that will be ignored by most Python functions (for example, if we calculate the mean of a column containing NaNs, Pandas just calculates the mean of all the non-NaN values)
# 
# ### Replace a dummy value with `df.replace()`
# 
# If all the bad datapoints have the same value, for example <tt>9999<tt>, we can easily replace them as follows: 

# In[8]:


hospital.LOS.replace(9999,np.NaN, inplace=True) # note inplace=True to edit the original dataframe
hospital.AGE.replace(9999,np.NaN, inplace=True) # note inplace=True to edit the original dataframe

# check they have gone - max values for LOS and AGE should no longer be 9999
hospital.describe()


# In[9]:


To do this we unfortunately have to use different syntax from our regular indexing, as we are *setting* values in the dataframe. We use the function `df.loc`.

#### Step 1: find the rows with long cars

First let's use `df.loc[]` to find the rows where length is greater than for a normal car (looking at the dataframe above, I chose a cut-off of 8 meters).


# In[34]:


# pull out the rows where length exceeds 8 meters
cars.loc[cars.length > 8]


# #### Step 2: Select only the relevant column
# 
# Now we want to pull out only the column <tt>length</tt>, as we only want to overwrite the length values with `NaN`, retaining the heights and widths
# 
# We add a column index to `df.loc[]`:

# In[7]:


# pull out the rows where length exceeds 8 meters
cars.loc[cars.length > 8, 'length']


# In[8]:


#### Step 3: Replace the values with `NaN`

Finally we replace the offending values with NaN:


# In[ ]:


cars.loc[cars.length > 8, 'length'] = np.nan


# * **note** that we need to use a `numpy` function, `np.nan` to create the NaN values
# 
# Let's check that the bad values have been replaced, by viewing the end of our dataframe

# In[ ]:


cars.sort_values(by = 'length').tail(n=10)


# * **note** If you don't see any `NaN` values, try using `df.head()` instead of `df.tail()` - depending on your Python installation, the defaults could be set such that NaNs appear at the top of the dataframe rather than the bottom.

# #### Exercises
# 
# Try the following quick exercises:

# In[ ]:


# find out what car height constitutes an outlier by sorting the dataframe by height


# In[ ]:


# replace values of 'height' greater than 3 meters by NaN 


# ### Replace the entire row by `NaN`
# 
# First, let's reload the dataset with outliers 

# In[ ]:


cars = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/cars_outlier1.csv')


# Sometimes, you might want to remove the whole record - for example, in the cars dataset, the vehicles with outlier lengths were evidently not cars at all (they were trucks)
# 
# You can replace the entire row with NaNs by simply not specifying a column index for `df.loc[]`:

# In[ ]:


# pull out the rows where length exceeds 8 meters
cars.loc[cars.length > 8]


# Now we replace those entire rows with `NaN`

# In[ ]:


cars.loc[cars.length > 8] = np.nan


# Finally let's check it worked:

# In[ ]:


cars.sort_values(by = 'length')


# * **note** all the values in the offending rows are now NaN, instead of just the value for <tt>length</tt> as previously
# 
# ### Drop the record entirely
# 
# In some cases you may wish to actually remove the rows from a dataframe. This should be treated with caution (see below).
# 
# In the caase of the cars dataset, since the outlier vehicles were not actually cars, they probably could just be cut right out.
# 
# The easiest way to do this is actually to create a new dataframe with only the values you want to keep:

# In[ ]:


# reload the data with outliers back in!
cars = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/cars_outlier1.csv')


# In[ ]:


# create a new dataframe with only cars less than 8m long
cars_clean = cars.loc[cars.length<8] # note the sign is now < rather than >


# In[ ]:


# check that the trucks are gone
cars_clean.sort_values(by = 'length')


# * **note** - this dataframe has 981 rows, whilst the original dataframe had 983 - this proves taht the two offending rows were removed completely

# In[ ]:



