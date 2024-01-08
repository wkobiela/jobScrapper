import os
import sys
import pandas as pd
from modules.base_logger import log
from .common import checkFileExistance

class Setup():
    def createExcelFile(self, filename, sheetname1, sheetname2, sheetname3):
        try:
            log.info("setup:createExcelFile: Creating xlsx file for storage.")
            data_frame1 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'LOKALIZACJA':[], 'DODANE':[]})
            data_frame2 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'INFO OGÓLNE':[], 'DODANE':[]})
            data_frame3 = pd.DataFrame({'LINK': [], 'OPIS':[], 'FIRMA':[], 'ZAROBKI':[], 'LOKALIZACJA':[], 'DODANE':[]})
            log.info("setup:createExcelFile: data frames created.")

            # create a excel writer object
            with pd.ExcelWriter(filename) as writer:
                log.info("setup:createExcelFile: inside pd.ExcelWriter")
                data_frame1.to_excel(writer, sheet_name=sheetname1, index=False)
                data_frame2.to_excel(writer, sheet_name=sheetname2, index=False)
                data_frame3.to_excel(writer, sheet_name=sheetname3, index=False)
        except Exception as ex:
            log.error(f"setup:createExcelFile: Exception: {ex}.")
            sys.exit()
        
    def checkExcel(self, filename, sheetname1, sheetname2, sheetname3):
        try:
            with open(filename, 'rb') as f:
                reader = pd.ExcelFile(f)
                if not all(x in [sheetname1, sheetname2, sheetname3] for x in reader.sheet_names):
                    log.warning(f"setup:checkExcel: {[sheetname1, sheetname2, sheetname3]} not in {reader.sheet_names}")
                    log.warning(f"setup:checkExcel: No valid worksheets in {reader.sheet_names}")
                    return False
                return True
        except FileNotFoundError:
            log.error(f"setup:checkExcel: File {filename} not found!")
            return False

def run(filename, sheetname1, sheetname2, sheetname3):
    setup = Setup()        
    if checkFileExistance(filename) is False:
        setup.createExcelFile(filename, sheetname1, sheetname2, sheetname3)
    else:
        log.info(f"setup:run: File {filename} exists. Checking sheetnames.")
        out = setup.checkExcel(filename, sheetname1, sheetname2, sheetname3)
        if out is not True:
            log.info("setup:run: Backing up old excel and creating fresh one.")
            os.rename(filename, 'backup_'+filename)
            setup.createExcelFile(filename, sheetname1, sheetname2, sheetname3)
        else:
            log.info("setup:run: Excel file passed validation. Proceeding.")
            