
# coding: utf-8

# In[2]:


import os
import json
import sys

# In[4]:

if len(sys.argv)==2:
    output = sys.argv[1]
else:
    output = 'default.csv'

tweets = []

for filename in os.listdir(os.getcwd()):
    if '.ipynb' not in filename:
        with open(filename, 'r') as file:
            data = json.load(file)
        tweets.append(data)


# In[15]:


clean_tweets = []

for i in range(len(tweets)):
    clean_tweets.append([tweets[i]['ID'], tweets[i]['text']])


# In[18]:


my_df = pd.DataFrame(clean_tweets)

my_df.to_csv('rasis.csv', index=False, header=False)

