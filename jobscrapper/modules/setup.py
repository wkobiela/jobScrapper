import os
import logging
import pandas as pd
from unidecode import unidecode
from jobscrapper.modules.common import checkFileExistance

log = logging.getLogger(__name__)

class Setup():
    
    def __init__(self):
        
        self.json_config = \
            '''{
    "excel_settings": {
        "EXCEL_NAME": "jobs.xlsx",
        "NOFLUFFJOBS_SHEET": "NoFluffJobs",
        "BULLDOGJOB_SHEET": "BulldogJob",
        "JUSTJOINIT_SHEET": "JustJoinIt"
    },
        "search_params": {
            "nofluffjobs_settings": {
                "site": "NoFluffJobs",
                "role": "testing",
                "lvl": "junior,mid",
                "city": "Gdańsk"
            },
            "bulldogjob_settings": {
                "site": "BulldogJob",
                "role": "qa,tester",
                "lvl": "junior,medium",
                "city": "Remote,Gdańsk"
            },
            "justjoinit_settings": {
                "site": "JustjoinIt",
                "role": "testing",
                "lvl": "mid.senior",
                "city": "Gdańsk"
            }
    }
}'''
        
    def createExcelFile(self, filename, sheetname1, sheetname2, sheetname3):
        try:
            log.debug("setup:createExcelFile: Creating xlsx file for storage.")
            data_frame1 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'LOKALIZACJA':[], 'DODANE':[]})
            data_frame2 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'INFO OGÓLNE':[], 'DODANE':[]})
            data_frame3 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'LOKALIZACJA':[], 'DODANE':[]})

            # create a excel writer object
            with pd.ExcelWriter(filename) as writer:
                data_frame1.to_excel(writer, sheet_name=sheetname1, index=False)
                data_frame2.to_excel(writer, sheet_name=sheetname2, index=False)
                data_frame3.to_excel(writer, sheet_name=sheetname3, index=False)
        except Exception as ex:
            log.error('setup:createExcelFile: Exception: %s', ex)
            raise
        
    def checkExcel(self, filename, sheetname1, sheetname2, sheetname3):
        try:
            with open(filename, 'rb') as f:
                reader = pd.ExcelFile(f)
                if not all(x in [sheetname1, sheetname2, sheetname3] for x in reader.sheet_names):
                    log.warning('setup:checkExcel: %s, %s or %s not in %s', 
                                sheetname1, sheetname2, sheetname3, reader.sheet_names)
                    log.warning('setup:checkExcel: No valid worksheets in %s', reader.sheet_names)
                    return False
                return True
        except FileNotFoundError:
            log.error('setup:checkExcel: File %s not found!', filename)
            return False
        
    def createConfigJson(self, filename):
        try:
            if type(filename) != str:
                raise ValueError('The input is not a string.')
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(unidecode(self.json_config))
        except Exception as ex:
            log.error('setup:createConfigJson: Exception: %s.', ex)
            raise

def run(filename, sheetname1, sheetname2, sheetname3): # pragma: no cover
    setup = Setup()        
    if checkFileExistance(filename) is False:
        setup.createExcelFile(filename, sheetname1, sheetname2, sheetname3)
    else:
        log.debug('setup:run: File %s exists. Checking sheetnames.', filename)
        out = setup.checkExcel(filename, sheetname1, sheetname2, sheetname3)
        if out is not True:
            log.debug("setup:run: Backing up old excel and creating fresh one.")
            os.rename(filename, 'backup_'+filename)
            setup.createExcelFile(filename, sheetname1, sheetname2, sheetname3)
        else:
            log.debug("setup:run: Excel file passed validation. Proceeding.")
            