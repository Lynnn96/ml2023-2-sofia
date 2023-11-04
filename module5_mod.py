#!/usr/bin/env python
# coding: utf-8

# In[2]:


class NumberStorage:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def find_number(self, num):
        if num in self.numbers:
            return self.numbers.index(num) + 1
        else:
            return -1


# In[ ]:




