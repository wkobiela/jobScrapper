import re
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.remote_connection import LOGGER

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
        
        LOGGER.setLevel(logging.WARNING)
        
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("useAutomationExtension", "false")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options) 
        driver.get(url)
        
        WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="Warstwa_1"]'))
            )
        
        page_content = driver.page_source    

        page_soup = BeautifulSoup(page_content, "html.parser")
        self.job_links_list = page_soup.find_all("div", {"class": "MuiBox-root css-1jbajow"}) 
 
        return self.job_links_list, self.domainName

    def updateJobsDict(self, job_links_list, domainName):
        try:
            for job in job_links_list:
                try:
                    job_link = "https://"+domainName+job.find('a',  class_='offer_list_offer_link css-3qyn8a')['href']
                    job_title = job.find('h3')
                    if job_title is not None:
                        job_title = job_title.find(string=True, recursive=False).text
                    else:
                        job_title = "Regex error."
                    job_company = job.find('div', class_=re.compile("MuiBox-root css-1mx97sn", re.I))
                    if job_company is not None:
                        job_company = job_company.find(string=True, recursive=True).text
                    else:
                        job_company = "Regex error"
                    job_salary = job.find('div', class_=re.compile("MuiBox-root css-18ypp16", re.I))
                    if job_salary is not None:
                        job_salary = job_salary.find(string=True, recursive=True).text
                    else: 
                        job_salary = "Regex error"
                    job_location = job.find('div', class_=re.compile("MuiBox-root css-1un5sk1", re.I))
                    if job_location is not None:
                        spans = job_location.find_all('span')
                        job_location = ''.join(spans[i].get_text() for i in range(min(2, len(spans))))
                    else: 
                        job_location = "Regex error"

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