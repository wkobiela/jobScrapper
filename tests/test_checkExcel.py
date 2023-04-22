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
    assert t1.checkExcel('jobs.xlsx', 'JustJoinIt', 'NoFluffJobs', 'BulldogJob') is True
    
def test_checkExcel_file_is_correct3(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'BulldogJob', 'JustJoinIt', 'NoFluffJobs') is True   

def test_checkExcel_file_is_not_correct(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'JustJoinIt') is False

def test_checkExcel_file_is_not_correct2(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'JustJoinIt') is False
    
def test_checkExcel_file_is_not_correct3(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_2(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') is False
    
def test_checkExcel_file_is_not_correct_3(test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_wrong_file_wrong_sheets(test_setup_correct):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_wrong_file_correct_sheets(test_setup_correct):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is False    
    
@pytest.fixture
def test_setup_wrong_sheets(autouse=True):
    t1.createExcelFile('jobs.xlsx', 'NoFluff', 'Bulldog', 'JustJoin')
    yield
    os.remove('jobs.xlsx')

def test_checkExcel_file_is_correct_sheets_wrong(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is False
    
def test_checkExcel_file_is_correct_sheets_wrong2(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'JustJoinIt', 'NoFluffJobs', 'BulldogJob') is False
    
def test_checkExcel_file_is_correct_sheets_wrong3(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'BulldogJob', 'JustJoinIt', 'NoFluffJobs') is False   

def test_checkExcel_is_correct_sheets_wrong4(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'JustJoinIt') is False

def test_checkExcel_is_correct_sheets_wrong5(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'JustJoinIt') is False
    
def test_checkExcel_is_correct_sheets_wrong6(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_sheets_wrong(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_sheets_wrong2(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'Other', 'Other') is False
    
def test_checkExcel_file_is_not_correct_sheets_wrong3(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_file_is_not_correct_sheets_wrong4(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_file_is_not_correct_sheets_wrong(test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is False   