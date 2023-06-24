import re
import requests
from bs4 import BeautifulSoup
from modules.base_logger import log
from modules.common import updateExcel, getPagesCount

class BulldogJob():
    def __init__(self):
        self.jobs_dict = {}
        
    def updateJobsDict(self, url):
        max_pages = getPagesCount(url, 
                    parent = 'li', 
                    child = 'class', 
                    regex='.*h-10 mx-1 rounded-full flex items-center.*')
        text = ""
        try:
            for page_num in range(1, max_pages + 1):
                page = requests.get(url+f"/page,{page_num}", timeout=120)
                page_soup = BeautifulSoup(page.content, "html.parser")                
                job_links_list = page_soup.find_all("a", {"href": re.compile('.*bulldogjob.pl/companies/jobs/.*')})
                for job in job_links_list:
                    #workarount for false job objects
                    if not job.find('button', class_=re.compile("flex items-center w-full relative text-xs", re.I)): 
                        continue
                    job_link = job.get('href')
                    job_title = job.find(name="h3", class_="text-18 font-extrabold leading-8 mr-8 md:mr-0")
                    job_title = job_title.find(text=True, recursive=False).text
                    job_company = job.find('div', class_=re.compile("text-xxs uppercase", re.I)).text
                    job_salary = job.find('div', class_=re.compile("lg:font-extrabold md:text-xl text-dm", re.I))
                    if job_salary.find(text=True, recursive=True) is not None:
                        job_salary = job_salary.find(text=True, recursive=True).text
                    else:
                        job_salary="Brak informacji"
                    job_overall_info = job.find_all('div', class_=re.compile("flex items-start", re.I))
                    for info in job_overall_info:
                        text = text + info.find('span').text + " / "                  
                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [text]}
                    text = ""
        except Exception as e:
            print(f"Exception {e} on updateJobsDict.")                
            
def run(sheet, url):  
    log.info("Starting BulldogJob scrapper.")
    bull = BulldogJob()
    bull.updateJobsDict(url)
    updateExcel(sheet, bull.jobs_dict)
    log.info("Finished BulldogJob scrapper.")
