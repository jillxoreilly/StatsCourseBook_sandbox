#!/usr/bin/env python
# coding: utf-8

# <html><head>
# <style>
# body {background-color: powderblue;}
# h1   {color: blue;}
# p    {color: red;}
# </style>
# </head>
# <body>

# # Simulated coin toss
# 
# To get a feel for how likely different outcomes are, we are going to <i>simulate the data generating process</i>
# 
# <img src="images/Minion_what.jpg" width=10% alt="What?!" >
# 
# Here is an example of how we could <i>simulate the data generating process</i> in real life:
# 
# To work out how likely we are to get 5 heads out of 10 coin tosses, we could...
# <ul>    
#     <li>get a real coin (but who has cash on them these days?)
#     <li>assume it is fair (<i>p = 0.5</i>)
#     <li>toss it 10 times (because <i>n = 10</i>)
#     <li>count the number of heads (<i>k</i>)
# </ul>
# ... 
# 
# Then we could repeat that whole process many times (say, 100 times) and count how often we get exactly 5 heads.
# 
# Or.... we could get the computer to do that. 
# 
# Yes, let's get the computer to do it. That will be less hassle.

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
sns.set_theme() # use pretty defaults


# ### Simulate a single coin toss
# 
# The computer doesn't really toss a coin. 
# 
# It does someting mathematically equivalent, namely generates a random number called <tt>x</tt> and applies a test to it that will give a "hit" a certain proportion of the time, defined by <i>p</i>. 
# 
# If the outcome is a hit,
# the value of the variable <tt>hit</tt> is set to 1, otherwise <tt>hit</tt> is set to zero
# 
# Try running the code block below several times and see if you understand what it does. 

# In[2]:


# generate a random number between 0 and 1
x = np.random.uniform(0,1)
print('value of random number:  ' + str(x))


# What happened?
# 
# We used numpy's random number generator (<tt>np.random</tt>) to get a number (with decimal places) between 0 and 1. The numbers are drawn from a uniform distribution, which means that any number between 0 and 1 is equally likely. 
#     
# Re run the code block above a few times - you should get a different random number every time.
#     
# How do we convert this to a virtual 'coin toss'? We need to randomly generate "hits" and "misses" rather than decimal numbers.
#     
# To do this we simply add a piece of code that checks whether our random number is greater or less than some number - in this case 0.5, as we should get equal frequencies of random numbers greater than 0.5 and less than 0.5, thus simulating a fair coin.

# In[3]:


# check if it is less than p - this should happen on a proportion of trials equal to p
p=0.5
if x>p:
    hit = 1
else:
    hit = 0
print('is it a hit?:            ' + str(hit))


# ### Simulate 10 coin tosses
# 
# In our coin tossing example, we need to toss the coin 10 times (<i>n</i> = 10) 
# and count how many hits we get (<i>k</i> = ?)
# 
# To do this we will create a loop to repeat the coin toss 10 times

# In[4]:


for i in np.arange(10):

    # generate a random number between 0 and 1
    x = np.random.uniform(0,1)
    print('value of random number:  ' + str(x))

    # check if it is less than p - this should happen on a proportion of trials equal to p
    p=0.7
    if x>p:
        hit = 1
    else:
        hit = 0
    print('is it a hit?:            ' + str(hit))


# <img src="images/Minion_ooph.jpeg" width=15% alt="What?!" >
# 
# OK, well the output of that code block was not really user friendly.
# 
# ### Use an array to store the outcomes
# 
# Now that we know how the virtual coin toss works, 
# we can dispense with printing out the actual value of the random number <tt>x</tt>
# and just give the 10 binary outcomes (1/0 for hit/miss)

# In[5]:


for i in np.arange(10):

    # generate a random number between 0 and 1
    x = np.random.uniform(0,1)

    # check if it is less than p - this should happen on a proportion of trials equal to p
    p=0.7
    if x>p:
        hit = 1
    else:
        hit = 0
    print(hit)


# ... but we also want to count the number of hits, so we need to store the outcomes (0/1) in an array

# In[6]:


outcomes = np.empty(10) # create an empty array to store the outcomes

for i in np.arange(10):

    # generate a random number between 0 and 1
    x = np.random.uniform(0,1)

    # check if it is less than p - this should happen on a proportion of trials equal to p
    p=0.7
    if x>p:
        hit = 1
    else:
        hit = 0
    
    outcomes[i] = hit # store the valuee of 'hit' on this trial in place 'i' in the array 'outcomes'
    
print('outcomes = ' + str(outcomes))


# ... and then we need to count the hits:

# In[7]:


k = np.sum(outcomes)
print('k = ' + str(k))


# Try running the code above a few times and check you understand what is happening.
# 
# Note that the outcome values 0. and 1. have dots after them just because they are floating point numbers 
# (numbers that could potentially have something after the decimal place rather than being rounded to the neareest whole number)
# 
# This looks a little awkward but it is just the Python way of writing 0.0 and 1.0 rather than 0 and 1

# ### Use a built in function
# 
# Simulating outcomes is actually something coders do a lot so there is a built in function for it in <tt>numpy</tt>.
# 
# Let's try - it makes the code a lot more compact

# In[8]:


k = np.random.binomial(10,0.5) # generate 10 samples with a 0.5 chance of a hit, and return the number of hits 
print('k = ' + str(k))


# The single line of code above does everything that our previous code block did 
# (it doesn't return the outcomes themselves, but we don't actually need them, do we?)
# 
# <img src="images/Minion_tadaaa.jpg" width=15% alt="ta-daa?!" >
