from pathlib import Path
import pytest
from bs4 import BeautifulSoup
from jobscrapper.scrappers.bulldogjob import BulldogJob

this_directory = Path(__file__).parent
url = 'https://bulldogjob.pl/companies/jobs/s/role,qa,tester/experienceLevel,junior,medium/city,Remote,Gdansk'

@pytest.fixture
def _bulldogjob():
    bulldog = BulldogJob()
    return bulldog

def test_creating_link_list(_bulldogjob):
    jobs_link_list = _bulldogjob.getJobsLinkList(url)
    assert len(jobs_link_list) != 0

def test_create_jobs_info_dict(_bulldogjob): 
    job_link_list = []
    with open(this_directory / 'testfiles/bulldog_example_jobs_link_list', encoding="utf8") as f:
        for line in f:
            job_link_list += BeautifulSoup(line, 'html.parser')
    jobs_info_dict = _bulldogjob.updateJobsDict(job_link_list)
    assert len(jobs_info_dict) == 13
    
def test_create_jobs_info_dict_wrong_list(_bulldogjob):
    wrong_job_link_list = 5
    with pytest.raises(TypeError):
        _bulldogjob.updateJobsDict(wrong_job_link_list)
    
    