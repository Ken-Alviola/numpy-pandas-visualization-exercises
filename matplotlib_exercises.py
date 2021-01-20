#!/usr/bin/env python
# coding: utf-8

# In[19]:


#1. Use matplotlib to plot the following equation:
# y = x ** 2 − x + 2
# You'll need to write the code that generates the x and y points.
# Add an anotation for the point 0, 0, the origin.

import matplotlib.pyplot as plt

plt.figure(figsize = (10,6))

x = list(range(-50,51))
y = [(n ** 2) - n + 2 for n in x]

plt.title('$y = x^2 -x +2$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14)

plt.grid(True, ls = '--')

plt.annotate('Origin', xy = (0,0), xytext = (0,500), arrowprops = dict(facecolor = 'gray'))

plt.plot(x,y)


# In[61]:


#2. Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
'''
y = x ** 0.5
y = x ** 3
y = 2 ** x
y = 1 / (x + 1)
'''
x1 = list(range(0,51))
y1 = [n ** 0.5 for n in x1]

plt.figure(figsize = (10,6))

plt.title('$y = \sqrt{x}$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14)

plt.grid(True, ls = '--')

plt.plot(x1,y1)


# In[62]:


plt.figure(figsize = (10,6))

x2 = list(range(-50,50))
y2 = [n ** 3 for n in x2]

plt.title('$y = x^3$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14)

plt.grid(True, ls = '--')

plt.plot(x2,y2)


# In[63]:


plt.figure(figsize = (10,6))

x3 = list(range(0,10))
y3 = [(2 ** n) for n in x3]

plt.title('$y = 2^x$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14)

plt.grid(True, ls = '--')

plt.plot(x3,y3)


# In[64]:


plt.figure(figsize = (10,6))

x4 = list(range(0,50))
y4 = [1 / (n + 1) for n in x4]

plt.title('$y = 1/(x+1)$', fontsize = 20)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14)

plt.grid(True, ls = '--')

plt.plot(x4,y4)


# In[85]:


#3. Combine the figures you created in the last step into one large figure with 4 subplots.
plt.figure(figsize = (10,10))

plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.grid(True, ls = '--')
plt.title('$y = \sqrt{x}$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$   ',fontsize = 14,rotation = 0)


plt.subplot(2,2,2)
plt.plot(x2,y2)
plt.grid(True, ls = '--')
plt.title('$y = x^3$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14,rotation = 0)

plt.subplot(2,2,3)
plt.plot(x3,y3)
plt.grid(True, ls = '--')
plt.title('$y = 2^x$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14, rotation = 0)

plt.subplot(2,2,4)
plt.plot(x4,y4)
plt.grid(True, ls = '--')
plt.title('$y = 1/(x+1)$', fontsize = 16)
plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$',fontsize = 14, rotation = 0)

plt.tight_layout()


# In[147]:


#4. Combine the figures you created in the last step into one figure where each of the 
# 4 equations has a different color for the points. 
# Be sure to include a legend and an appropriate title for the figure.

plt.figure(figsize = (15,15))

x1 = list(range(-20,21))
y1 = [n ** 0.5 for n in x1]

x2 = list(range(-5,6))
y2 = [n ** 3 for n in x2]

x3 = list(range(-20,21))
y3 = [(2 ** n) for n in x3]

x4 = list(range(0,21))
y4 = [1 / (n + 1) for n in x4]


plt.plot(x1,y1, label = '$y = \sqrt{x}$')
plt.grid(True, ls = '--')

plt.xlabel('$x$',fontsize = 14)
plt.ylabel('$y$ ',fontsize = 14,rotation = 0)

plt.plot(x2,y2, color = 'red', label = '$y = x^3$')

plt.plot(x3,y3, color = 'purple', label = '$y = 2^x$')

plt.plot(x4,y4, color = 'green', label = '$y = 1/(x+1)$')

plt.xlim(-10,10)
plt.ylim(-10,10)

#plt.title('$y = 1/(x+1)$', fontsize = 16)
plt.legend()


# In[ ]:




