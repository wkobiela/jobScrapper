import os
import pytest
from jobscrapper.modules import common, setup

t1 = setup.Setup()
    
@pytest.fixture
def _test_create_excel():
    t1.createExcelFile('test.xlsx', 'just', 'bull', 'nofluff')
    yield
    os.remove('test.xlsx')
    

def test_createExcel_pass(_test_create_excel):
    assert common.checkFileExistance('test.xlsx') is True    

def test_createExcel_throws_exception():
    with pytest.raises(TypeError):
        t1.createExcelFile()
