from scrappers import justjoinit
from scrappers import nofluffjobs
from scrappers import bulldogjob
from modules import setup, common, base_logger

# Excel settings
EXCEL_NAME = 'jobs.xlsx'
NOFLUFFJOBS_SHEET = 'NoFluffJobs'
BULLDOGJOB_SHEET = 'BulldogJob'
JUSTJOINIT_SHEET = 'JustJoinIt'

# Search params
nofluffjobs_settings = {
    "site": "NoFluffJobs",
    "role": "testing",
    "lvl": "junior,mid",
    "city": "Gdańsk" 
}

bulldogjob_settings = {
    "site": "BulldogJob",
    "role": "qa,tester",
    "lvl": "junior,medium",
    "city": "Remote,Gdańsk" 
}

justjoinit_settings = {
    "site": "JustjoinIt",
    "role": "testing",
    "lvl": "mid.senior",
    "city": "Gdańsk" 
}

base_logger.log.info("runner: Starting runner.")
# Create links
NOFLUFFJOBS_URL = common.createLinks(site=nofluffjobs_settings['site'], 
                                    role=nofluffjobs_settings['role'], 
                                    lvl=nofluffjobs_settings['lvl'], 
                                    city=nofluffjobs_settings['city'])
BULLDOGJOB_URL = common.createLinks(site=bulldogjob_settings['site'], 
                                    role=bulldogjob_settings['role'], 
                                    lvl=bulldogjob_settings['lvl'], 
                                    city=bulldogjob_settings['city'])
JUSTJOINIT_URL = common.createLinks(site=justjoinit_settings['site'],
                                    role=justjoinit_settings['role'],
                                    lvl=justjoinit_settings['lvl'],
                                    city=justjoinit_settings['city'])

# Run setup and scrappers
setup.run(EXCEL_NAME, NOFLUFFJOBS_SHEET, BULLDOGJOB_SHEET, JUSTJOINIT_SHEET)
nofluffjobs.run(NOFLUFFJOBS_SHEET, NOFLUFFJOBS_URL)
bulldogjob.run(BULLDOGJOB_SHEET, BULLDOGJOB_URL)
justjoinit.run(JUSTJOINIT_SHEET, JUSTJOINIT_URL)
base_logger.log.info("runner: Runner finished work.")
