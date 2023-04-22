from scrappers import justjoinit
from scrappers import nofluffjobs
from scrappers import bulldogjob
from modules import setup, common

"""
Parameters:
- justjoinit.run(url): url to API
- nofluffjobs.run(...(site, role, lvl, city)) -> always looks remote + city
- bulldogjob.run(...(site, role, lvl, city))
"""

setup.run('jobs.xlsx', 'NoFluffJobs', 'BulldogJob', 'JustJoinIt')
nofluffjobs.run(common.createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk"))
bulldogjob.run(common.createLinks(site='BulldogJob', role="qa", lvl="junior,mid", city="Remote,Gdańsk"))
justjoinit.run("https://justjoin.it/api/offers")
