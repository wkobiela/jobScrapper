import requests
from bs4 import BeautifulSoup
import re
from common import getDomainName, updateExcel

class BulldogJob():
    # URL = argv[1]
    def __init__(self):
        self.jobs_dict = {}
    
    def getPagesCount(self, url):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            pages_count = soup.find_all('li', {"class": re.compile('.*h-10 mx-1 rounded-full flex items-center.*')})
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
                    job_salary = "Brak informacji" if job_salary == None else job_salary.text
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
            
    
bull = BulldogJob()
bull.updateJobsDict("https://bulldogjob.pl/companies/jobs/s/city,Remote/role,tester")
updateExcel("Bull", bull.jobs_dict)