#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pickle
from CropModelFinalization import get_mapping


# In[4]:


maps = get_mapping()


# In[6]:


loaded_model=pickle.load(open('crop_model_final.sav','rb'))


# In[18]:


input_data=(49,4.234107,4.406719,34.315615,2.731860,7.263119,81.787105,350.0)

def infer(input_data = input_data):
    input_array=np.asarray(input_data)
    data_reshape=input_array.reshape(1,-1)
    prediction=loaded_model.predict_proba(data_reshape)
    flattened_array = prediction.flatten()
    top_three_indices = np.argsort(flattened_array)[-3:][::-1]
    crop_list = [maps[i] for i in top_three_indices]
    return crop_list, np.sort(flattened_array)[-3:][::-1]


# In[19]:


crops_to_grow, prediction = infer()

