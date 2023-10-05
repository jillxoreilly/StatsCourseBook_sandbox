#!/usr/bin/env python
# coding: utf-8

# ## Sort out `scipy.stats` version
# 
# This section is for those running Python on their own computers. 
# 
# If you are using Colab, please follow the instruvctions in each notebook.
# 
# This week we use a function `scipy.stats.permutation_test()`
# 
# You need scipy stats version > 1.8.0 to run this. 
# 
# You should check your version by running the following code block.

# In[1]:


import scipy as scipy
scipy.version.version


# If the reported version is less than 1.8.0 you need to update it -
# 
# First you can see if running this code block helps (the output of the code cell is should be the new version number 1.9.3, but it may throw an error on your computer):

# In[2]:


get_ipython().system('pip install scipy==1.9.3')
import scipy as scipy
scipy.version.version


# If your version is still <1.8.0 after running that, especially if you are on Windows, or you have an error message, you can try the following:

# In[3]:


get_ipython().system('pip3 install scipy==1.9.3')
import scipy as scipy
scipy.version.version


# If that still didn't work try:
# 
# Mac: open a terminal (Applications--Utilities--Terminal) and type:
# <tt> conda install -c conda-forge scipy=1.10.0 </tt>
# or if that fails,
# <tt> conda update scipy </tt>
#                       
# Windows: open an Anaconda terminal (spotlight search for anaconda and select the anaconda terminal app) and type:
# <tt> conda install -c conda-forge scipy=1.10.0 </tt>
# or if that fails,
# <tt> conda update scipy </tt>
#                       
# Please try and do this before the tutorial - otherwise your tutor will know you didn't read the prep work thoroughly ;-)

# In[ ]:




