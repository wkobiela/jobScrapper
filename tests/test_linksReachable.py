import requests
from modules.common import createLinks

def test_is_NoFluffJobs_reachable():
    link = createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk")
    response = requests.get(link, timeout=120)
    assert response.status_code == 200
    
def test_is_BulldogJob_reachable():
    link = createLinks(site='BulldogJob', role="qa,tester", lvl="junior,medium", city="Remote,Gdańsk")
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(link, timeout=120, headers=headers)
    assert response.status_code == 200
    
# def test_is_JustJoinIt_reachable():
#     link = 'https://justjoin.it/api/offers'
#     response = requests.get(link, timeout=120)
#     assert response.status_code == 200