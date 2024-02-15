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

def test_createExcel_throws_ValueError():
    with pytest.raises(ValueError):
        t1.createExcelFile(5, 'just', 'bull', 'noffuff')
        
def test_createExcel_throws_TypeError():
    with pytest.raises(TypeError):
        t1.createExcelFile('test.xlsx', 4, 'bull', 'noffuff')

def test_createExcel_throws_TypeError2():
    with pytest.raises(TypeError):
        t1.createExcelFile('test.xlsx', 'just', 1, 'noffuff')
        
def test_createExcel_throws_TypeError3():
    with pytest.raises(TypeError):
        t1.createExcelFile('test.xlsx', 'just', 'bull', 4)   