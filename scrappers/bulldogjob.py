import re
import logging
import requests
from bs4 import BeautifulSoup
from modules.common import updateExcel, getPagesCount

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

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
                page = requests.get(url+f"/page,{page_num}")
                page_soup = BeautifulSoup(page.content, "html.parser")                
                job_links_list = page_soup.find_all("div", {"class": re.compile('.*bg-white mb-4 rounded-lg shadow.*')})
                for job in job_links_list:
                    job_link = job.find(name='a')['href']             
                    job_title = job.find(name="h3", class_="JobListItem_title__tdmYl").text
                    job_company = job.find('p', class_=re.compile("JobListItemCompanyDetails", re.I)).text 
                    job_salary = job.find('p', class_=re.compile("text-3", re.I))
                    job_salary = "Brak informacji" if job_salary is None else job_salary.text
                    job_overall_info = job.find_all('div', class_=re.compile("flex items-start my-2", re.I))
                    for info in job_overall_info:
                        text = text + info.find('span').text + " / "
                                        
                    self.jobs_dict[job_link] = {"Title": [job_title], 
                                                "Company": [job_company], 
                                                "Salary": [job_salary], 
                                                "Location": [text]}
                    text = ""
        except Exception as e:
            print(f"Exception {e} on updateJobsDict.")                
            
def run(url):  
    logging.info("Starting BulldogJob scrapper.")
    bull = BulldogJob()
    bull.updateJobsDict(url)
    updateExcel("BulldogJob", bull.jobs_dict)
    logging.info("Finished BulldogJob scrapper.")
