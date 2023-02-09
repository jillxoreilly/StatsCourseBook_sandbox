#!/usr/bin/env python
# coding: utf-8

# # Grouping data

# In many datasets, data can be categorized and we would wish to give descriptive statistics separately for each category.

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


# ### Load and view the data
# 
# <img src="images/carsBanner.png" width=100% alt="Picture of some cars" >
# 
# Let's load the datafile "vehicles.csv" which contains size data on vehicles parked at a vehicle-ferry terminal at 1pm on Sunday 24th April 2022, which they regard as a representative sample.

# In[2]:


vehicles = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourse/main/data/vehicles.csv')
display(vehicles)


# That was a long list of vehicles!
# 
# * What information do we have about each vehicle?

# ### Obtain descriptive statistics
# 
# We can use the built in functions in <tt>pandas.describe()</tt> to return descriptives for our data

# In[3]:


vehicles['length'].describe()


# ### Why group the data?

# You can see above that the mean length of vehicles in the car park is 6.72m.
# 
# This is surprising as it is rather longer than even a large family car
# 
# To get a better sense of the length data, I am going to plot them. 
# 
# Don't worry too much about the plotting code for now, as there are dedicated exercises on plotting later.

# In[4]:


sns.histplot(data=vehicles, x="length",  bins = np.arange(0,16,0.5))
plt.xlabel('vehicle length (m)')


# Interesting. It looks like there are several clusters of vehicle lengths. 
# 
# Have a look back at our dataframe - is there some information there that could explain the different clusters?
# <ul>
#     <li> Probably the clusters relate to different vehicle types
# </ul>
# 
# I can plot vehicle types in different colours (again no need ot worry about the plotting code at this stage)

# In[5]:


sns.histplot(data=vehicles, x="length", bins = np.arange(0,16,0.5), hue="type")
plt.xlabel('vehicle length (m)')


# Aha. We might want to describe our data separately for each by vehicle type.
# 
# ### Grouping into separate dataframes
# 
# One way to do this is to create separate dataframes for each vehicle type:

# In[6]:


cars = vehicles[vehicles['type']=='car']
cars.describe()


# we can see that 981 of the vehicles were cars, and their mean length was 4.198m, much shorter than the mean over all vehicles.
# 
# Try modifying the code below to get descriptive statistics for trucks:

# In[7]:


# modify the code to get descritives for trucks
cars = vehicles[vehicles['type']=='car']
cars.describe()


# ### <tt>pandas.groupby</tt>
# 
# We can also use the pandas function <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html"><tt>groupby</tt></a> to split up our dataframe according to a categorical variable, in this case vehicle type.

# In[8]:


vehicles.groupby(['type']).describe()


# Yikes, that was an unweildy table!
# 
# It may be preferable to output descriptives only for one measure (eg length):

# In[9]:


vehicles.groupby(['type'])['length'].describe()


# ... or to output one descriptive (such as the mean) at a time, rather than the whole table

# In[10]:


vehicles.groupby(['type']).mean()

