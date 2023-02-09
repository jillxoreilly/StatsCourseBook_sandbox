#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# ### Load data file

# In[2]:


wb = pandas.read_csv('data/wellbeingSample.csv')
wb


# # bootstrap confidence interval for $r$

# In[3]:


# my best effort in Python - horribly clunky!

nReps=10000
c=np.empty(nReps)
n=len(wb[wb['College']=='Lonsdale'])
print('n = ' + str(n))

# how we got correlation before (already clunky!)
print('r = ' + str(wb[wb['College']=='Lonsdale']['Score_preVac'].corr(wb[wb['College']=='Lonsdale']['Score_postVac'])))
    # convert to a numpy array)
    # convert to a numpy array

for i in range(nReps):
    # first grab just the data values from Lonsdale 
    bitWeNeed = wb[wb['College']=='Lonsdale'][['Score_preVac','Score_postVac']]
    # convert to a numpy array
    data = bitWeNeed.to_numpy()
    # bootstrap selection of rows
    ix= np.random.choice(range(n),n,replace=True)
    # bootstrap sample
    sample = data[ix]
    # bootstrp correlation
    tmp=np.corrcoef(sample[:,0],sample[:,1])
    c[i]=tmp[0,1]

sns.histplot(c)
plt.show()


# How I would do that in MATLAB (not clunky!):
# 
# 
# 
# <tt>
#     
# [data is a matrix 122x2 (columns are wb scores pre and post vac)]
# 
# for i=1:nReps
#     
#     ix= randi([1,122],122,1) # 122x1 vector of random integers between 1 and 122 (with replacement)
#     
#     c(i)=corr(data(ix,1),data(ix,2))
#     
# end
# 
# hist(c)
# </tt>

# In[ ]:





# # For comparison
# 
# It all works the way I wanted for a bootstrapped sampling dist of difference of means - the difference is that for the correlation I need to randomly select *pairs* of values from the df

# In[4]:



nReps=10000
mDiff=np.empty(nReps)
nLonsdale=len(wb[wb['College']=='Lonsdale'])
nBeaufort=len(wb[wb['College']=='Lonsdale'])
print('n = ' + str(n))

for i in range(nReps):
    sampleLonsdale = np.random.choice(wb[wb['College']=='Lonsdale']['Score_preVac'], n, replace=True)
    sampleBeaufort = np.random.choice(wb[wb['College']=='Beaufort']['Score_preVac'], n, replace=True)
    mDiff[i] = sampleLonsdale.mean()-sampleBeaufort.mean()
    
sns.histplot(mDiff,bins=np.arange(-8.05,4.05,0.1))


# In[5]:


# my best effort in Python - horribly clunky!

nReps=10000
c=np.empty(nReps)
n=len(wb[wb['College']=='Lonsdale'])
print('n = ' + str(n))

# how we got correlation before (already clunky!)
print('r = ' + str(wb[wb['College']=='Lonsdale']['Score_preVac'].corr(wb[wb['College']=='Lonsdale']['Score_postVac'])))
    # convert to a numpy array)
    # convert to a numpy array

for i in range(nReps):
    sample= np.random.Generator.choice(wb[wb['College']=='Lonsdale'][['Score_preVac','Score_postVac']],n,replace=True)
    tmp=np.corrcoef(sample[:,0],sample[:,1])
    c[i]=tmp[0,1]

sns.histplot(c)
plt.show()


# In[ ]:




