import re
import logging
import requests
from bs4 import BeautifulSoup
from jobscrapper.modules.common import updateExcel, getPagesCount

log = logging.getLogger(__name__)

class BulldogJob():
    def __init__(self):
        self.jobs_dict = {}
        self.job_link_list = []
        self.header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/58.0.3029.110 Safari/537.36'
                }
        
    def getJobsLinkList(self, url):
        max_pages = getPagesCount(url, parent = 'li', child = 'class', 
            regex='.*h-10 mx-1 rounded-full flex items-center.*')
        for page_number in range(1, max_pages + 1):
            page = requests.get(url+f"/page,{page_number}", timeout=120, headers=self.header)
            page_content = BeautifulSoup(page.content, "html.parser")
            self.job_link_list += page_content.find_all("a", {"href": re.compile('.*bulldogjob.pl/companies/jobs/.*')})
        return self.job_link_list
        
    def updateJobsDict(self, job_link_list):
        text = ""
        try:
            for job in job_link_list:
                try:
                    #workarount for false job objects
                    if not job.find('div', class_=re.compile("flex flex-col items-center relative my-auto", re.I)): 
                        continue

                    job_link = job.get('href')
                    job_title = job.find(name="h3", class_=re.compile("md:mb-5 lg:mb-0 md:text-18 text", re.I))
                    if job_title.find(string=True, recursive=True) is not None:
                        job_title = job_title.find(string=True, recursive=False).text
                    else:
                        job_title="Regex error."
                    
                    job_company = job.find('div', class_=re.compile("text-xxs uppercase", re.I))
                    if job_company.find(string=True, recursive=True) is not None:
                        job_company = job_company.find(string=True, recursive=True) is not None
                    else:
                        job_company = "Regex error"
                    
                    job_salary = job.find('div', class_=re.compile("lg:font-extrabold md:text-xl text-dm", re.I))
                    if job_salary is not None:
                        job_salary = job_salary.find(string=True, recursive=True).text
                    else:
                        job_salary="No information or regex error"
                        
                    job_overall_info = job.find_all('div', class_=re.compile("flex items-start", re.I))
                    for info in job_overall_info:
                        text = text + info.find('span').text + " / "

                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [text]}
                    text = ""
                except Exception as ie:
                    log.error('bulldogjob:updateJobsDict: Exception %s on %s.',ie ,job) 
        except Exception as e:
            log.error('bulldogjob:updateJobsDict: Exception %s.', e)     
        return self.jobs_dict           
            
def run(sheet, url):  
    log.info("bulldogjob:run: Starting BulldogJob scrapper.")
    bull = BulldogJob()
    jobs_list = bull.getJobsLinkList(url)
    jobs_dict = bull.updateJobsDict(jobs_list)
    updateExcel(sheet, jobs_dict)
    log.info("bulldogjob:run: Finished BulldogJob scrapper.")
