#!/usr/bin/env python
# coding: utf-8

# # Rolling a virtual dice I
# 
# <img src="https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/images/dice.jpg" width=15% alt="(display image of dice)" >
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


# ## Simulated dice roll
# 
# We are going to get the computer to roll a 'virtual' dice. We call this a data simulation. 
# 
# Data simulations are useful for getting a sense of how likely different outcomes are. 
# 
# Of course, in the sense of a simple dice roll you can work out the probability of different outcomes using an equation, but many data generating processes (that is - systems that generate data) are sufficiently complex that a computer based simulation is necessary.
# 
# For example weather forecasts, predictions of disease spread and economic forecasts all use data simulations.
# 
# 
# Let's start simple...
# 
# ## Simulation of a single dice roll
# 
# Of course, the computer does not really roll the dice. 
# 
# It does something mathematically equivalent, that is generate a random integer (whole number) between 1 and 6.

# In[2]:


np.random.randint(1,7)


# What happened there?
# 
# We used numpy's random number generator (<tt>numpy.random</tt>), which can generate all sorts of random numbers. 
# 
# In this case we told it to give us an integer in the range [1,7) 
# 
# The syntax here is a little surprising: <tt>randint(1,7)</tt> means "greater than or including 1" and "less than but NOT including 7". In other words <tt>randint(1,7)</tt>  returns 1,2,3,4,5 or 6 (but NOT 7)
# <br>
# <br>
# 
# 
# <div style = "    padding-top: 10px;
#     padding-bottom: 10px;
#     padding-left: 10px;
#     padding-right: 10px;
#     box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
#     vertical-align: middle;">
#     
# This may seem a little unusual - you might have expected to see <tt>randint(1,6)</tt> instead.
#     
# In Python when we specify ranges they always include the lower bound but not the upper bound. 
#     
# A real world example would be if a sign at a ticket booth said "junior ticket (children over 1 and under 7) £3" - 
#     <ul>
#     <li>a child on their first birthday needs the junior ticket
#     <li>a child of 6 years 364 days can buy the junior ticket 
#     <li>a child on their 7th birthday cannot buy the junior ticket, 
#     </ul>
# The range of ages for the £3 junior ticket is [1,7)
# 
# </div>
# 
# <br>
# Try running the code block several times - you should get a different number on your 'dice' each time
# 
# 
# Now we can ask <tt>numpy.random </tt> to give us lots of random integers (simulated dice rolls) as follows:
#     
# 

# In[3]:


np.random.randint(1,7,10)


# Now we got a numpy array with 10 random numbers in it.
# 
# <ul>
# <li> Can you work out how to change the code to get 12 "dice rolls"?
# <li> Can you change the code to simulate rolling a 16-sided dice?
# </ul>
# 
# <img src="images/polyhedral_dice.jpg" width=30% alt="(display image of dice)" >

# ## Simulation of rolling two dice
# 
# In some games, players roll two dice and add the scores on both dice together.
# 
# Let's simulate rolling two dice and adding the scores together:
# 

# In[4]:


d1 = np.random.randint(1,7)
d2 = np.random.randint(1,7)

dSum = d1+d2

print(dSum)


# What happened there? 
# 
# We simulated a dice roll by getting a random integer between 1 and 6 as before, but then we saved the outcome to a variable called d1 (short for "dice 1")
# Then we did the same thin again and saved the result to a variable called d2 (short for "dice 2")
# 
# Then we added d1 and d2 together

# You may have come across the idea that with two dice, some scores are more frequent than others as there are more ways of making them from the scores on the individual dice. There is only one way of getting a 12, but six ways of getting a 7:
# 
# <img src="images/dice2x2.jpg" width=30% alt="(display image of dice)" >
# 
# Let's simulate rolling two dice lots of times using a <tt>for</tt> loop and plot the frequency of different overall scores:

# In[5]:


dSum = np.empty(20)

for i in range(20):
    d1 = np.random.randint(1,7)
    d2 = np.random.randint(1,7)
    
    dSum[i] = d1+d2

# count up how many of each individual score there are
scores, counts = np.unique(dSum, return_counts=True)

print('scores on individual trials: ' + str(dSum))
print('possible scores: ' + str(scores))
print('frequency: ' + str(counts))


# OK, now let's simulate a really large number of trials and plot the frequency of getting each score on a bar plot

# In[6]:


dSum = np.empty(60000)

for i in range(60000):
    d1 = np.random.randint(1,7)
    d2 = np.random.randint(1,7)
    
    dSum[i] = d1+d2

# count up how many of each individual score there are
scores, counts = np.unique(dSum, return_counts=True)

# plot them
plt.bar(scores, height=counts)
plt.xlabel('score')
plt.ylabel('frequency')
plt.show()


# ## Exercise: rolling 3 or more dice
# 
# Can you edit the code block to simulate the scores for 3 dice? 
# What about 10 dice?

# In[7]:


dSum = np.empty(60000)

for i in range(60000):
    d1 = np.random.randint(1,7)
    d2 = np.random.randint(1,7)
    d3 = .....
    
    dSum[i] = d1+d2+ ......

# count up how many of each individual score there are
scores, counts = np.unique(dSum, return_counts=True)

# plot them
plt.bar(scores, height=counts)
plt.xlabel('score')
plt.ylabel('frequency')
plt.show()

