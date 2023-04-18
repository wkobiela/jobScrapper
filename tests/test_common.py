import os
import sys
import pytest
sys.path.insert(0, f'{os.getcwd()}\\modules')

from common import replaceChars, getDomainName

strings_list = [
    ('[test','test'),
    ('test]', 'test'),
    ("'test", "test"),
    ('test\\xa0', 'test'),
    ('\\ntest', 'test')
]

@pytest.mark.parametrize('in_put, out_put', strings_list)
def test_replace_chars_back_square_brackets(in_put, out_put):
    assert replaceChars(in_put) == out_put

    
urls_list = [
    ('https://nofluffjobs.com/pl/testing?criteria=employment%3Db2b%20%20seniority%3Djunior', 'https://nofluffjobs.com'),
    ('https://bulldogjob.pl/companies/jobs/s/city,Remote/role,tester', 'https://bulldogjob.pl'),
    ('https://justjoin.it/api/offers', 'https://justjoin.it')
]
    
@pytest.mark.parametrize('in_put, out_put', urls_list)    
def test_getDomainName_urls(in_put, out_put):
    assert getDomainName(in_put) == out_put