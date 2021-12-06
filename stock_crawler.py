#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import pandas as pd
import time
from pykrx import stock


# In[5]:


stock_total = pd.read_csv("stock_list.csv")


# In[7]:
import sys

start_day = sys.argv[1]
end_day = sys.argv[2]

print(start_day + "/" + end_day)