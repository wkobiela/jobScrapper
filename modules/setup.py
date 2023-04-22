import os
import pandas as pd
from modules.base_logger import log
from .common import checkFileExistance

class Setup():
    def createExcelFile(self, filename, sheetname1, sheetname2, sheetname3):
        try:
            log.info("Creating xlsx file for storage.")
            data_frame1 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'LOKALIZACJA':[], 'DODANE':[]})
            data_frame2 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'INFO OGÓLNE':[], 'DODANE':[]})
            data_frame3 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'LOKALIZACJA':[], 'DODANE':[]})

            # create a excel writer object
            with pd.ExcelWriter(filename) as writer:
                data_frame1.to_excel(writer, sheet_name=sheetname1, index=False)
                data_frame2.to_excel(writer, sheet_name=sheetname2, index=False)
                data_frame3.to_excel(writer, sheet_name=sheetname3, index=False)
        except Exception as ex:
            log.error(f"Failed with exception {ex}.")
        
    def checkExcel(self, filename, sheetname1, sheetname2, sheetname3):
        try:
            with open(filename, 'rb') as f:
                reader = pd.ExcelFile(f)
                if not all(x in [sheetname1, sheetname2, sheetname3] for x in reader.sheet_names):
                    log.warning(f"{[sheetname1, sheetname2, sheetname3]} not in {reader.sheet_names}")
                    log.warning(f"No valid worksheets in {reader.sheet_names}")
                    return False
                return True
        except FileNotFoundError:
            log.error(f"File {filename} not found!")
            return False

def run(filename, sheetname1, sheetname2, sheetname3):
    setup = Setup()        
    if checkFileExistance(filename) is False:
        log.info("Creating xlsx file for storage.")
        setup.createExcelFile(filename, sheetname1, sheetname2, sheetname3)
    else:
        log.info(f"File {filename} exists. Checking sheetnames.")
        out = setup.checkExcel(filename, sheetname1, sheetname2, sheetname3)
        if out is not True:
            log.info("Backing up old excel and creating fresh one.")
            os.rename(filename, 'backup_'+filename)
            setup.createExcelFile(filename, sheetname1, sheetname2, sheetname3)
        else:
            log.info("Excel file passed validation. Proceeding.")
            