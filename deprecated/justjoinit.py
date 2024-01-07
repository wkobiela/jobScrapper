import requests
from modules.base_logger import log
from modules.common import updateExcel

class JustJoinIt():
    def __init__(self):
        self.jobs_dict = {}      

    def updateJobsDict(self):
        url = 'https://justjoin.it/api/offers'
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
            response = requests.get(url, headers=headers, timeout=120)
            return response
        except Exception as e:
            log.error(f"Exception {e} on updateJobsDict.")
            return None
            
    def prepareJobsDict(self, response, role, lvl, city):
        marker_list = []
        city_list = []
        exp_list = []

        for offer_dict in response.json():
            url = f'https://justjoin.it/offers/{offer_dict["id"]}'

            if offer_dict.get("marker_icon") not in role:
                continue
            if offer_dict.get("experience_level") not in lvl:
                continue
            if (offer_dict.get("workplace_type") not in ("remote") and 
                not (offer_dict.get("workplace_type") not in ("remote") and offer_dict.get("city") in city)):
                continue
            if offer_dict.get("display_offer") is False:
                continue
            
            job_title = offer_dict.get("title")
            job_company = offer_dict.get("company_name")
            job_salary = offer_dict.get("employment_types")
            job_location = offer_dict.get("city")
            
            self.jobs_dict[url] = {"Title": [job_title], 
                                    "Company": [job_company], 
                                    "Salary": [job_salary], 
                                    "Location": [job_location]}
            marker_list.append(offer_dict.get("marker_icon"))
            city_list.append(offer_dict.get("city"))
            exp_list.append(offer_dict.get("experience_level"))

def run(sheetname, role, lvl, city):
    log.info("Starting JustJointIt scrapper.")
    just = JustJoinIt()
    resp = just.updateJobsDict()
    just.prepareJobsDict(resp, role, lvl, city)
    updateExcel(sheetname, just.jobs_dict)
    log.info("Finished JustJoinIt scrapper.")