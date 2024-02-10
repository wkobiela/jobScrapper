from pathlib import Path
import pytest
from bs4 import BeautifulSoup
from jobscrapper.scrappers.nofluffjobs import NoFluffJobs

this_directory = Path(__file__).parent
url = 'https://nofluffjobs.com/pl/praca-zdalna/testing?criteria=city%3DGdansk%20%20seniority%3Djunior,mid'

@pytest.fixture
def _nofluffjobs():
    nofluffjobs = NoFluffJobs()
    return nofluffjobs

def test_creating_link_list(_nofluffjobs):
    jobs_link_list, _ = _nofluffjobs.getJobsLinkList(url)
    assert len(jobs_link_list) != 0
    
def test_getting_domain(_nofluffjobs):
    _, domain = _nofluffjobs.getJobsLinkList(url)
    assert domain == 'nofluffjobs.com'

def test_create_jobs_info_dict(_nofluffjobs): 
    job_link_list = []
    with open(this_directory / 'testfiles/nofluffjobs_example_jobs_link_list', encoding="utf8") as f:
        for line in f:
            job_link_list += BeautifulSoup(line, 'html.parser')    
    jobs_dict = _nofluffjobs.updateJobsDict(job_link_list, 'nofluffjobs.com')
    assert len(jobs_dict) == 20
    
def test_create_jobs_info_dict_wrong_list(_nofluffjobs):
    wrong_job_link_list = 5
    with pytest.raises(TypeError):
        _nofluffjobs.updateJobsDict(wrong_job_link_list, 'nofluffjobs.com')