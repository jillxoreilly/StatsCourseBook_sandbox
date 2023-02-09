#!/usr/bin/env python
# coding: utf-8

# # Movie data
# 
# The file 'MovieProfits.csv' contains data on 609 movies from the years 2008-2012, from the website rottentomatoes.com
# 
# Your task is to investigate and report how the factors
# 
# 
# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[1]:





# ### Import and view the data

# In[1]:


movies=pandas.read_csv('data/MovieProfits.csv')
movies


# In[10]:


sns.scatterplot(data=movies, x='Budget ($M)', y='Critic Score (Rotten Tomatoes)')


# In[8]:


movies.sort_values(by='US Gross ($M)')


# In[11]:


sns.scatterplot(data=movies, x='Budget ($M)', y='Run Time (min)')


# In[14]:


sns.violinplot(data=movies, x='Year', y='Budget ($M)')


# In[38]:


imdb=pandas.read_csv('data/imdb.csv')
movies=imdb[imdb['Type']=='Film']
movies


# In[43]:


sns.histplot(data=movies, y='Rate',x='Votes')
movies[['Date','Rate']].corr(method='spearman')


# In[33]:


sns.violinplot(data=movies, x='Alcohol', y='Rate', order=['None','Mild','Moderate','Severe'])


# In[30]:


movies


# In[44]:


sns.violinplot(data=movies, x='Certificate',y='Rate')


# In[46]:


movies['Certificate'].value_counts()


# In[47]:


TV-Y: Designed to be appropriate for all children
TV-Y7: Suitable for ages 7 and up
G: Suitable for General Audiences
TV-G: Suitable for General Audiences
PG: Parental Guidance suggested
TV-PG: Parental Guidance suggested
PG-13: Parents strongly cautioned. May be Inappropriate for ages 12 and under.
TV-14: Parents strongly cautioned. May not be suitable for ages 14 and under.
R: Restricted. May be inappropriate for ages 17 and under.
TV-MA: For Mature Audiences. May not be suitable for ages 17 and under.
NC-17: Inappropriate for ages 17 and under
E - Educational
M - Mature
TV-Y7 - suitable for children over 7


# In[50]:


movies[movies['Certificate']=='TV-14']


# In[ ]:




