#!/usr/bin/env python
# coding: utf-8

# # Sampling with and without replacement
# 
# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries
# 

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# ### Toy example
# 
# Let's explore the idea of sampling with and without replacement using a very simple example (a simple example designed just to illustrate a point is sometimes called a <i>toy example</i>)
# 
# Say I have a dataset listing four children's pets:
# 
# [cat, dog, cat, rabbit]
# 
# If I sample from this dataset, I get a new list of pets. Say I draw a sample of size $𝑛=2$, my sample might be [cat, cat] (if I'm lucky- I love cats!)
# 
# 
# #### Without replacement
# 
# If I sample without replacement, after I have 'drawn' my first sample pet fromt the original dataset, I cannot draw it again - my next sample pet will be drawn from the remaining three. The consequence of this is that all samples of size 𝑛=4 contain all of the original 4 pets, albeit in a different order
# 
# [cat, cat, dog, rabbit]
# 
# [rabbit, cat, dog, cat]
# 
# [cat, dog, rabbit, cat]
# 
# etc
# 
# #### With replacement
# 
# If I sample with replacement, each 'draw' can be any of the four animals (think of it like pulling a card from a deck, checking which animal is on it, and then replacing the card in the deck before the next sample is drawn).
# 
# So I could get:
# 
# [cat, cat, cat, cat]
# 
# if I'm really lucky!
# 
# or more likely:
# 
# [cat, dog, cat, cat]
# 
# [rabbit, dog, cat, rabbit]
# 
# ... etc
# 
# Let's try it, replacing the animals with numbers: dog = 1, cat = 2, rabbit = 3

# In[2]:


# Sampling without replacement
data = [2,1,3,2]
nReps= 10

for i in range(nReps):
    sample = np.random.choice(data,4,replace=False)
    print('sample ' + str(i) + ' = ' + str(sample))


# When sampling without replacement each sample should be identical in contents (albeit in a random order) - this is clearer if I sort the sample values in ascending order:

# In[3]:


# Sampling without replacement
data = [2,1,3,2]
nReps= 10

for i in range(nReps):
    sample = np.random.choice(data,4,replace=False)
    print('sample ' + str(i) + ' = ' + str(np.sort(sample)))


# <ul>
#     <li>Can you change the code above to sample <i>with</i> replacement?
#     <li>In your samples drawn with replacement, look for those which are not simply permutations of the original four datapoints (animals) but contain more or fewer cats/dogs/rabbits than expected
# </ul>

# ### Real world examples
# 
# A real world example of sampling without replacement would be if we give 100 students a wellbeing questionairre - each student in our sample is a member of the parent distribution (all students/ allstudents in the college we were sampling from etc). We will only want to survey each student once.
# 
# A real world of example of sampling with replacement is rolling a dice. Each diceroll yeilds an outcome (1-6) that is a sample from an infinite selection of possible outcomes (think of it as drawing a card from an 
