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


# [ your text here to summarize which values were considered erroneous ]

# #### b) Plot the relationship between Budget and Gross Turnover
# 
# <ul>
#     <li> Create a scatterplot showing the relationship between Budget and Gross Turnover
#     <li> Add the line x=y so we can see which movies made a profit and which made a loss
# </ul>

# In[4]:


# make a scatterplot
sns.scatterplot(data=movies, x='Budget ($M)', y='US Gross ($M)', alpha=0.5)

# add the line x=y so we can see which movies made a profit and which made a loss
plt.plot([0,250],[0,250],'r')


# #### c) Comment on the plot made in (b)
# <ul>
#     <li> Do movies with a higher budget make a higher profit?
#     <li> Do all movies make a profit or do some make a loss?
#     <li> Comment on anything else you notice about the data distribution
# </ul>

# [your answer here]

# #### d) Is there a correlation between Budget and Gross Turnover?
# 
# <ul>
# <li>Calculate the correlation coefficient
# <li>Briefly justify your choice of correlation method
# </ul>

# In[5]:


# your code here for the correlation


# [Your text here to justify correlation method]

# #### e) Add a column to the dataframe for 'Profit ($M)'
#  ... Where profit is defined as Gross Turnover minus Budget

# In[6]:


# Your code here to add the column ['Profit ($M)']
movies['Profit ($M)']=movies['US Gross ($M)']-movies['Budget ($M)']

# Display the dataframe with the new column included
movies


# #### f) Plot the distributions of Budget, Gross Turnover and Profit
# 
# <ul>
# <li>Create three histograms showing the distributions of Budget, Gross Turnover and Profit
# <li>Make them as subplots in a single figure to keep things tidy
# <li>Comment on the distribution of each variable, including some descriptive statistics
# </ul>

# In[7]:


plt.figure(figsize=[15,5])

plt.subplot(1,3,1)
sns.histplot(data=movies, x='US Gross ($M)')

plt.subplot(1,3,2)
sns.histplot(data=movies, x='Budget ($M)')

plt.subplot(1,3,3)
sns.histplot(data=movies, x='Profit ($M)')

plt.tight_layout()


# [ your comments here on the distriution of each variable]

# In[8]:


# Your code here to obtain the relevant descriptive statistics
# remember to include comments (beginning with #) or print statements so that the reader can follow what you did


# #### g) What is the relationship between Budget and Profit
# 
# <ul>
# <li> Create a scatterplot for Budget vs Profit
# <li> Calculate the correlation between Budget and Profit using both Pearson's and Spearman's correlation coefficient. 
#     <ul> 
#         <li>Comment on the difference in results and why it might occur
#         <li> Which approach is more appropriate and why?
#     </ul>
# </ul>

# In[9]:


# Your code here for the scatterplot
sns.scatterplot(data=movies, x='Budget ($M)', y='Profit ($M)', alpha=0.5)


# In[10]:


# Your code here for the correlations
print("Spearman's r")
movies['Budget ($M)'].corr(movies['Profit ($M)'], method='spearman')

print("Pearson's r")
movies['Budget ($M)'].corr(movies['Profit ($M)'], method='pearson')


# [your comments here]

# #### h) Add a column containing Profit per $ of budget
# 
# This should be defined as Profit/Budget

# In[11]:


# Your code here to add the column ['Profit ($M)']
movies['Profit per $']=movies['Profit ($M)']/movies['Budget ($M)']


# #### i) Plot histograms of profit per dollar budget
# 
# Create three histograms containing the distribution of profit per dollar budget for:
# <ul>
# <li> All movies
# <li> Movies with a budget below \$50M
# <li> Movies with a budget above \$100M
# </ul>

# #### j) 95% confidence interval for the mean profit per dollar
# 
# Create a bootstrapped confidence interval for the mean profit per dollar, separately for 
# <ul>
#     <li> Movies with a budget below \$50M
#     <li> Movies with a budget above \$100M
# </ul>

# In[12]:


#### Your code here for the 95% confidence interval: Movies with a budget below $50M 


# In[13]:


#### Your code here for the 95% confidence interval: Movies with a budget abobve $100M 


# #### k) Comment on the confidence intervals obtained in the previous question.

# [ your answer here ]

# In[ ]:




