import requests
from bs4 import BeautifulSoup as bs
import csv
url=("https://www.indeed.com/q-Web-Developer-l-San-Francisco,-CA-jobs.html",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=10",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=20",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=30",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=40",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=50",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=60",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=70",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=80",
     "https://www.indeed.com/jobs?q=Web+Developer&l=San+Francisco%2C+CA&start=90")

jobs = ["Job Title"]
comName=["Company Name"]
desc=["Description"]
loca=["Location"]
date=["Post Date"]

for x in url:

    r = requests.get(x)
    soup = bs(r.text,"html.parser")

    def extract_job_title_from_result(soup):
        for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard unifiedRow row result"}):
            for span in div.find_all(name="span", attrs={"class":"company"}):
                a=span.get_text()
                comName.append(a)
            for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
                jobs.append(a["title"])
            for div in div.find_all(name="div", attrs={"class":"summary"}):
                a=div.get_text()
                desc.append(a)
            for span in div.find_all(name="span", attrs={"class":"date"}):
                a=span.get_text()
                loca.append(a)
            for div in div.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard-footer"}):
                a=div.get_text()
                date.append(a)
        return()
    extract_job_title_from_result(soup)


#deleting \n and - I'll use - as delimiter
def orderlist(liste):
    a=0
    for x in liste:
        liste[a]=liste[a].replace("\n","")
        liste[a]=liste[a].replace("-"," ")
        a=a+1
orderlist(comName)
orderlist(desc)

#creating csv
with open ("C:\\Users\\Furkan Keskinkilic\\Desktop\\newcsv.csv", "w", newline="") as f:
    writer =csv.writer(f, delimiter="-")
    writer.writerow(jobs)
    writer.writerow(comName)
    writer.writerow(desc)