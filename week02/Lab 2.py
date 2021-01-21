#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Exercise 1

# ### (1) download the two files

# In[3]:


df=pd.read_csv("Downloads/passengerData.csv")
df.head()


# In[4]:


df2 = pd.read_excel("Downloads/ticketPrices.xlsx")
df2.head()


# ### (2) Merge the two files at the column they share

# In[5]:


df_merged = pd.merge(df,df2,on="TicketType")
df_merged.head()


# ### (3) Display the name of the oldest passengers

# In[6]:


old_guy = (df_merged.Age == df_merged.Age.max())
print(df_merged.Name[old_guy])


# ### (4) Plot age versus ticket price

# In[7]:


plt.xlabel("Fare")
plt.ylabel("Age")
plt.scatter(df_merged.Fare, df_merged.Age)


# ### (5) Plot female passengers aged 40-50 who paid greater than or equal to 40

# In[8]:


ladies = (df_merged.Sex=='female')&(df_merged.Age >=40)&(df_merged.Age<=50)&(df_merged.Fare>=40)
plt.xlabel("Fare")
plt.ylabel("Age")
plt.scatter(df_merged.Fare[ladies], df_merged.Age[ladies])


# # Exercise 2
# ### (1) load the Titanic survival data into a pandas data frame

# In[9]:


titanic = pd.read_csv("Downloads/titanicSurvival_m.csv")
titanic.head()


# ### (2) Find the counts of missing values in each column

# In[11]:


pd.isnull(titanic).sum()


# ### (3) Compute the mean and other descriptive statistics

# In[12]:


titanic.describe()


# ### (4) Replace missing values in "age" and "fare" columns with 0, and visualise in a scatter plot

# In[15]:


titanic_0 = titanic[['Fare','Age']].fillna(0)
plt.scatter(titanic_0.Fare, titanic_0.Age)
plt.title('Age vs. Fare: NaN replaced by 0')


# ### (5) Replace the missing values in "age" and "fare" with the mean of each column, and visualise in a scatter plot

# In[16]:


titanic_mean = titanic[['Age', 'Fare']]
mean = titanic[['Age', 'Fare']].mean()
titanic_mean[['Age', 'Fare']] = titanic_mean[['Age', 'Fare']].fillna(value=mean)

plt.scatter(titanic_mean.Fare, titanic_mean.Age)
plt.title('Age vs. Fare: NaN replaced by Means')


# ### (6) Reflect on the differences you see in the plots

# When we fill with 0 you can see a concentration of points near the 0 vertical axis and horizontal.
# In the second you can see a horizontal and vertical concentration around the means (~30)

# # Exercise 3

# ### (1) Download the csv

# In[17]:


tb=pd.read_csv('Downloads/TB_burden_countries_2014-09-29.csv')
tb.head()


# ### (2) Replace missing values

# In[18]:


mean=tb.mean()
tb=tb.fillna(value=mean)


# ### (3) Choose a number of columns with different shapes and visualise on a histogram

# In[19]:


plt.hist(tb.e_prev_100k_hi)


# ### (4) Apply a log transformation on the data

# In[20]:


plt.hist(np.log(tb.e_prev_100k_hi))


# ### (5) choose the numerical columns and map all the columns to [0,1] interval 

# In[21]:


numeric_columns = tb.select_dtypes(include=np.number).columns.tolist()
tb_scaled=tb
tb_scaled[numeric_columns] = tb_scaled[numeric_columns] -tb_scaled[numeric_columns].min()
tb_scaled[numeric_columns] = tb_scaled[numeric_columns]/tb_scaled[numeric_columns].max()
tb_scaled[numeric_columns].describe().loc[['min', 'max'], :]


# ### (6) Compare the means of each column

# In[22]:


tb_scaled[numeric_columns].describe().loc[['mean'], :]


# In[ ]:




