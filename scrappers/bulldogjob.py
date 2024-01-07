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
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/58.0.3029.110 Safari/537.36'
                }
                page = requests.get(url+f"/page,{page_num}", timeout=120, headers=headers)
                page_soup = BeautifulSoup(page.content, "html.parser")                
                job_links_list = page_soup.find_all("a", {"href": re.compile('.*bulldogjob.pl/companies/jobs/.*')})
                for job in job_links_list:
                    try:
                        #workarount for false job objects
                        if not job.find('div', class_=re.compile("flex flex-col items-center relative my-auto", re.I)): 
                            continue

                        job_link = job.get('href')
                        
                        job_title = job.find(name="h3", class_=re.compile("md:mb-5 lg:mb-0 md:text-18 text", re.I))
                        if job_title.find(text=True, recursive=True) is not None:
                            job_title = job_title.find(text=True, recursive=False).text
                        else:
                            job_title="Regex error."
                        
                        job_company = job.find('div', class_=re.compile("text-xxs uppercase", re.I))
                        if job_company.find(text=True, recursive=True) is not None:
                            job_company = job_company.find(text=True, recursive=True) is not None
                        else:
                            job_company = "Regex error"
                        
                        job_salary = job.find('div', class_=re.compile("lg:font-extrabold md:text-xl text-dm", re.I))
                        if job_salary is not None:
                            job_salary = job_salary.find(text=True, recursive=True).text
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
                        print(f"Exception {ie} on {job}.") 
        except Exception as e:
            print(f"Exception {e} on updateJobsDict.")                
            
def run(sheet, url):  
    log.info("Starting BulldogJob scrapper.")
    bull = BulldogJob()
    bull.updateJobsDict(url)
    updateExcel(sheet, bull.jobs_dict)
    log.info("Finished BulldogJob scrapper.")
