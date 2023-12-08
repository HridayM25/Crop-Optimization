#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install prophet


# In[10]:


import pandas as pd
import numpy as np
from prophet import Prophet


# In[ ]:


def forecasted_prediction(df, growth_time):
    """
    Args : Takes in the crop name, and the time for growth.
    
    Returns : tuple (buying_price, selling_price)
    
    """
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=growth_time)
    forecast = model.predict(future)
    selling_price = (forecast['yhat'].tail(1)).iloc[0]
    buying_price = df.iloc[-1].value
    return (buying_price, selling_price)

