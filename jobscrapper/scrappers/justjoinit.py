import re
import logging
import requests
from bs4 import BeautifulSoup
from jobscrapper.modules.common import getDomainName, updateExcel

log = logging.getLogger(__name__)

class JustJoinIt():
    def __init__(self):
        self.jobs_dict = {}    
        self.job_link_list = []
        self.domain_name = ""
        
    def getJobsLinkList(self, url):
        self.domainName = getDomainName(url)
        page = requests.get(url, timeout=120)
        page_soup = BeautifulSoup(page.content, "html.parser")
        self.job_links_list = page_soup.find_all("div", {"class": "css-1iq2gw3"}) 
        return self.job_links_list, self.domainName

    def updateJobsDict(self, job_links_list, domainName):
        try:
            for job in job_links_list:
                try:
                    job_link = "https://"+domainName+job.find('a',  class_='css-4lqp8g')['href']
                    job_title = job.find('h2').text
                    job_company = job.find('div', class_=re.compile("css-aryx9u", re.I)).text 
                    job_salary = job.find('div', class_=re.compile("css-17pspck", re.I)).text
                    job_location = job.find('div', class_=re.compile("css-11qgze1", re.I)).text
                    if any in (job_link, job_title, job_company, job_salary, job_location) is None:
                        log.error('justjoinit:updateJobsDict: Regex need to be fixed, not working for job: %s', job)
                        break
                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [job_location]}
                except Exception as ie:
                    log.error('justjoinit:updateJobsDict: Exception %s on %s.', ie, job) 
        except Exception as e:
            log.error('justjoinit:updateJobsDict: Exception %s.', e)
            raise
        return self.jobs_dict

def run(sheetname, url): # pragma: no cover
    log.info("justjoinit:run: Starting JustJointIt scrapper.")
    just = JustJoinIt()
    jobs_list, domain = just.getJobsLinkList(url)
    jobs_dict = just.updateJobsDict(jobs_list, domain)
    updateExcel(sheetname, jobs_dict)
    log.info("justjoinit:run: Finished JustJoinIt scrapper.")