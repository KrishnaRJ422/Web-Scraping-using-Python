Created on Wed Dec 30 19:42:42 2020

@author: krish
"""
import pandas as pd
import requests
import numpy as np
#to extract first page
url = "https://kvsangathan.nic.in/about-kvs/directories/kvs-directory"
r = requests.get(url,verify=False)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df = df_list[0]
df.head()
df.to_csv('data_kv1.csv',index=False)

#to extract data of next pages
pages = np.arange(1, 43, 1)
for page in pages:
    print(page)
    page="https://kvsangathan.nic.in/about-kvs/directories/kvs-directory?page=" + str(page)
#url = "https://kvsangathan.nic.in/about-kvs/directories/kvs-directory?page=$i"
    print(page)
    r = requests.get(page,verify=False)
    df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
    df = df_list[0]
    #df.head()
    df.to_csv('data_kv2.csv',index=False,mode='a',header=False)
