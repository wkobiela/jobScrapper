import os
import sys
import pytest
sys.path.insert(0, f'{os.getcwd()}')

from modules.common import createLinks


def test_createLinks_not_enough_arguments():
    with pytest.raises(SystemExit):
        assert createLinks(role="testing", lvl="junior,mid", city="Gdańsk")
        
def test_createLinks_wrong_arguments():
    with pytest.raises(SystemExit):
        assert createLinks(website='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk")
        
def test_createLinks_too_much_arguments():
    with pytest.raises(SystemExit):
        assert createLinks(website='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk", more="Somemore")
        
def test_createLinks_BulldogJob():
    assert createLinks(site='BulldogJob', role="qa", lvl="junior,mid", city="Remote,Gdańsk") == \
        "https://bulldogjob.pl/companies/jobs/s/role,qa/experienceLevel,junior,mid/city,Remote,Gdańsk"
        
def test_createLinks_NoFluffJobs():
    assert createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk") == \
        "https://nofluffjobs.com/pl/praca-zdalna/testing?criteria=city%3DGdańsk%20%20seniority%3Djunior,mid"