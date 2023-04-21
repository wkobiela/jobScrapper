import os
import sys
import pytest
sys.path.insert(0, f'{os.getcwd()}')

from modules.setup import Setup

t1 = Setup()

@pytest.fixture
def test_setup_correct(autouse=True):
    t1.createExcelFile('jobs.xlsx', 'NoFluffJobs', 'BulldogJob', 'JustJoinIt')
    yield
    os.remove('jobs.xlsx')

def test_checkExcel_file_is_correct(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') == True
    
def test_checkExcel_file_is_correct2(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'JustJoinIt', 'NoFluffJobs', 'BulldogJob') == True
    
def test_checkExcel_file_is_correct3(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'BulldogJob', 'JustJoinIt', 'NoFluffJobs') == True   

def test_checkExcel_file_is_not_correct(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'JustJoinIt') == False

def test_checkExcel_file_is_not_correct2(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'JustJoinIt') == False
    
def test_checkExcel_file_is_not_correct3(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'Other') == False

def test_checkExcel_file_is_not_correct_(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') == False

def test_checkExcel_file_is_not_correct_2(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') == False
    
def test_checkExcel_file_is_not_correct_3(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'Other') == False
    
def test_checkExcel_wrong_file_wrong_sheets(test_setup_correct):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') == False
    
def test_checkExcel_wrong_file_correct_sheets(test_setup_correct):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') == False    