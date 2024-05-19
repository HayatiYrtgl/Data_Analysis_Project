#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import talib


# In[22]:


# read the data
data = pd.read_excel("../dataset/tumhisse.xlsx")


# In[23]:


data.head()


# In[24]:


# data na values
data.isna().sum()


# In[25]:


# data describe
data.info()


# In[26]:


data.describe().T


# In[27]:


# data dist plot for na values
for i in data.describe().columns:
    sns.displot(data=data[i], kde=True)
    plt.show()


# In[28]:


# mean using
data.isna().sum()


# In[29]:


data["Min(TL)"].fillna(method="ffill", inplace=True)


# In[30]:


data.fillna(method="ffill", inplace=True)


# In[31]:


data.isna().sum()


# In[32]:


# data visual
# target is close price
# index datetime
data.index = pd.to_datetime(data["Tarih"], dayfirst=True)


# In[33]:


data.head()


# In[34]:


# drop tarih column
data.drop("Tarih", inplace=True, axis=1)


# In[35]:


# copy the data
df = data.copy()


# In[36]:


data.head()


# In[37]:


data.plot()


# In[38]:


# scat plot
for i in df.columns:
    if i != "Kapanış(TL)	":
        sns.scatterplot(data=df, x="Kapanış(TL)", y=i,hue="Kapanış(TL)")
        plt.show()


# In[75]:


# zigzag
ilocation_high = []
ilocation_down = []
for i in range(1, len(df["Kapanış(TL)"])):
    if df["Kapanış(TL)"].iloc[i] >= df["Kapanış(TL)"].iloc[i-1]:
        ilocation_high.append(df["Kapanış(TL)"].iloc[i])
        ilocation_down.append(np.nan)
    else:
        ilocation_down.append(df["Kapanış(TL)"].iloc[i-1])
        ilocation_high.append(np.nan)


# In[80]:


plt.plot(ilocation_high, label="Yükseliş", linestyle="-", color="green")
plt.plot(ilocation_down, label="düşüş", linestyle="--", color="red")
plt.legend()


# In[83]:


# target
target_close_price_np = df["Kapanış(TL)"].values


# In[92]:


# INDICATORS moveing average 7 days
df["MA-7"] = talib.MA(target_close_price_np,timeperiod=7)


# In[93]:


df.head()


# In[94]:


# willr indicator
df["willr"] = talib.WILLR(high=df["Max(TL)"].values, close=target_close_price_np, low=df["Min(TL)"].values)


# In[97]:


# adx
df["adx"] = talib.ADX(high=df["Max(TL)"].values, close=target_close_price_np, low=df["Min(TL)"].values)


# In[105]:


# rsi
df["rsi"] = talib.RSI(target_close_price_np)


# In[108]:


# linear reg 
df["linreg"] = talib.LINEARREG(target_close_price_np)


# In[109]:


# momentum
df["momentum"] = talib.MOM(target_close_price_np)


# In[110]:


# ema
df["ema"] = talib.EMA(target_close_price_np)


# In[111]:


df["cci"] = talib.CCI(high=df["Max(TL)"].values, close=target_close_price_np, low=df["Min(TL)"].values)


# In[112]:


df.head()


# In[113]:


df.tail()


# In[114]:


# copy the dataframe
process = df.copy()


# In[116]:


# process heatmap corr
plt.figure(figsize=(16, 8))
sns.heatmap(process.corr(), annot=True)


# In[123]:


import ruptures as rpt


# In[138]:


# pelt algo 
algo = rpt.Pelt(model="l2", min_size=30)
algo.fit(target_close_price_np)
results = algo.predict(pen=1)


# In[139]:


results
plt.figure(figsize=(16, 8))
rpt.display(target_close_price_np, [], results)


# In[140]:


# drop the values from dataset


# In[141]:


# Data Analysis is over...


# In[ ]:




