def program():
    import pandas as pd
    import numpy as np
    import requests
    from requests import get
    from urllib.request import urlopen

    import bs4
    from bs4 import BeautifulSoup as bs
    import csv
    import time
    import re

    L1= []
    L2 =[]
    L3 =[]
    L4 =[]
    L5 =[]
    L6 =[]
    

    url = "https://www.indeed.co.in/jobs?q=machine+learning&l=india&start=10"
    html=urlopen(url)
    time.sleep(2)
    soup=bs(html,"html.parser")

    for div in soup.find_all("div",{"class":"row"}):
        for a in div.find_all("a", {"data-tn-element":"jobTitle"}):
                L1.append(a["title"])

    for div in soup.find_all("div",{"class":"row"}):
        for span in div.find_all("span", {"class":"company"}):
                L2.append(span.text.strip())

    for div in soup.find_all("div",{"class":"row"}):
            for span in div.find_all("span",{"class":"location"}):
                  L3.append(span.text.strip())

    for div in soup.find_all("div",{"class":"row"}):
            for div in div.find_all("div", {"class":"summary"}):
                 L4.append(div.text.strip())

    for div in soup.find_all("div",{"class":"row"}):
        try:
                div_two = div.find("div", {"class":"salarySnippet salarySnippetDemphasize"})
                div_three = div_two.find("span", {"class":"salaryText"})
                L5.append(div_three.text.strip())
        except:
            L5.append("Not disclosed")

    for div in soup.find_all("div",{"class":"row"}):
        try:
            for div in div.find_all("div", {"class":"jobsearch-SerpJobCard-footer"}):
                for span in div.find_all("span", {"class":"date"}):
                         L6.append(span.text.strip())
        except:
                     L6.append("Not disclosed")
        
        
        zippedList =  list(zip(L1,L2,L3,L4,L5))
        
        df= pd.DataFrame(zippedList, columns = ['Designation' , 'Company', 'Location','Summary','Salary'])

        data = df.loc[[0]]
        empty = []
        for i in data.itertuples():
            mylist=[i.Designation,i.Company,i.Location,i.Summary,i.Salary]
            empty.append(mylist)

        z= "".join(str(y)for y in empty)
        z=z.strip("]")
        z=z.strip("[")
        

        return(z)

        
   
