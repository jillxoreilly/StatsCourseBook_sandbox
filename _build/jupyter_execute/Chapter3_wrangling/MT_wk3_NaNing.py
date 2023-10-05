#!/usr/bin/env python
# coding: utf-8

# # Neutralizing bad datapoints
# 
# Once you have found dummy values (such as 9999), bad datapoints or outliers, you will want to neutralize the in some way.
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
# You will need to download the file heartAttack.csv from Canvas to your computer, then import it

# In[2]:


hospital=pd.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(hospital)


# ## Replace only the bad values
# 
# - `df.replace(old_value, new_value, inplace=True)`
# - `df.loc[row_index, column_index] = new_value`
# 
# In most cases the best option is to replace only the bad values, retaining the rest of the record.
# 
# We will replace the values with `NaN` - 'not a number' which is a dummy value that will be ignored by most Python functions (for example, if we calculate the mean of a column containing NaNs, Pandas just calculates the mean of all the non-NaN values)
# 
# ### Replace a dummy value with `df.replace()`
# 
# If all the bad datapoints have the same value, for example <tt>9999<tt>, we can easily replace them as follows: 

# In[3]:


hospital.LOS.replace(9999,np.NaN, inplace=True) # note inplace=True to edit the original dataframe
hospital.AGE.replace(9999,np.NaN, inplace=True) # note inplace=True to edit the original dataframe

# check they have gone - max values for LOS and AGE should no longer be 9999
hospital.describe()


# ### Replace values over a cutoff with df.loc[]
# 
# In some cases we want to replace a range of values; say for example we decided to remove charges over 30000 dollars.
# 
# To do this we unfortunately have to use different syntax from our regular indexing with `df.query()`, as we are *setting* values in the dataframe. We use the function `df.loc[]` which accesses specific *locations* in the dataframe defined by row and column numbers.
# 
# Say if I wanted to replace the value of <tt>SEX<tt> in the first row to <tt>'bananas'<tt> (!):

# In[4]:


hospital.loc[0,'SEX']='bananas' # remember row zero is the first row in Python!
hospital.head() # check it worked


# Now, instead of giving a row number, I can use a criterion (<tt>hospital.CHARGES > 30000<tt>) to find the rows I want to edit:

# In[5]:


hospital.loc[(hospital.CHARGES > 30000),'CHARGES']=np.nan # remember row zero is the first row in Python!
hospital.describe() # check it worked


# * **Note** the maximum value of CHARGES should now be 30000 dollars

# ### Replace the whole record
# 
# Occasionally we decide a whole record or row of the data table (often corresponding to an individual) should be replaced with `NaN`.
# 
# Some situations in which we would replace the whole record with `NaN` would be:
# 
# * We realise after the fact that a participant didn't meet includion criteria for our study - for example, we are studying unmedicated patients witha  certain condition, and they disclosed after data collection that they are already on medication
# * They have bad values for several variables
# * we wish to only retain records that are complete
# 
# We can replace the whole record with `NaN` using `df.loc[]` and simply not specifying a column. For example, let's make the whole second row of the dataframe become `NaN`

# In[6]:


hospital.loc[1] = np.nan # remember we count from zero in Python so second row = row 1 !
hospital.head() # check it worked


# Or say we want to replace the whole record for anyone with <tt>CHARGES</tt> under 100 dollars with `NaN`:

# In[7]:


hospital.loc[(hospital.CHARGES<100)] = np.nan # remember we count from zero in Python so second row = row 1 !
hospital.describe() # check it worked - mmin charge should now be >= $100


# ### Drop the record from the dataframe
# 
# * `df.drop(row_index)`
# 
# **Generally not recommended** - in general we replace missing data with `NaN` so that it is transparent how many bad datapoints were collected. 
# 
# Imagine if we conducted a survey including a question "have you ever committed a crime". Perhaps some people would not answer this question (mmaybe momre likely if the answer is 'yes'). 
# 
# If we deleted all the records for people who skipped the question, this could be misleading.
# 
# **However** sometimes we need to just remove rows. An example would be if a pile of forms were automatically scanned, and it turned out a lot of the were completely blank (spare forms). We would want to delete the records corresponding to those spare forms.
# 
# Another example would be if a record was an exact duplicate of another.
# 
# To remove records (rows) we use `df.drop()`. 
# 
# For example, perhaps we want to remove row 0 (the first row), as we this it is a prank entry (<tt>SEX == 'bananas'</tt>):

# In[8]:


hospital.drop(0, inplace=True)
hospital # check it's gone


# In[ ]:




