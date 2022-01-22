#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Loading packages
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#Importing data
demand = pd.read_csv("data/demand_data.csv")
supply = pd.read_csv("data/supply_data.csv")
#mortage_rates = pd.read_csv("data/30_yr_mortgages_rates_points_v2.csv")
#homeownership_rates = pd.read_csv("data/Adjusted_homeownership_rates.csv")
#median_home_price = pd.read_csv("Median_Home_Price_History.csv")


# In[2]:


#Overview of data
demand.head()


# In[3]:


# of rows and columns
demand.shape


# In[4]:


# variable names and data type
demand.dtypes


# In[5]:


# column name, # of observations, # null and data type
demand.info()


# In[6]:


#statistic of data  
demand.describe()


# In[7]:


#Overview of data
supply.head()


# In[8]:


# of rows and columns
supply.shape


# In[9]:


# variable names and data type
supply.dtypes


# In[10]:


# column name, # of observations, # null and data type
supply.info()


# In[11]:


#statistic of data  
supply.describe()


# In[12]:


# print unique count for date variables
d_dates = demand.DATE.unique()

d_dates.sort()

d_dates


# In[13]:


# print unique count for date variables
s_dates = supply.Period.unique()

s_dates.sort()

s_dates


# In[14]:


# change date variable 
demand['DATE_new'] = pd.to_datetime(demand['DATE'])

# create year and quarter columns
demand['Year'] = pd.to_datetime(demand['DATE_new']).dt.to_period('Y')
demand['Quarter'] = pd.to_datetime(demand['DATE_new']).dt.to_period('Q')

demand.head()


# In[15]:


# print unique count for date variables
de_dates = demand.Quarter.unique()

de_dates


# In[16]:


#subset dataset
demand_Quarter = demand.drop(['DATE','DATE_new'], 1)


# group by year and quarter
demand_gb_Quarter = demand_Quarter.groupby(['Year','Quarter'])

demand_gb_Quarter.first()

demand_Quarter.info()


# In[17]:


# change date variable , drop unname column
supply.drop(supply.columns[0], axis=1, inplace=True)

supply['Period_new'] = pd.to_datetime(supply['Period']).dt.strftime("%Y-%d-%m")

# create year and quarter columns
supply['Year'] = pd.to_datetime(supply['Period_new']).dt.to_period('Y')
supply['Quarter'] = pd.to_datetime(supply['Period_new']).dt.to_period('Q')

supply.head()


# In[18]:


# print unique count for date variables
su_dates = supply.Quarter.unique()

su_dates


# In[19]:


#subset dataset
supply_Quarter = supply.drop(['Period','Period_new'], 1)


# create year and quarter columns
supply_gb_Quarter = supply_Quarter.groupby(['Year','Quarter']).sum()

print(supply_gb_Quarter)


supply_Quarter.info()


# In[26]:


supply_Quarter.to_csv('supply_Quarter_clean.csv', index = False)

demand_Quarter.to_csv('demand_Quarter_clean.csv', index = False)


# In[ ]:




