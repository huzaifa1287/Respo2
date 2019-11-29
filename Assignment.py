#!/usr/bin/env python
# coding: utf-8

# # Python Assignment
# 

# In[1]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[2]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[1]:


pi=3.142
rad = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(rad) + " is: " + str(pi * rad**2))


# In[4]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[6]:


num1 =int(input("Enter number1:"))
num2 = int(input("Enter number2:"))

sum =num1+num2

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[16]:


print("Twinkle, twinkle, little star\n\tHow I wonder what you are!\n\tUp above the world so high,\n\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


# In[ ]:




