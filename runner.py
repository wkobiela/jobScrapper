from scrappers import justjoinit
from scrappers import nofluffjobs
from scrappers import bulldogjob
from modules import setup, common

"""
Parameters:
- justjoinit.run(role(str), lvl(list), city(str)) -> always looks remote + city
- nofluffjobs.run(...(site(str), role(str), lvl(str), city(str))) -> always looks remote + city
- bulldogjob.run(...(ite(str), role(str), lvl(str), city(str)))
"""

setup.run('jobs.xlsx', 'NoFluffJobs', 'BulldogJob', 'JustJoinIt')
nofluffjobs.run(common.createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk"))
bulldogjob.run(common.createLinks(site='BulldogJob', role="qa", lvl="junior,mid", city="Remote,Gdańsk"))
justjoinit.run(role="testing", lvl=["mid", "junior"], city='Gdańsk')
