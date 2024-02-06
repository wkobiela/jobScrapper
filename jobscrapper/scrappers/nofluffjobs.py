import re
import logging
import requests
from bs4 import BeautifulSoup
from jobscrapper.modules.common import getDomainName, updateExcel, getPagesCount

log = logging.getLogger(__name__)

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
                page = requests.get(url+f"&page={page_num}", timeout=120)
                page_soup = BeautifulSoup(page.content, "html.parser")
                job_links_list = page_soup.find_all("a", {"class": "posting-list-item"})

                for job in job_links_list:
                    job_link = "https://"+domainName+job['href']
                    job_title = job.find('h3').text
                    job_company = job.find('h4').text 
                    job_salary = job.find('span', class_=re.compile("badgy salary", re.I)).text
                    job_location = job.find('div', class_=re.compile("tw-flex tw-items-center ng-star-inserted", re.I)).text
                    
                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [job_location]}
        except Exception as e:
            log.error(f"nofluffjobs:updateJobsDict: Exception {e}.")                
            
def run(sheet, url):
    log.info("nofluffjobs:run: Starting NoFluffJobs scrapper.")
    fluff = NoFluffJobs()
    fluff.updateJobsDict(url)
    updateExcel(sheet, fluff.jobs_dict)
    log.info("nofluffjobs:run: Finished NoFluffJobs scrapper.")