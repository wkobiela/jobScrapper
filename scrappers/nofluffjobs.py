import re
import requests
from bs4 import BeautifulSoup
from modules.base_logger import log
from modules.common import getDomainName, updateExcel, getPagesCount

class NoFluffJobs():
    def __init__(self):
        self.jobs_dict = {}      

    def updateJobsDict(self, url):
        max_pages = getPagesCount(url,
                    parent='a',
                    child='class',
                    regex='.*page-link.*')
        domainName = getDomainName(url)
        try:
            for page_num in range(1, max_pages + 1):
                page = requests.get(url+f"&page={page_num}")
                page_soup = BeautifulSoup(page.content, "html.parser")
                job_links_list = page_soup.find_all("a", {"class": "posting-list-item"})

                for job in job_links_list:
                    job_link = "https://"+domainName+job['href']
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
            
def run(url):
    log.info("Starting NoFluffJobs scrapper.")
    fluff = NoFluffJobs()
    fluff.updateJobsDict(url)
    updateExcel("NoFluffJobs", fluff.jobs_dict)
    log.info("Finished NoFluffJobs scrapper.")