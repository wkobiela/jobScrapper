import re
import requests
from bs4 import BeautifulSoup
from common import getDomainName, updateExcel, getPagesCount

class JustJoinIt():
    def __init__(self):
        self.jobs_dict = {}      

    def updateJobsDict(self, url):
        try:
            headers = {
                "content-type": "application/json, text/plain",
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) "
                    "Gecko/20100101 Firefox/57.0"
                ),
                "Host": "justjoin.it",
                "Referer": "justjoin.it",
            }
            response = requests.get(url, headers=headers)
            self.prepareJobsDict(response)
        except Exception as e:
            print(f"Exception {e} on updateJobsDict.")     
            
    def prepareJobsDict(self, response):
        marker_list = []
        city_list = []
        exp_list = []
        for offer_dict in response.json():
            url = f'https://justjoin.it/offers/{offer_dict["id"]}'
            """ Available marker_icons to choose:
            {'testing', 'net', 'architecture', 'ruby', 'php', 'mobile', 'other', 'analytics', 
            'erp', 'go', 'admin', 'scala', 'pm', 'support', 'data', 'java', 'security', 'game', 
            'python', 'ux', 'c', 'javascript', 'devops', 'html'}
            """
            if offer_dict.get("marker_icon") != "testing":
                continue
            if offer_dict.get("experience_level") not in ("mid", "junior"):
                continue
            if offer_dict.get("city") not in ("Gdańsk") or not offer_dict.get("remote"):
                continue
            
            job_title = offer_dict.get("title")
            job_company = offer_dict.get("company_name")
            job_salary = offer_dict.get("employment_types")
            job_location = offer_dict.get("city")
            
            self.jobs_dict[url] = {"Title": [job_title], 
                                    "Company": [job_company], 
                                    "Salary": [job_salary], 
                                    "Location": [job_location]}

            # print(offer_dict)
            marker_list.append(offer_dict.get("marker_icon"))
            city_list.append(offer_dict.get("city"))
            exp_list.append(offer_dict.get("experience_level"))
        # print(set(marker_list))  
        # print(set(city_list))  
        # print(set(exp_list))
            
    
just = JustJoinIt()
just.updateJobsDict("https://justjoin.it/api/offers")
updateExcel("Just", just.jobs_dict)