#!/usr/bin/env python
# coding: utf-8

# # Movie data
# 
# The file 'MovieProfits.csv' contains data on 609 movies from the years 2008-2012, from the website rottentomatoes.com
# 
# 
# For each Movie we have some information including: 
# <ul>
#     <li> The gross box office turnover (US Gross) in millions of dollars
#     <li> The budget for making the movie, in millions of dollars
#     <li> The duration or run time of the movie
#     <li> The critics' score out of 100%
# </ul>
# 
# You will complete a series of data analysis tasks as instructed in the questions below.
# 
# You will receive an overall grade from your tutor.
# 
# Each question-part carries roughly equal weight.
# 
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
sns.set_style('whitegrid')


# ### Import and view the data

# In[2]:


movies=pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/MovieProfits.csv')
movies


# #### a) Find and remove outliers
# 
# There are some erroneous values in the columns 'Year' and 'Run Time (min)'. 
# <ul>
#     <li>Find these and replace them with NaNs.
#     <li>Briefly justify (in the text box below) which values you considered erroneous
# </ul>

# In[3]:


# Your code here to replace erroenous values with NaNs
# No need to show your working


# [ your comments here]

# #### b) Plot the relationship between Budget and Gross Turnover
# 
# <ul>
#     <li> Create a scatterplot showing the relationship between Budget and Gross Turnover
#     <li> Add the line x=y so we can see which movies made a profit and which made a loss
# </ul>

# In[4]:


# make a scatterplot

# add the line x=y so we can see which movies made a profit and which made a loss


# #### c) Comment on the plot made in (b)
# <ul>
#     <li> Do movies with a higher budget have a higher gross turnover?
#     <li> Do all movies make a profit or do some make a loss?
#     <li> Comment on anything else you notice about the data distribution
# </ul>
# Support your answer with descriptive statistics where appropriate

# In[5]:


# supporting calculations


# [ your comments here ]

# #### d) Is there a correlation between Budget and Gross Turnover?
# 
# <ul>
# <li>Calculate the correlation coefficient
# <li>Briefly justify your choice of correlation method
# </ul>

# In[6]:


# your code here for the correlation


# [ your comments here]

# #### e) Add a column to the dataframe for 'Profit ($M)'
#  ... Where profit is defined as Gross Turnover minus Budget

# In[7]:


# Your code here to add the column ['Profit ($M)']

# Display the dataframe with the new column included


# #### f) What is the relationship between Budget and Profit
# 
# <ul>
# <li> Create a scatterplot for Budget vs Profit
# <li> Calculate the correlation between Budget and Profit using both Pearson's and Spearman's correlation coefficient. 
#     <ul> 
#         <li>Comment on the difference in results and why it might occur
#         <li> Which approach is more appropriate and why?
#     </ul>
# </ul>

# In[8]:


# Your code here for the scatterplot


# In[9]:


# Your code here for the correlations


# [ your comments here ]

# #### g) Add a column containing Profit per $ of budget
# 
# This should be defined as Profit/Budget

# In[10]:


# Your code here to add the column ['Profit ($M)']


# #### i) Plot histograms of profit per dollar budget
# 
# Create three histograms containing the distribution of profit per dollar budget for:
# <ul>
# <li> All movies
# <li> Movies with a budget below \$50M
# <li> Movies with a budget above \$100M
# </ul>
# Make them as three subplots in a single figure to keep things tidy

# In[11]:


plt.figure(figsize=[15,5]) # set figure size

# Your code here



# #### j) 95% confidence interval for the mean profit per dollar
# 
# Create a bootstrapped confidence interval for the mean profit per dollar, separately for 
# <ul>
#     <li> Movies with a budget below \$50M
#     <li> Movies with a budget above \$100M
# </ul>

# In[12]:


#### Your code here for the 95% confidence interval: Movies with a budget below $50M 
nReps = 10000
m = # your code here
n = # your code here

for i in range(nReps):
    sample=# your code here
    m[i]=# your code here
    
print('95% CI: [' + str(np.quantile(m, 0.025)) + ',' + str(np.quantile(m, 0.975)) + ']')


# In[52]:


#### Your code here for the 95% confidence interval: Movies with a budget above $100M 
nReps = 10000
m = # your code here
n = # your code here

for i in range(nReps):
    sample=# your code here
    m[i]=# your code here
    
print('95% CI: [' + str(np.quantile(m, 0.025)) + ',' + str(np.quantile(m, 0.975)) + ']')


# #### k) Comment on the confidence intervals obtained in the previous question.
# 
# The mean is also called the expected value - so the mean profit per dollar is also the expected profit per dollar (if we were to make a new movie). 
# 
# <ul>
# <li>Is the expected profit per dollar higher for low- or high- budget movies?
# <li>Is the expected profit per dollar more uncertain/variable for low- or high- budget movies?
# </ul>

# [ your comment here ]

# In[ ]:




