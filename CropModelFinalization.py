#!/usr/bin/env python
# coding: utf-8

# In[177]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[178]:


df=pd.read_csv('indiancrop_dataset.csv')
df.head()


# In[179]:


df.info()


# In[180]:


df["STATE"].value_counts()


# In[181]:


df.drop(['STATE'],axis=1,inplace=True)


# In[182]:


df


# In[183]:


df.skew()


# In[184]:


df.P_SOIL=np.log(df['P_SOIL'])


# In[185]:


df.K_SOIL=np.log(df['K_SOIL'])


# In[186]:


df['HUMIDITY']=np.log(df['HUMIDITY'])


# In[187]:


iq1=df['CROP_PRICE'].quantile(0.25)
iq2=df['CROP_PRICE'].quantile(0.75)
iq1


# In[188]:


iq2


# In[189]:


df['CROP_PRICE']=np.where(df['CROP_PRICE']<iq1,iq1,df['CROP_PRICE'])
df['CROP_PRICE']=np.where(df['CROP_PRICE']>iq2,iq2,df['CROP_PRICE'])


# In[190]:


df.skew()


# # **ENCODING CATEGORICAL INTO NUMERICAL**

# In[191]:


from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
le2=LabelEncoder()
df['CROP']=le1.fit_transform(df['CROP'])
# encoded_labels = le1.fit_transform(df['CROP'])
# decoded_labels = le1.inverse_transform(encoded_labels)
# #df['STATE']=le2.fit_transform(df['STATE'])


# In[206]:


def get_mapping():
    label_mapping = dict(zip(range(len(le1.classes_)), le1.classes_))
    return label_mapping


# In[208]:


y = df.pop("CROP")
X = df


# In[209]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.7,random_state=1)


# In[210]:


print("Training data",x_train.shape)


# In[211]:


print("Training data",x_test.shape)


# # **IMPORTING ALGORITHM**
# 
# **NAIVE BAYES**

# In[212]:


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()


# In[213]:


model.fit(x_train,y_train)


# **PREDICTION OF CROP**

# In[214]:


y_prediction=model.predict_proba(x_test)


# # **MODEL METRICS**

# In[215]:


from sklearn.metrics import accuracy_score, log_loss
1-log_loss(y_test,y_prediction)


# # **SAVING THE MODEL**

# In[216]:


import pickle


# In[217]:


filename='crop_model_final.sav'
pickle.dump(model,open(filename,'wb'))


# In[118]:


loaded_model=pickle.load(open('crop_model_final.sav','rb'))


# In[107]:


X.columns


# In[110]:


input_data=(49,4.234107,4.406719,34.315615,2.731860,7.263119,81.787105,350.0)
input_array=np.asarray(input_data)
data_reshape=input_array.reshape(1,-1)
prediction=model.predict_proba(data_reshape)
print(prediction)


# In[111]:


def get_three_max_indices(numbers):
    indices = np.argsort(numbers)[-3:][::-1]
    return indices


# In[115]:


flattened_array = prediction.flatten()

# Get the indices of the top three maximum values
top_three_indices = np.argsort(flattened_array)[-3:][::-1]

print("Indices of the top three maximum values:", top_three_indices)


# In[ ]:




