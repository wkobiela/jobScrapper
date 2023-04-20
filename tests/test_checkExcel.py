import os
import sys
import pytest
sys.path.insert(0, f'{os.getcwd()}')

from modules.setup import Setup


t1 = Setup()

@pytest.mark.parametrize("sheetname1", ['NoFluffJobs'])
@pytest.mark.parametrize("sheetname2", ['JustJoinIt'])
@pytest.mark.parametrize("sheetname3", ['BulldogJob'])
def test_checkExcel_file_is_correct(sheetname1, sheetname2, sheetname3):
    assert t1.checkExcel('jobs.xlsx', sheetname1, sheetname2, sheetname3) == True


def test_checkExcel_file_is_not_correct():
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'JustJoinIt') == False

def test_checkExcel_file_is_not_correct2():
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'JustJoinIt') == False
    
def test_checkExcel_file_is_not_correct3():
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'Other') == False

def test_checkExcel_file_is_not_correct_():
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') == False

def test_checkExcel_file_is_not_correct_2():
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') == False
    
def test_checkExcel_file_is_not_correct_3():
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'Other') == False