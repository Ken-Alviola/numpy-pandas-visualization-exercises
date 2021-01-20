#!/usr/bin/env python
# coding: utf-8

# In[92]:


'''
Title your chart "Big O Notation"
Label your x axis "Elements"
Label your y axis "Operations"
Label your curves or make a legend for the curves
Use LaTex notation where possible

Curves to graph:

y = 0x + 1 and label the curve "O(1)"
y = log(x)and label the curve "v"
y = x and label the curve "O(n)"
y = x * log(x) and label it "O(n log n)"
y = x ** 2 and label it "O(n^2)"
y = 2 ** x and label it "O(2^n)"
y = n! and label it "O(n!)"
y = n ** n and label it "O(n^n)"
'''
import matplotlib.pyplot as plt
import math

plt.figure(figsize = (10,10))
plt.xlabel('Elements',fontsize = 14)
plt.ylabel('Operations',fontsize = 14)
plt.grid(True, ls = '--')

plt.title('Big O Notation')

x1 = list(range(-100,101))
y1 = [0 * n + 1 for n in x1] 

x2 = list(range(1,100))
y2 = [math.log(n) for n in x2]

x3 = list(range(-100,101))
y3 = [n for n in x3]

x4 = list(range(1,100))
y4 = [n * math.log(n) for n in x4]

x5 = list(range(-25,26))
y5 = [n ** 2 for n in x5]

x6 = list(range(-100,10))
y6 = [2 ** n for n in x6]

x7 = list(range(0,7))
y7 = [math.factorial(n) for n in x7]

x8 = list(range(-10,6))
y8 = [n ** n for n in x8]


plt.plot(x1,y1, label = '$O(1)$')
plt.plot(x2,y2, label = '$O(log n)$')
plt.plot(x3,y3, label = '$O(n)$')
plt.plot(x4,y4, label = '$O(n log n)$')
plt.plot(x5,y5, label = '$O(n^2)$')
plt.plot(x6,y6, label = 'O(2^n)')
plt.plot(x7,y7, label = '$O(n!)$')
plt.plot(x8,y8, label = '$O(n^n)$')

plt.axhline(0, color = 'k', linewidth = 1.5)
plt.axvline(0, color = 'k', linewidth = 1.5)

plt.xlim(-15,15)
plt.ylim(-5,10)

plt.legend()


# In[ ]:


#6. Bonus Write the code necessary to write your name on a chart. Use box letters.


# In[ ]:


#7. Bonus: use curves for letters in your name that have curves in them.


# In[ ]:




