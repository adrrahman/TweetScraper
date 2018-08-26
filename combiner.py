
# coding: utf-8

# In[2]:


import os
import json
import sys
import pandas as pd

# In[4]:

if len(sys.argv)==2:
    output = sys.argv[1]+'csv'
else:
    output = 'default.csv' 

tweets = []

path = os.getcwd()+"\Data\\tweet"
print(path)

for filename in os.listdir(path):
    if '.' not in filename:
    	file = path+"\\"+filename
    	with open(file, 'r') as file:
            data = json.load(file)
    	tweets.append(data)


# In[15]:


clean_tweets = []

for i in range(len(tweets)):
    clean_tweets.append([tweets[i]['ID'], tweets[i]['text']])


# In[18]:


my_df = pd.DataFrame(clean_tweets)

my_df.to_csv(output, index=False, header=False)