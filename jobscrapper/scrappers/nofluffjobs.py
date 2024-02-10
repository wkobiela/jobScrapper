import re
import logging
import requests
from bs4 import BeautifulSoup
from jobscrapper.modules.common import getDomainName, updateExcel, getPagesCount

log = logging.getLogger(__name__)

class NoFluffJobs():
    def __init__(self):
        self.jobs_dict = {}   
        self.job_links_list = []
        self.domain_name = ""
        
    def getJobsLinkList(self, url):
        max_pages = getPagesCount(url, parent='a', child='class', regex='.*page-link.*')
        self.domainName = getDomainName(url)
        for page_num in range(1, max_pages + 1):
            page = requests.get(url+f"&page={page_num}", timeout=120)
            page_soup = BeautifulSoup(page.content, "html.parser")
            self.job_links_list = page_soup.find_all("a", {"class": "posting-list-item"})
        return self.job_links_list, self.domainName

    def updateJobsDict(self, job_links_list, domainName):
        try:
            for job in job_links_list:
                try: 
                    job_link = "https://"+domainName+job['href']
                    job_title = job.find('h3')
                    if job_title is not None:
                        job_title = job_title.find(string=True, recursive=False).text
                    else:
                        job_title = "Regex error."
                    job_company = job.find('h4')
                    if job_company is not None:
                        job_company = job_company.find(string=True, recursive=True).text
                    else:
                        job_company = "Regex error." 
                    job_salary = job.find('span', class_=re.compile("badgy salary", re.I))
                    if job_salary is not None:
                        job_salary = job_salary.find(string=True, recursive=True).text
                    else:
                        job_salary = "Regex error."
                    job_location = job.find('div', class_=re.compile("tw-flex tw-items-center ng-star-inserted", re.I))
                    if job_location is not None:
                        job_location = job_location.find(string=True, recursive=True).text
                    else:
                        job_location = "Regex error."
                                            
                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [job_location]}
                except Exception as ie:
                        log.error('nofluffjobs:updateJobsDict: Exception %s on %s.', ie, job) 
        except Exception as e:
            log.error('nofluffjobs:updateJobsDict: Exception %s.', e)
            raise
        return self.jobs_dict                
            
def run(sheet, url): # pragma: no cover
    log.info("nofluffjobs:run: Starting NoFluffJobs scrapper.")
    fluff = NoFluffJobs()
    jobs_list, domain = fluff.getJobsLinkList(url)
    jobs_dict = fluff.updateJobsDict(jobs_list, domain)
    updateExcel(sheet, jobs_dict)
    log.info("nofluffjobs:run: Finished NoFluffJobs scrapper.")