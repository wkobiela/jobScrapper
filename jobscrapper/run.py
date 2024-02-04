import argparse
import json

from jobscrapper.scrappers import justjoinit
from jobscrapper.scrappers import nofluffjobs
from jobscrapper.scrappers import bulldogjob
from jobscrapper.modules import setup, common, base_logger


def main():
    program_description = '''
    jobScrapper -  Simplify your IT job search.
    How to use: https://github.com/wkobiela/jobScrapper/blob/master/README.md'''
    
    yaml = setup.Setup()
    if common.checkFileExistance('config.json') is False:
        yaml.createConfigJson('config.json')
    
    parser = argparse.ArgumentParser(description=program_description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--config", help="Path to the configuration file", required=True)
    args = parser.parse_args()
    
    try:
        with open(args.config, 'r') as configuration:
            config = json.load(configuration)
    except FileNotFoundError as e:
        base_logger.log.error(e)
        exit(1)

    # Excel settings
    EXCEL_NAME = config['excel_settings']['EXCEL_NAME']
    NOFLUFFJOBS_SHEET = config['excel_settings']['NOFLUFFJOBS_SHEET']
    BULLDOGJOB_SHEET = config['excel_settings']['BULLDOGJOB_SHEET']
    JUSTJOINIT_SHEET = config['excel_settings']['JUSTJOINIT_SHEET']

    # Search params
    nofluffjobs_settings = config['search_params']['nofluffjobs_settings']
    bulldogjob_settings = config['search_params']['bulldogjob_settings']
    justjoinit_settings = config['search_params']['justjoinit_settings']

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

if __name__ == "__main__":
    main()
