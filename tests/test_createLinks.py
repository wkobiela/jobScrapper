import pytest
from jobscrapper.modules import common



def test_createLinks_not_enough_arguments():
    with pytest.raises(SystemExit):
        common.createLinks(role="testing", lvl="junior,mid", city="Gdańsk")
        
def test_createLinks_wrong_arguments():
    with pytest.raises(SystemExit):
        common.createLinks(website='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk")
        
def test_createLinks_too_much_arguments():
    with pytest.raises(SystemExit):
        common.createLinks(website='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk", more="Somemore")
        
def test_createLinks_BulldogJob():
    assert common.createLinks(site='BulldogJob', role="qa,tester", lvl="junior,medium", city="Remote,Gdańsk") == \
        "https://bulldogjob.pl/companies/jobs/s/role,qa,tester/experienceLevel,junior,medium/city,Remote,Gdansk"
        
def test_createLinks_NoFluffJobs():
    assert common.createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk") == \
        "https://nofluffjobs.com/pl/praca-zdalna/testing?criteria=city%3DGdansk%20%20seniority%3Djunior,mid"
        
def test_createLinks_JustjoinIt():
    assert common.createLinks(site="JustjoinIt", role="testing", lvl="mid.senior", city="Gdańsk") == \
        "https://justjoin.it/gdansk/testing/experience-level_mid.senior/remote_yes"