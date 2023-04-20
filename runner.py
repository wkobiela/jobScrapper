from scrappers import justjoinit
from scrappers import nofluffjobs
from scrappers import bulldogjob
from modules import setup

"""
Parameters:
- justjoinit.run(url): url to API
- nofluffjobs.run(url): url to prepared search link
- bulldogjo.run(url): url to prepared search link
"""

setup.run('jobs.xlsx', 'NoFluffJobs', 'BulldogJob', 'JustJoinIt')
nofluffjobs.run("https://nofluffjobs.com/pl/praca-zdalna/testing?criteria=city%3Dgdansk,trojmiasto,sopot%20%20seniority%3Djunior,mid")
bulldogjob.run("https://bulldogjob.pl/companies/jobs/s/role,qa/experienceLevel,junior,medium/city,Remote,Tr%C3%B3jmiasto")
justjoinit.run("https://justjoin.it/api/offers")
