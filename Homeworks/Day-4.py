#!/usr/bin/env python
# coding: utf-8

# In[1]:


def prime_first(number):
  count=0
  if num>1 :
    for i in range(2,num+1):
      if num % i ==0 :
        count+=1
    if count == 1 :
      print(num) 

def prime_second(number):
  count=0
  for i in range(2,num+1):
    if num%i ==0:
      count+=1
  if count==1:
    print(num)          

for num in range(1000):
  if num<500 :
    prime_first(num)
  else :
    prime_second(num)   


# In[ ]:




