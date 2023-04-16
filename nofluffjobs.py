import requests
from bs4 import BeautifulSoup
import re
from common import getDomainName, updateExcel

class NoFluffJobs():
    # URL = argv[1]
    def __init__(self):
        self.jobs_dict = {}
    
    def getPagesCount(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            pages_count = soup.find_all('a', {'class': 'page-link'})
            max_page_count = 1
            for page in pages_count:
                try:
                    val = int(page.text.strip())
                except(ValueError):
                    continue
                max_page_count = val if val > max_page_count else max_page_count
            print(f"All found pages: {max_page_count}")
            return max_page_count
        except Exception as e:
            print(f"Exception {e} on getPagesCount.")        

    def updateJobsDict(self, url):
        max_pages = self.getPagesCount(url)
        domainName = getDomainName(url)
        try:
            for page_num in range(1, max_pages + 1):
                page = requests.get(url+f"&page={page_num}")
                page_soup = BeautifulSoup(page.content, "html.parser")
                job_links_list = page_soup.find_all("a", {"class": "posting-list-item"})

                for job in job_links_list:
                    job_link = domainName+job['href']
                    job_title = job.find('h3').text
                    job_company = job.find('span', class_=re.compile("company", re.I)).text 
                    job_salary = job.find('span', class_=re.compile("badgy salary", re.I)).text
                    job_location = job.find('div', class_=re.compile("tw-flex tw-items-center ng-star-inserted", re.I)).text
                    
                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [job_location]}
                    #print(len(self.jobs_dict))
        # print(self.jobs_dict)
        except Exception as e:
            print(f"Exception {e} on updateJobsDict.")                
            
    
fluff = NoFluffJobs()
fluff.updateJobsDict("https://nofluffjobs.com/pl/testing?criteria=employment%3Db2b%20requirement%3DPython")
updateExcel("NoFluff", fluff.jobs_dict)