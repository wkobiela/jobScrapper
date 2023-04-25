import os
import pytest
from modules.setup import Setup

t1 = Setup()

@pytest.fixture
def _test_setup_correct():
    t1.createExcelFile('jobs.xlsx', 'NoFluffJobs', 'BulldogJob', 'JustJoinIt')
    yield
    os.remove('jobs.xlsx')

def test_checkExcel_file_is_correct(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is True
    
def test_checkExcel_file_is_correct2(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'JustJoinIt', 'NoFluffJobs', 'BulldogJob') is True
    
def test_checkExcel_file_is_correct3(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'BulldogJob', 'JustJoinIt', 'NoFluffJobs') is True   

def test_checkExcel_file_is_not_correct(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'JustJoinIt') is False

def test_checkExcel_file_is_not_correct2(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'JustJoinIt') is False
    
def test_checkExcel_file_is_not_correct3(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_2(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'Other', 'Other') is False
    
def test_checkExcel_file_is_not_correct_3(_test_setup_correct):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_wrong_file_wrong_sheets(_test_setup_correct):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_wrong_file_correct_sheets(_test_setup_correct):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is False    
    
@pytest.fixture
def _test_setup_wrong_sheets():
    t1.createExcelFile('jobs.xlsx', 'NoFluff', 'Bulldog', 'JustJoin')
    yield
    os.remove('jobs.xlsx')

def test_checkExcel_file_is_correct_sheets_wrong(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is False
    
def test_checkExcel_file_is_correct_sheets_wrong2(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'JustJoinIt', 'NoFluffJobs', 'BulldogJob') is False
    
def test_checkExcel_file_is_correct_sheets_wrong3(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'BulldogJob', 'JustJoinIt', 'NoFluffJobs') is False   

def test_checkExcel_is_correct_sheets_wrong4(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'BulldogJob', 'JustJoinIt') is False

def test_checkExcel_is_correct_sheets_wrong5(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'JustJoinIt') is False
    
def test_checkExcel_is_correct_sheets_wrong6(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs.xlsx', 'Other', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_sheets_wrong(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'Other', 'Other') is False

def test_checkExcel_file_is_not_correct_sheets_wrong2(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'Other', 'Other') is False
    
def test_checkExcel_file_is_not_correct_sheets_wrong3(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_file_is_not_correct_sheets_wrong4(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'Other', 'BulldogJob', 'Other') is False
    
def test_checkExcel_file_is_not_correct_sheets_wrong5(_test_setup_wrong_sheets):
    assert t1.checkExcel('jobs_wrong.xlsx', 'NoFluffJobs', 'JustJoinIt', 'BulldogJob') is False   