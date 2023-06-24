import requests
from modules.common import createLinks

def test_is_NoFluffJobs_reachable():
    link = createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk")
    response = requests.get(link, timeout=120)
    assert response.status_code == 200
    
def test_is_BulldogJob_reachable():
    link = createLinks(site='BulldogJob', role="qa", lvl="junior,mid", city="Remote,Gdańsk")
    response = requests.get(link, timeout=120)
    assert response.status_code == 200
    
def test_is_JustJoinIt_reachable():
    link = 'https://justjoin.it/api/offers'
    response = requests.get(link, timeout=120)
    assert response.status_code == 200