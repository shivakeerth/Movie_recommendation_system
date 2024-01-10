#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


# In[3]:


movies=pd.read_csv(r"C:\Users\kotha\OneDrive\Desktop\movie_recommendation\top10K-TMDB-movies.csv")


# In[4]:


movies.head(10)


# In[5]:


movies.describe()


# In[6]:


movies.info()


# In[7]:


movies.isnull().sum()


# In[8]:


movies.columns


# In[9]:


movies=movies[['id', 'title', 'genre','overview']]


# In[10]:


movies


# In[11]:


movies['tags']=movies['overview']+movies['genre']


# In[12]:


movies


# In[13]:


new_data = movies.drop(columns=['overview','genre'])


# In[14]:


new_data


# In[15]:


cv=CountVectorizer(max_features=10000,stop_words='english')


# In[16]:


cv


# In[17]:


vector=cv.fit_transform(new_data['tags'].values.astype('U')).toarray()


# In[18]:


vector.shape


# In[19]:


from sklearn.metrics.pairwise import cosine_similarity


# In[20]:


similarity=cosine_similarity(vector)


# In[21]:


similarity


# In[22]:


new_data[new_data['title']=="The Godfather"].index[0]


# In[23]:


distance=sorted(list(enumerate(similarity[2])),reverse=True,key=lambda vector:vector[1])
for i in distance[0:5]:
    print(new_data.iloc[i[0]].title)


# In[24]:


def recommand(movies):
    index=new_data[new_data['title']==movies].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    for i in distance[0:5]:
        print(new_data.iloc[i[0]].title)


# In[25]:


recommand("Iron Man")


# In[41]:


import pickle


# In[43]:


movies_list =r"C:\Users\kotha\OneDrive\Desktop\movie_recommendation\artificats\movie_list.pkl"
pickle.dump(new_data, open(movies_list, 'wb'))


# In[44]:


similarity_pkl = r"C:\Users\kotha\OneDrive\Desktop\movie_recommendation\artificats\similarity.pkl"
pickle.dump(similarity, open(similarity_pkl, 'wb'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




