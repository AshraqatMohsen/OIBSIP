#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()
import datetime as dt


# In[4]:


retail  = pd.read_csv('data/retail_sales_dataset.csv'  , index_col = 'Transaction ID')


# In[5]:


retail.head()


# In[6]:


retail.tail()


# In[7]:


retail.shape


# In[8]:


retail.shape[1] #number of columns


# In[9]:


retail.shape[0]  #number of rows


# In[10]:


retail.info()


# In[11]:


retail.describe()


# In[12]:


retail.describe(include = 'all') #describing the whole data


# In[13]:


retail.isna().sum() #check null values


# In[15]:


retail.duplicated().sum() #check duplicate values


# In[30]:


retail['Gender'].unique()


# In[31]:


retail['Gender'].nunique()


# In[17]:


retail['Gender'].value_counts()


# In[28]:


retail['Age'].unique()


# In[29]:


retail['Age'].nunique()


# In[19]:


retail['Age'].value_counts()


# In[26]:


retail['Product Category'].unique()


# In[27]:


retail['Product Category'].nunique()


# In[20]:


retail['Product Category'].value_counts()


# * the data type of date , gender , product category are incorectly , so change it 

# In[21]:


# change date type
retail['Date'] = pd.to_datetime(retail['Date'])


# In[23]:


#change gender type to category
retail['Gender'] = retail['Gender'].astype('category')


# In[24]:


# change Product category to category
retail['Product Category']=retail['Product Category'].astype('category')


# In[25]:


retail.dtypes


# In[32]:


gender_counts = retail.Gender.value_counts()


# In[35]:


plt.pie(gender_counts , labels = gender_counts.index , autopct = '%1.1f%%')
plt.title('Gender')


# In[36]:


product_category_counts = retail['Product Category'].value_counts()


# In[44]:


retail['Product Category'].value_counts().plot(kind = 'bar' , color = 'skyblue')


# In[59]:


retail.groupby('Gender')['Product Category'].count()


# In[61]:


retail.groupby(['Age','Gender'])['Product Category'].count()


# In[62]:


retail.groupby(['Age','Gender'])['Product Category' , 'Quantity'].count()


# In[63]:


retail.groupby(['Age','Gender' , 'Product Category'])['Quantity'].count()


# In[64]:


retail.groupby(['Age','Gender' , 'Product Category'])['Quantity'].count().to_frame()


# In[65]:


retail.groupby(['Age','Gender' , 'Product Category' , 'Quantity'])['Price per Unit'].count().to_frame()


# In[66]:


retail['Quantity'].unique()


# In[67]:


retail['Quantity'].nunique()


# In[69]:


retail['Quantity'].value_counts()


# In[70]:


retail['Quantity'].value_counts().plot(kind = 'bar' , color = 'skyblue')


# In[71]:


retail['Price per Unit'].unique()


# In[72]:


retail['Price per Unit'].nunique()


# In[73]:


retail['Price per Unit'].value_counts()


# In[75]:


retail.groupby(['Age'])['Price per Unit'].count()


# In[76]:


retail.groupby(['Age'])['Price per Unit' , 'Product Category'].count()


# In[77]:


retail.groupby(['Age', 'Product Category'])['Price per Unit'].count()


# In[78]:


retail.groupby(['Age', 'Product Category' , 'Gender'])['Price per Unit'].count()


# In[80]:


retail.groupby('Product Category')['Total Amount'].sum()


# In[81]:


retail.groupby('Product Category')['Total Amount'].count()


# In[82]:


sales_by_category = retail.groupby('Product Category')['Total Amount'].sum()


# In[85]:


sales_by_category.plot(kind='bar')
plt.title('Sales by each Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)


# In[86]:


retail['Date']=retail['Date'].dt.strftime('%d-%m-%Y')


# In[87]:


retail.head(1)


# # Total Sales by month

# * create new column for month , day , year 

# In[90]:


retail['Date'] = pd.to_datetime(retail['Date'])


# In[91]:


retail['Month'] = retail['Date'].dt.month


# In[92]:


retail['Year'] = retail['Date'].dt.year


# In[93]:


retail['weekday'] = retail['Date'].dt.weekday


# In[114]:


retail['Quarter'] = retail['Date'].dt.quarter


# In[115]:


retail.head(1)


# In[95]:


retail['day'] = retail['Date'].dt.day


# In[116]:


retail.head(1)


# # Revenue by month

# In[101]:


retail.groupby('Month')['Total Amount'].sum()


# In[102]:


monthly_sales =  retail.groupby('Month')['Total Amount'].sum()


# # plot Revenue by month

# In[103]:


monthly_sales.plot(kind = 'bar')
plt.title('Monthly Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)


# In[130]:


sns.set_style('whitegrid')
plt.figure(figsize=(13, 6))
plt.plot(monthly_sales, marker= 'o')
plt.xlabel('Month')
plt.ylabel('Total sales')
plt.title("Overall Sales Monthly")


# 
# # Revenue by Year
# 

# In[104]:


retail.groupby('Year')['Total Amount'].sum()


# In[105]:


year_sales =  retail.groupby('Year')['Total Amount'].sum()


# # plot Revenue by Year

# In[106]:


year_sales.plot(kind = 'bar')
plt.title('Year Total Sales')
plt.xlabel('Year')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)


# In[129]:


sns.set_style('whitegrid')
plt.figure(figsize=(13, 6))
plt.plot(year_sales, marker= 'o')
plt.xlabel('Year')
plt.ylabel('Total sales')
plt.title(" Sales Yearly")


# # Revenue by Quarter

# In[117]:


retail.groupby('Quarter')['Total Amount'].sum()


# In[118]:


sales_by_quarter =  retail.groupby('Quarter')['Total Amount'].sum()


# # Plot Revenue by Quarter
# 

# In[119]:


sales_by_quarter.plot(kind = 'bar')
plt.title('Quarter Total Sales')
plt.xlabel('Quarter')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)


# In[126]:


sns.set_style('whitegrid')
plt.figure(figsize=(13, 6))
plt.plot(sales_by_quarter, marker= 'o')
plt.xlabel('Month')
plt.ylabel('Total sales')
plt.title("Overall Sales Monthly")


# # Total Sales by Category

# In[107]:


retail.groupby('Product Category')['Total Amount'].sum()


# In[108]:


sales_category = retail.groupby('Product Category')['Total Amount'].sum()


# In[109]:


sales_category.plot(kind='bar')
plt.title('Sales by Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)


# # Sales by Gender

# In[110]:


retail.groupby('Gender')['Total Amount'].sum()


# In[111]:


sales_by_gender = retail.groupby('Gender')['Total Amount'].sum()


# In[113]:


sales_by_gender.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Gender')


# In[136]:


retail.groupby(['Gender','Product Category']).count()


# In[137]:


retail.groupby(['Gender','Product Category'])['Product Category'].count()


# In[138]:


category_by_gender = retail.groupby(['Gender','Product Category'])['Product Category'].count()


# In[139]:


category_by_gender = pd.DataFrame(category_by_gender)


# In[140]:


category_by_gender


# In[154]:


retail.groupby(['Gender','Product Category'])['Product Category'].get_group(('Female' , 'Beauty')).count()


# In[155]:


female_beauty = retail.groupby(['Gender','Product Category'])['Product Category'].get_group(('Female' , 'Beauty')).count()


# In[156]:


male_beauty =  retail.groupby(['Gender','Product Category'])['Product Category'].get_group(('Male' , 'Beauty')).count()


# In[ ]:




