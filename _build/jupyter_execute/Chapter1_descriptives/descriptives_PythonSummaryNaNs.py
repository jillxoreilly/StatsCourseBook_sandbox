#!/usr/bin/env python
# coding: utf-8

# # Key Python functions: Missing data and NaNs
# 
# In this notebook we gather together and recap the <tt>Pandas</tt> functions we have learned this week:
# * Functions for **locating outliers**
# * Syntax for replacing missing data with **NaN**
# 
# 
# 
# As we have seen, outliers can distort the values of statistics such as the mean and standard deviation
# 
# In real datasets, outliers are common, arising from one of the following:
# 
# <ul>
#     <li> Real but unusual values (eg many basketball players are outliers in terms of height)
#     <li> Noise in a data recording system (eg in brain imaging data, noise signals from head movement are much larger than the real brain activity we are trying to record)
#     <li> Data entry error (human types the wrong number)
# </ul>
# 
# Identifying and removing outliers and bad data points is a crucial step in the process of preparing our data for analysis, sometimes called <i>data wrangling</i>
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
import pandas 
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ## Import a dataset to work with
# 
# You will need to download the file OxfordWeather.csv from Canvas to your computer, then import it

# In[2]:


cars = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/cars_outlier1.csv')
display(cars)


# ## Finding outliers
# 
# - `df.describe()`
# - `df.sort_values(by = 'columname').head()` and `df.sortvalues(by = 'columname').head()`
# 
# When working with a new dataset it is always necessary to check for missing data and outliers.
# 
# Often the best way to check for outliers is by plotting (which will be covered next week) but some of the describing data functions are also useful for this.
# 
# ### Use `df.describe()` to check min and max values are plausible
# 
# Often if there is an outlier or misrecorded data point, the outlier will be the minimum or maxiumum value in a dataset:
# 
# * If the decimal point is misplaced we get a very large (or small value) - eg a person's height could easily be misrecorded as 1765 cm (over 17 metres!) instead of 176.5 cm
# * If the wrong units are used we could get a very larg or small value - eg a person's height is recorded as 1.756 (m) when it should have been recorded as 176.5 (cm) 
# * sometimes 'dummy' values are used as placeholders for missing data - often the duymmy value is `NaN` but sometimes an obviously-wrong numerical value (such as 999) is used.
# 
# Therefore, running `df.describe()` and checking the min and max values for each datapoint is a good first step
# 
# Let's try it with our cars dataset:

# In[3]:


cars.describe()


# We can see that the max values for <tt>length</tt> (15 meters) and height (4 meters) are implausible (if you are thinking 'but how would I know how long or high a car is' - just think for a second - two metres is the height of a very tall person, do you see many cars twice that height?!). 
# 
# On the other hand, the minimum values look OK.
# 
# ### Use `df.sort_values(by = 'column')` or `df.sort_values(by = 'column').tail()` to find the offending rows in the dataframe
# 
# We now want to have a look at the records (dataframe rows) containing the outlier vehicle lengths (or heights), to try and figure out what went wrong.
# 
# If our data were in a spreadsheet like Excel, we might sort the data by the column of interest (height) and scroll to the bottom to find the largest values. 
# 
# When working with a code-based data analysis we can achieve much the same thing by sorting and then displaying the top or bottom of the sorted dataframe using `df.head()` or `df.tail()`:
# 
# #### Step 1: Sort by the column of interest
# 
# We sort by length:

# In[4]:


cars.sort_values(by = 'length')


# We can already see that there are two outliers with much higher lengths - and that they are actually trucks not cars - so that explains the problem
# 
# In some cases, we might have a lot of outliers - the default display for a dataframe shows us the first and last five entries only. So we might want to expand out view a little bit.
# 
# To show the last 10 entries use `df.tail()` (here chained together with `df.sort_values()`):

# In[5]:


cars.sort_values(by = 'length').tail(n=10)


# similarly you can use `df.head(n=20)` to show the first 20 entries (for example).

# ## Dealing with outliers
# 
# Once you have found outliers, you will want to remove them from your dataset.
# 
# ### Replace only the bad values
# 
# - `df.loc[row_index, column_index] = np.nan()`
# 
# In most cases the best option is to replace only the bad values, retaining the rest of the record.
# 
# We will replace the values with `NaN` - 'not a number' which is a dummy value that will be ignored by most Python functions (for example, if we calculate the mean of a column containing NaNs, Pandas just calculates the mean of all the non-NaN values)
# 
# To do this we unfortunately have to use different syntax from our regular indexing, as we are *setting* values in the dataframe. We use the function `df.loc`.
# 
# #### Step 1: find the rows with long cars
# 
# First let's use `df.loc[]` to find the rows where length is greater than for a normal car (looking at the dataframe above, I chose a cut-off of 8 meters).

# In[6]:


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




