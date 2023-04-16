import requests
from sys import argv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re

# URL = argv[1]
URL = "https://nofluffjobs.com/pl/testing?page=1"
page = requests.get(URL)

# get domain name from url
parsed_uri = urllib.request.urlparse(URL)
domainName = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

jobs_dict = {}

soup = BeautifulSoup(page.content, "html.parser")
job_links_list = soup.find_all("a", {"class": "posting-list-item"})

for job in job_links_list:
    job_link = domainName+job['href']
    job_title = job.find('h3').text
    job_company = job.find('span', class_=re.compile("company", re.I)).text 
    # print(job_link)
    # print(job_title)
    # print(job_company)
    jobs_dict[job_link] = [job_title, job_company]


print(jobs_dict)