#!/usr/bin/env python
# coding: utf-8

# In[9]:


print("Twinkle,twinkle, little star \n \t How I wonder what you are! \n \t \t Up above the world so high \n \t \t like the diamond in a sky \n Twinkle,twinkle, little star \n \t How I wonder what you are! ");


# In[11]:


from platform import python_version

print(python_version())


# In[18]:


from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# In[24]:


radius = float (input("Enter circle radius: "))
area = 3.14 * radius * radius
print(area)


# In[27]:


firstname = input("whats your first name ")
lastname = input("whats your last name ")
fullname = lastname + " " + firstname
print(fullname)


# In[28]:


a = int(input("firstnumber to add "))
b = int(input("secondnumber to add "))
print (a+b)


# In[ ]:




