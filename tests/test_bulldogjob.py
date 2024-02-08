from pathlib import Path
from bs4 import BeautifulSoup
from jobscrapper.scrappers.bulldogjob import BulldogJob

this_directory = Path(__file__).parent

bulldog = BulldogJob()
url = 'https://bulldogjob.pl/companies/jobs/s/role,qa,tester/experienceLevel,junior,medium/city,Remote,Gdansk'


def test_creating_link_list():
    jobs_link_list = bulldog.getJobsLinkList(url)
    
    assert len(jobs_link_list) != 0

    
def test_create_jobs_info_dict(): 
    job_link_list = []
    
    with open(this_directory / 'testfiles/bulldog_example_jobs_link_list', encoding="utf8") as f:
        for line in f:
            job_link_list += BeautifulSoup(line, 'html.parser')
    
    jobs_info_dict = bulldog.updateJobsDict(job_link_list)
    
    assert len(jobs_info_dict) == 11