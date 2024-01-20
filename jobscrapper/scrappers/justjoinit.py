import re
import requests
from bs4 import BeautifulSoup
from jobscrapper.modules.base_logger import log
from jobscrapper.modules.common import getDomainName, updateExcel

class JustJoinIt():
    def __init__(self):
        self.jobs_dict = {}      

    def updateJobsDict(self, url):
        domainName = getDomainName(url)
        try:
            page = requests.get(url, timeout=120)
            page_soup = BeautifulSoup(page.content, "html.parser")
            job_links_list = page_soup.find_all("div", {"class": "css-1iq2gw3"})

            for job in job_links_list:
                job_link = "https://"+domainName+job.find('a',  class_='css-4lqp8g')['href']
                job_title = job.find('h2').text
                job_company = job.find('div', class_=re.compile("css-ldh1c9", re.I)).text 
                job_salary = job.find('div', class_=re.compile("css-1b2ga3v", re.I)).text
                job_location = job.find('div', class_=re.compile("css-68pppj", re.I)).text
                self.jobs_dict[job_link] = {"Title": [job_title], 
                                            "Company": [job_company], 
                                            "Salary": [job_salary], 
                                            "Location": [job_location]}
        except Exception as e:
            log.error(f"justjoinit:updateJobsDict: Exception {e}.")

def run(sheetname, url):
    log.info("justjoinit:run: Starting JustJointIt scrapper.")
    just = JustJoinIt()
    just.updateJobsDict(url)
    updateExcel(sheetname, just.jobs_dict)
    log.info("justjoinit:run: Finished JustJoinIt scrapper.")