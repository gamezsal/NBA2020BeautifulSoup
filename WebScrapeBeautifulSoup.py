#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# In[7]:


#NBA Season 2019-2020

#URL page we will be scraping 
url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html".format (2020)

#HTML from given URL
html = urlopen(url)


soup = BeautifulSoup(html)


# In[8]:


# use findALL() to get the column headers
soup.findAll('tr', limit=2)

# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
headers


# In[9]:


# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]


# In[10]:


stats = pd.DataFrame(player_stats, columns = headers)
stats.head(10)


# In[ ]:




