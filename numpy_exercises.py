#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np
import math
#Use the following code for the questions below:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1. How many negative numbers are there?
print(a[a < 0],'\n')
print(f'There are {len(a[a < 0])} negative numbers in array')


# In[81]:


#2. How many positive numbers are there?

print(a[a > 0],'\n')
print(f'There are {len(a[a > 0])} positive numbers in array')


# In[83]:


#3. How many even positive numbers are there?

positive = a[a > 0]
print('positive:',positive,'\n')

positive_even  = positive[positive % 2 == 0]
print('positive_even:',positive_even,'\n')

print(f'There are {len(positive_even)} positive even numbers in array')


# In[69]:


#4. If you were to add 3 to each data point, how many positive numbers would there be?
a_plus_3 = a + 3
print(a_plus_3)

positive_a_plus_3 = a_plus_3[a_plus_3 > 0]
print(positive_a_plus_3)

print(f'There are {len(positive_a_plus_3)} positive even numbers in array')


# In[71]:


#5. If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2
a_squared.mean(), a_squared.std()


# In[78]:


#6. A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the mean of the data is 0.
#This is done by subtracting the mean from each data point. 
#Center the data set. See this link for more on centering.

a_centered = a - a.mean()

print(f'original:{a},\n mean: {a.mean()},\n centered:{a_centered},\n centered_mean: {a_centered.mean()}')


# In[79]:


#7. Calculate the z-score for each data point. Recall that the z-score is given by:
#Z = (x − μ) / σ

z_score = (a - a.mean())/a.std()
z_score


# In[85]:


#8. Copy the setup and exercise directions
#from More Numpy Practice into your numpy_exercises.py and add your solutions.
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
array_a = np.array(a)
sum_of_a = array_a.sum()
sum_of_a


# In[86]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = array_a.min()
min_of_a


# In[87]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = array_a.max()
max_of_a


# In[88]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = array_a.mean()
mean_of_a


# In[176]:


# Exercise 5 - Make a variable named product_of_a to hold the product 
# of multiplying all the numbers in the above list together

product_of_a = array_a.prod()
product_of_a


# In[90]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like
# [1, 4, 9, 16, 25...]

squares_of_a = array_a ** 2
squares_of_a


# In[91]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = array_a[array_a % 2 != 0]
odds_in_a


# In[92]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = array_a[array_a % 2 == 0]
evens_in_a


# In[130]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
    
print(sum_of_b)

array_b = np.array(b)

sum_of_b = array_b.sum()
sum_of_b


# In[98]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = array_b.min()
min_of_b


# In[101]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = array_b.max()
max_of_b


# In[102]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = array_b.mean()
mean_of_b


# In[110]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        
print(product_of_b)

product_of_b = array_b.prod()

product_of_b


# In[114]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
print(squares_of_b)

squares_of_b = np.square(array_b)
squares_of_b


# In[116]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            
print(odds_in_b)

odds_in_b = array_b[array_b % 2 != 0]
odds_in_b


# In[117]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
            
print(evens_in_b)

evens_in_b = array_b[array_b % 2 == 0]
evens_in_b


# In[120]:


# Exercise 9 - print out the shape of the array b.
array_b.shape


# In[121]:


# Exercise 10 - transpose the array b.

np.transpose(array_b)


# In[129]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(array_b, -1)


# In[131]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(array_b,(6,1))


# In[132]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

array_c = np.array(c)

array_c.min(), array_c.max(), array_c.sum(), array_c.prod()


# In[133]:


# Exercise 2 - Determine the standard deviation of c.
array_c.std()


# In[134]:


# Exercise 3 - Determine the variance of c.
array_c.var()


# In[136]:


# Exercise 4 - Print out the shape of the array c
array_c.shape


# In[139]:


# Exercise 5 - Transpose c and print out transposed result.
np.transpose(c)


# In[143]:


# Exercise 6 - Get the dot product of the array c with c. 
np.dot(array_c,c)


# In[159]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_transposed = np.transpose(c)
print(c_transposed)

c_times_c_trans = c * c_transposed
print(c_times_c_trans)

c_times_c_trans.sum()


# In[160]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed.
# Answer should be 131681894400.

c_times_c_trans.prod()


# In[162]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
array_d = np.array(d)

sin_d = np.sin(array_d)
sin_d


# In[163]:


# Exercise 2 - Find the cosine of all the numbers in d
cos_d = np.cos(array_d)
cos_d


# In[165]:


# Exercise 3 - Find the tangent of all the numbers in d
tan_d = np.tan(array_d)
tan_d


# In[166]:


# Exercise 4 - Find all the negative numbers in d
neg_d = array_d[array_d < 0]
neg_d


# In[167]:


# Exercise 5 - Find all the positive numbers in d
pos_d = array_d[array_d > 0]
pos_d


# In[169]:


# Exercise 6 - Return an array of only the unique numbers in d.
unique_d = np.unique(array_d)
unique_d


# In[171]:


# Exercise 7 - Determine how many unique numbers there are in d.
print(np.unique(array_d,return_counts = True))
len(np.unique(array_d))


# In[173]:


# Exercise 8 - Print out the shape of d.
array_d.shape


# In[174]:


# Exercise 9 - Transpose and then print out the shape of d.
print(np.transpose(array_d))


# In[175]:


# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(array_d, (9,2))


# In[178]:


#Awesome Bonus For much more practice with numpy, 
#Go to https://github.com/rougier/numpy-100 and click the "Fork" icon in the upper-right
#of the screen to fork the repo. This makes a copy of the repo onto your own account. 
#Next, clone your fork https://github.com/your-username/numpy-100 down to your machine.
#Work through, add, commit, and push your solutions to your own repo.


# In[ ]:




