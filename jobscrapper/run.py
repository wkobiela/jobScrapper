import sys
import argparse
import logging
import json

from jobscrapper.scrappers import justjoinit
from jobscrapper.scrappers import nofluffjobs
from jobscrapper.scrappers import bulldogjob
from jobscrapper.modules import setup, common


def main():
    program_description = '''
    jobScrapper -  Simplify your IT job search.
    to see help and all options, use "jobscrapper --help"
    readme: https://github.com/wkobiela/jobScrapper/blob/master/README.md'''
    
    parser = argparse.ArgumentParser(description=program_description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--config", help="path to the configuration file", required=False)
    parser.add_argument("--init", help="create initial config.json file, if no custom is delivered", 
                        required=False, 
                        action="store_true")
    parser.add_argument("--loglevel", help="set the loglevel from INFO, DEBUG (default INFO)", 
                        required=False, 
                        default='INFO')
    args = parser.parse_args()
    
    if args.loglevel not in ('INFO', 'DEBUG'):
        print("Invalid loglevel. Valid loglevels are 'INFO' and 'DEBUG'. Setting default as INFO.")
        args.loglevel = 'INFO'
    
    if args.loglevel == 'INFO':
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler()
            ]
        )
    
    if args.loglevel == 'DEBUG':
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler("debug.log"),
                logging.StreamHandler()
            ]
        )
    
    log = logging.getLogger(__name__)
    
    if args.init:
        yaml = setup.Setup()
        log.debug("runner: Creating initial config.json file")
        if common.checkFileExistance('config.json') is False:
            yaml.createConfigJson('config.json')
            log.info("runner: Initial config.json file successfully created.")
        else:
            log.info("runner: config.json file already exists.")
        if args.config is None:
            sys.exit(0)
    
    if args.config is None:
        print(program_description)
        sys.exit(1)
        
    try:
        with open(args.config, 'r', encoding="utf-8") as configuration:
            config = json.load(configuration)
    except FileNotFoundError as e:
        log.error(e)
        sys.exit(1)
        
    

    # Excel settings
    EXCEL_NAME = config['excel_settings']['EXCEL_NAME']
    NOFLUFFJOBS_SHEET = config['excel_settings']['NOFLUFFJOBS_SHEET']
    BULLDOGJOB_SHEET = config['excel_settings']['BULLDOGJOB_SHEET']
    JUSTJOINIT_SHEET = config['excel_settings']['JUSTJOINIT_SHEET']

    # Search params
    nofluffjobs_settings = config['search_params']['nofluffjobs_settings']
    bulldogjob_settings = config['search_params']['bulldogjob_settings']
    justjoinit_settings = config['search_params']['justjoinit_settings']

    log.info("runner: Starting runner.")
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
    log.info("runner: Runner finished work.")

if __name__ == "__main__":
    main()
