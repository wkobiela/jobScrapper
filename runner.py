from scrappers import justjoinit
from scrappers import nofluffjobs
from scrappers import bulldogjob

"""
Parameters:
- justjoinit.run(url): url to API
- nofluffjobs.run(url): url to prepared search link
- bulldogjo.run(url): url to prepared search link
"""

justjoinit.run("https://justjoin.it/api/offers")
nofluffjobs.run("https://nofluffjobs.com/pl/testing?criteria=employment%3Db2b%20%20seniority%3Djunior,mid")
bulldogjob.run("https://bulldogjob.pl/companies/jobs/s/city,Remote/role,tester")