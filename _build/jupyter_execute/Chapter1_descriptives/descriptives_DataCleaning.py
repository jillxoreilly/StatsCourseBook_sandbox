#!/usr/bin/env python
# coding: utf-8

# # Data cleaning
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


# ## Removing an outlier
# 
# In some cases, we can identify that an outlier datapoint should not be in our dataset, and remove it.
# 
# Let's try an example:
# 
# ### Import the data
# 
# Let's import a dataframe with size information on a random sample of cars
# 
# 

# In[2]:


cars = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/cars_outlier1.csv')
display(cars)


# ### Get descriptives
# 
# We can get the descriptive statistics using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html"><tt>decribe()</tt></a> method in <tt>pandas</tt>

# In[3]:


cars.describe()


# Hm, the maximum value for car length looks very high.
# 
# Let's plot the data (don't worry about the plotting code, there is a session on this later)

# In[4]:


sns.histplot(cars['length'])


# There must be a cars of length up to 15.36m (the max length in the descriptives table) but we can't see them in the plot - although we can see the x axis is stretched out to accommodate them.
# 
# Let's zoom in a bit:

# In[5]:


plt.subplot(1,2,1)
sns.histplot(cars['length'])

plt.subplot(1,2,2)
sns.histplot(cars['length'])
plt.ylim((0,10))

plt.subplots_adjust(wspace = 0.5)


# Hm, a couple of outliers.
# 
# Let's check it in the dataframe by pulling out any cars longer than 8m:

# In[6]:


cars[cars['length']>8]


# ahh, the value of <tt>type</tt> for the two vehicles that exceed 8m is 'truck'. 
# 
# Let's check what other types we have:

# In[7]:


cars['type'].value_counts()


# Hm, 981 cars and 2 trucks. I think the trucks were included by mistake. Let's drop them:

# In[8]:


cars_clean = cars.drop([100,101]) # 100 is the row index of the truck - you can see it above
cars_clean['type'].value_counts() # check if we still have any trucks in the sample


# We got the row indices for the trucks from the cell above where we pulled out rows with length >8m and inspected it. 
# 
# if you were working with lots of files, it could be useful to cut out the middle man and find the row index using code:

# In[9]:


ix = cars.index[cars['type']=='truck'] # find the row index for the truck and save it as 'ix'
cars_clean = cars.drop(ix)
cars_clean['type'].value_counts() # check if we still have any trucks in the sample


# ## NaN an outlier value
# 
# Sometimes, we don't want to remove an entire entry.
# 
# Say for example there is a data entry error for one of the vehicle heights. We might not be that interested in vehicle height, and wish to retain other data on this vehicle.
# 
# Then we can replace just the offending value with the value <tt>NaN</tt>
# 
# <tt>NaN</tt> stands for Not a Number and is code across many programming languages for a missing value that should be ignored.
# 
# Let's try an example
# 
# ### Import the data
# 
# Let's import a dataframe with size information on a random sample of cars

# In[10]:


cars = # your code here to read the file 'https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/cars_outlier2.csv'
display(cars)


# ### Get descriptives
# 
# We can get the descriptive statistics using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html"><tt>decribe()</tt></a> method in <tt>pandas</tt>

# In[ ]:


# your code here to get the descriptives - check above for an example!


# It looks like there are some very high cars in the sample, but the maximum length and width are as expected.
# 
# Let's have a look at the rows of the dataframe containing the very high cars

# In[ ]:


# your code here to display the rows of the dataframe with car height greater than 8m
# check above for an example


# Hm, these height values appear to be about 10x the mean height
# 
# Maybe a data entry error (the decimal point is in the wrong place)
# 
# We can replace the values with a <tt>NaN</tt>

# In[ ]:


cars_clean = cars # make a copy of the dataframe to work on

cars_clean.loc[[100,101],['height']]=np.nan
# or cut out the middle man and find the offending row numbers using code
#cars.loc[(cars['height']>8),['height']]=np.nan

# let's view the edited dataframe
display(cars_clean[98:105])


# We can see that the mean and max height should now have gone back to reasonable values, as Python just ignores the NaNs when calculating the descriptive statistics:

# In[ ]:


cars_clean.describe()


# ### Find NaNs
# 
# If you download a dataset, it can be useful to check which rows have missing values. 
# 
# You can do this using the method <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html"><tt>isna</tt></a>, which returns a True for NaN values and False elsewhere.
# 
# For example we can check the section of the dataframe where we replaced some values with <tt>NaN</tt>s

# In[ ]:


cars_clean[98:105].isna()


# If you want to find the rows in which 'height' is <tt>NaN</tt>, you can use isna() to give indices like this:

# In[ ]:


cars_clean[cars_clean['height'].isna()]


# ## Delete or <tt>NaN</tt>?
# 
# When should you delete the entire row and when should you replace a missing value with a <tt>NaN</tt>?
# 
# In general, it is better to replace bad or missing values with a <tt>NaN</tt>
# 
# I think there are three main considerations:
# 
# ### Partial data records are valuable
# 
# If you have many data values for each record or row in your dataframe (in this case, records correspond to individual cars, but they could be patients for example), you may not wish ot junk all the data just because some variables are incomplete or have bad values. 
# 
# For example, say we run a study which involves a hospital visit for a battery of tests (blood pressure, thyroid function, levels of vitamin B12...) and the lab looses a batch of samples for the B12 analysis. The remaining data on the patients may still be useful - maybe we didn't even care that much about vitamin B12.
# 
# In this case, it is better to put a missing value for B12 in the affected patients and retain the rest of their data as normal.
# 
# ### Deleting data could be misleaading
# 
# Say one of the measures in our patient study is a follow-up questionairre and only 60% of patients complete this.
# 
# If we simply delete all the patients who didn't complete the follow-up from our database, we will have a biased sample (an no-one will ever know!)
# 
# For this reason it is good practice to retain incomplete data records, with <tt>Nan</tt>s as appropriate, so another researcher can see the full picture.
# 
# ### Some errors really are errors
# 
# However, if a record is clearly an error (completely empty) or a duplicate (two identical files for the same NHS number), it would be appropriate to delete it

# In[21]:


cars.loc[:,['height', 'length']].corr()


# In[26]:


cars.height.corr(cars.length)


# In[ ]:




