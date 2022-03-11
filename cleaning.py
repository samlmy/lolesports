#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
df1 = pd.read_csv('loldata.csv')
df1 = df1[df1['gameid'].notna()]
sample = df1[36:48]
sample.to_csv('sample.csv', index = False)


# In[2]:


pro = ['LCK', 'LCS', 'LEC', 'LPL', 'PCS', 'CBLOL', 'LCO', 'LCL', 'LJL', 'LLA', 'VCS', 'TCL']
lst = []
incomp_gameid = []
for index, row in df1.iterrows():
    if row['player'] == 'unknown player' or row['team'] == 'unknown team' or row['datacompleteness'] != 'complete' or row['league'] not in pro or row['year'] != 2021:
        incomp_gameid.append(row['gameid'])
for index, row in df1.iterrows():        
    if row['gameid'] in incomp_gameid or row['position'] != 'team':
        lst.append(index)


# In[4]:


f1.drop(lst, inplace=True)

timeline = df1[['gameid', 'team', 'killsat10', 'killsat15', 'goldat10','goldat15', 'dragons']]
timeline.loc[:,('killsat10', 'killsat15', 'goldat10','goldat15', 'dragons')] = timeline.loc[:,('killsat10', 'killsat15', 'goldat10','goldat15', 'dragons')].astype(int)
timeline.dtypes


# In[5]:


df = pd.read_csv('loldata.csv')
df = df[df['gameid'].notna()]


# In[6]:


lst = []
incomp_gameid = []
for index, row in df.iterrows():
    if row['player'] == 'unknown player' or row['team'] == 'unknown team' or row['datacompleteness'] != 'complete' or row['league'] not in pro or row['year'] != 2021:
        incomp_gameid.append(row['gameid'])
for index, row in df.iterrows():
    if row['gameid'] in incomp_gameid or row['position'] == 'team':
        lst.append(index)


# In[7]:


df.drop(lst, inplace=True)


# In[8]:


df


# In[9]:


team = df1[['team', 'league']]
team


# In[10]:


player = df[['player', 'team']]


# In[11]:


red = []
drop_red = []
blue = []
win = []
match = df1[['gameid', 'gamelength', 'patch', 'side', 'team', 'result']]
for index, row in match.iterrows():
    if row['side'] == 'Red':
        red.append(row['team'])
        drop_red.append(index)
        if row['result'] == 1:
            win.append('red')
        else:
            win.append('blue')
    elif row['side'] == 'Blue':
        blue.append(row['team'])
        if row['result'] == 0:
            win.append('red')
        else:
            win.append('blue')
match.loc[:,('winner')] = win
match.drop(drop_red, inplace=True)
#len(win)
#len(blue)
#match
match.loc[:,('red')] = red
match.loc[:,('blue')] = blue
match = match[['gameid', 'gamelength', 'patch', 'red', 'blue', 'winner']]
match


# In[ ]:





# In[14]:


score = df[['gameid', 'player', 'position', 'kills', 'totalgold', 'visionscore']]


# In[13]:


team.to_csv('team.csv', index = False)
player.to_csv('player.csv', index = False)
match.to_csv('match.csv', index = False)
timeline.to_csv('timeline.csv', index = False)
score.to_csv('scoreboard.csv', index = False)


# In[70]:




