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

EXCEL_NAME = 'jobs.xlsx'
NOFLUFFJOBS_SHEET = 'NoFluffJobs'
BULLDOGJOB_SHEET = 'BulldogJob'
JUSTJOINIT_SHEET = 'JustJoinIt'

NOFLUFFJOBS_URL = common.createLinks(site='NoFluffJobs', role="testing", lvl="junior,mid", city="Gdańsk")
BULLDOGJOB_URL = common.createLinks(site='BulldogJob', role="qa,tester", lvl="junior,mid", city="Remote,Gdańsk")

setup.run(EXCEL_NAME, NOFLUFFJOBS_SHEET, BULLDOGJOB_SHEET, JUSTJOINIT_SHEET)
nofluffjobs.run(NOFLUFFJOBS_SHEET, NOFLUFFJOBS_URL)
bulldogjob.run(BULLDOGJOB_SHEET, BULLDOGJOB_URL)
justjoinit.run(JUSTJOINIT_SHEET, role=['testing'], lvl=["mid", "junior"], city='Gdańsk')
