import requests
from sys import argv
from bs4 import BeautifulSoup
import urllib
import re
from openpyxl import load_workbook


class NoFluffJobs():
    # URL = argv[1]
    def __init__(self):
        self.jobs_dict = {}
    
    def getDomainName(self, url):
        parsed_uri = urllib.request.urlparse(url)
        domainName = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return domainName

    def getPagesCount(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        pages_count = soup.find_all('a', {'class': 'page-link'})
        max_page_count = 1
        for page in pages_count:
            try:
                val = int(page.text.strip())
            except(ValueError):
                continue
            max_page_count = val if val > max_page_count else max_page_count
        print(f"All found pages: {max_page_count}")
        max_page_count = 1
        return max_page_count

    def updateJobsDict(self, url):
        max_pages = self.getPagesCount(url)
        domainName = self.getDomainName(url)
        for page_num in range(1, max_pages+1):
            page = requests.get(url+f"?page={page_num}")
            print(page_num)
            page_soup = BeautifulSoup(page.content, "html.parser")
            
            job_links_list = page_soup.find_all("a", {"class": "posting-list-item"})

            for job in job_links_list:
                job_link = domainName+job['href']
                job_title = job.find('h3').text
                job_company = job.find('span', class_=re.compile("company", re.I)).text 
                self.jobs_dict[job_link] = {"Title": [], "Company": []}
                self.jobs_dict[job_link]["Title"].append(job_title)
                self.jobs_dict[job_link]["Company"].append(job_company)
            print(len(self.jobs_dict))
        # print(self.jobs_dict)
    
    def updateExcel(self):
        try:
            workbook = load_workbook("jobs.xlsx")
            sheet = workbook.active

            for k, v in self.jobs_dict.items():
                exists = False
                for row in sheet.rows:
                    if row[0].value == k:
                        # print(f"{row[0].value} Już taki mamy {k}")
                        exists = True
                if exists is False:
                    # print(f"Takiego nie mamy: {k}")
                    sheet.insert_rows(2, 1)
                    sheet.cell(row = 2, column = 1, value = k)
                    sheet.cell(row = 2, column = 2, value = str(v["Title"]))
                    sheet.cell(row = 2, column = 3, value = str(v["Company"]))  
            workbook.save(filename="jobs.xlsx")
        except Exception as e:
            print(f"Exception: {e}")
        
    
fluff = NoFluffJobs()
num = fluff.updateJobsDict("https://nofluffjobs.com/pl/testing")
fluff.updateExcel()