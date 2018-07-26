# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:16:53 2018

@author: CodersMine Vinay Verma
"""

"""
find=['apple','ball']

file=open("LIST","r")

for i in range(len(find)):
    file.write(find[i])
file.close()

reading was much powerful using pandas than file

FORMAT = Just names of the title 
"""


import requests
from bs4 import BeautifulSoup

import pandas as pd
dataset=pd.read_csv("LIST.txt",header= None)
find=dataset.iloc[:,0]

file=open("SearchResults.txt","w")

for i in range(len(find)):
    r=requests.get("https://en.wikipedia.org/wiki/"+find[i])
    c=r.content
    
    soup=BeautifulSoup(c,"html.parser")
    #print(soup.prettify())
    
    all=soup.find_all("div",{"class":"mw-parser-output"})
    
    print(find[i])
    #print(all[0].find_all("p")[1].text)
    file.write("\n\n"+find[i]+"\n\n\n"+all[0].find_all("p")[1].text)

file.close()    
print("\n\nProgram Completed Successfully : Files Written \n\n")