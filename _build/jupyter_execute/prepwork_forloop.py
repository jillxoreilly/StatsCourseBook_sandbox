#!/usr/bin/env python
# coding: utf-8

# # The <tt>for</tt> loop
# 
# The thing computers are really good at is repeating a calculation lots of times
# 
# One way to do this is using a loop
# 
# Here we meet the <tt>for</tt> loop (there is also such thing as a <tt>while</tt> loop which we will meet later)

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


# ## Example: "hello, hello, hello"
# 
# Say we want to repeat something a few times, like saying hello
# 
# We can get the computer to do this using a for loop

# In[2]:


for i in range(3):
    print("i = " + str(i))
    print("hello!")


# <ul>
# <li>See if you can change the code to say "hello" five times
# </ul>
# 
# We can also use the <tt>for</tt> loop to do the same operation for every member of a list:

# In[3]:


friends = ['Alan','Barry','Craig']
print('number of friends is ' + str(len(friends)))


for i in range(len(friends)):
    print("i = " + str(i))
    print("Hello " + friends[i] + "!")


# <ul>
#     <li> What does <tt>len(friends)</tt> do? (Hint - check 'number of friends is...')
#     <li> What does <tt>range(len(friends))</tt> do? (Hint - check what <tt>range(3)</tt> did above
# </ul>

# ### Exercise: when to eat shellfish
# 
# It is said that you should only eat shellfish in months that don't have "r" in the name.
# 
# We can check whether a month has an r in the name using the test <tt>in</tt>, which returns <tt>True</tt> or <tt>False</tt>:

# In[4]:


month = "January"
"r" in month


# In[5]:


month = "May"
"r" in month


# We can set up an <tt>if</tt> statement to print different statements depending on whether there is an r in the name of the month

# In[6]:


month = "August"

if ("r" in month):
    print('Don\'t eat shellfish in ' + month)
else:
    print('Do eat shellfish in ' + month)   


# Now can you make a <tt>for</tt> loop that checks every month and prints a sentence about whether to eat shellfish, as in the <tt>if</tt> statement above?

# In[7]:


months=['January','February','March','April','May','June',
        'July','August','September','October','November','Decemeber']

for i in range(12): # complete the code
    if ("r" in months[i]):
        print('Don\'t eat shellfish in ' + months[i])
    else:
        print('Do eat shellfish in ' + months[i]) 
        


# ## Example: adding up numbers
# 
# Say we want to add up all the numbers from 1 to 10. 
# 
# We could do it like this:

# In[8]:


s = 1+2+3+4+5+6+7+8+9+10
print('sum = ' + str(s))


# ... but that would get annoying if we wanted to add up, say, the numbers from 1 to 100.
# 
# Let's try another way.
# 
# First let's get an array with the numbers 1-10 in it using the <tt>numpy</tt> function <tt>np.arange</tt>

# In[9]:


numbers = np.arange(start=1, stop=10, step=1)
print(numbers)


# Oops, I forgot in Python the upper bound of the range is always left out - so if I want to stop at 10 (rather than 9) I need to do this:

# In[10]:


numbers = np.arange(start=1, stop=10+1, step=1)
print(numbers)


# ### Loop: add one number at a time
# 
# Let's create a variable called s which is the sum of the numbers. 
# 
# Initially, s is zero

# In[11]:


s = 0


# Then we can add each element of our array <tt>numbers</tt> in turn

# In[12]:


s = 0
s = s+numbers[0] # remember the first number in the list is indexed '0' not '1'!
print(s)


# and the rest...

# In[13]:


s = 0
s = s+numbers[0] 
print(s)
s = s+numbers[1] 
print(s)
s = s+numbers[2] 
print(s)
s = s+numbers[3] 
print(s)
s = s+numbers[4] 
print(s)
s = s+numbers[5] 
print(s)
s = s+numbers[6] 
print(s)
s = s+numbers[7] 
print(s)
s = s+numbers[8] 
print(s)
s = s+numbers[9] # remember the last one is in position 9, not 10!
print(s)


# Ooph, that was cumbersome!
# 
# We an avoid typing the commands every time by doing a loop

# In[14]:


s=0
numbers = np.arange(start=1, stop=10+1, step=1)
for i in range(len(numbers)):
    s=s+numbers[i]
    print(s)


# We don't even need to print <tt>s</tt> out every time, just at the end
# 
# We signal the end of the loop by the end of the indenting:

# In[15]:


s=0
numbers = np.arange(start=1, stop=10+1, step=1)
for i in range(len(numbers)):
    s=s+numbers[i]
    
print(s)


# We can make our loop generalizable using a variable $n$ for the number up to which we are summing integers:

# In[16]:


n=10
s=0
numbers = np.arange(start=1, stop=n+1, step=1)
for i in range(len(numbers)):
    s=s+numbers[i]
    
print(s)


# ### Exercises:
# 
# <ul>
# <li> Can you edit the loop above so it sums the numbers to n=100 ?
# <li> What about obtaining the sum of the numbers [0.1, 0.2, 0.3 ..... 0.9, 1.0]? 
# </ul>
# 

# 
# ### Aside
# 
# We can actually work out the sum of the numbers to $n$ using the formula 
# 
# $s_n = \frac{n(n+1)}{2}$
# 
# You can think of it as a series of 101 pairs that each add to 100: 
#     <ul list-style-type="none">
#     <li>0+100 = 100
#     <li>1+99 = 100
#     <li>2+98 = 100
#     <li>3+97 = 100
#     </ul>
#     <ul>
#     <li>49+51 = 100
#     <li>50+50 = 100
#     </ul>
#     
# This formula has been known since the time of Pythagoras.
# 
# One charming story about the great mathematician Euler is that when he was in infant school, the master gave the task of summing numbers to 100 to keep the children quiet for a while. Within a few seconds Euler was at his desk with the answer, having immediately perceived that the solution above could be used.
# 

# ## Example: Fibonacci Sequence
# 
# The Fibonacci Sequence is a sequence of numbers that begins [0,1,...] and continues by adding together the two previous numbers such that 
# 
# $$ x_i = x_{i-1} + x_{i-2} $$
# 
# The sequence begins [0, 1, 1, 2, 3, 5, 8, 13..... ] and goes on forever.
# 
# You can find some fun facts about the Fibonacci sequence <a href="https://www.mathsisfun.com/numbers/fibonacci-sequence.html">here</a>:
# 
# Let's make a <tt>for</tt> loop to calculate the first 10 elements of the Fibonacci sequence 

# In[17]:


n = 10 # number of elements to calculate
fibonaccis = np.empty(n) 

# get the sequence started
fibonaccis[0] = 0
fibonaccis[1] = 1

for i in range(2,n): # start in place 2 as we already set the first two elements of the sequence (places 0 and 1)
    fibonaccis[i] = # your code here to calculate the ith Fibonacci number
    
plt.plot(fibonaccis,'.-')
plt.xlabel('$i$')
plt.ylabel('$x_i$')


# In[ ]:




