import os
import pytest
from jobscrapper.modules import common, setup

t1 = setup.Setup()

@pytest.fixture
def _test_create_config():
    t1.createConfigJson('config.json')
    yield
    os.remove('config.json')
    
def test_createConfig(_test_create_config):
    assert common.checkFileExistance('config.json') is True
    
def test_createConfig_throws_exception():
    with pytest.raises(TypeError):
        t1.createConfigJson()