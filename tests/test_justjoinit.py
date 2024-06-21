from pathlib import Path
import pytest
from bs4 import BeautifulSoup
from jobscrapper.scrappers.justjoinit import JustJoinIt

this_directory = Path(__file__).parent
url = 'https://justjoin.it/gdansk/testing/experience-level_mid.senior/remote_yes'

@pytest.fixture
def _justjoinit():
    justjoinit = JustJoinIt()
    return justjoinit

def test_creating_link_list(_justjoinit):
    jobs_link_list, _ = _justjoinit.getJobsLinkList(url)
    assert len(jobs_link_list) != 0
    
def test_getting_domain(_justjoinit):
    _, domain = _justjoinit.getJobsLinkList(url)
    assert domain == 'justjoin.it'

def test_create_jobs_info_dict(_justjoinit): 
    job_link_list = []
    with open(this_directory / 'testfiles/justjoinit_example_jobs_link_list', encoding="utf8") as f:
        for line in f:
            job_link_list += BeautifulSoup(line, 'html.parser')    
    jobs_dict = _justjoinit.updateJobsDict(job_link_list, 'justjoin.it')
    assert len(jobs_dict) == 21
    
def test_create_jobs_info_dict_wrong_list(_justjoinit):
    wrong_job_link_list = 5
    with pytest.raises(TypeError):
        _justjoinit.updateJobsDict(wrong_job_link_list, 'justjoin.it')
    
    