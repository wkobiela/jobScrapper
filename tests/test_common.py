import os, sys
import pytest
sys.path.insert(0, f'{os.getcwd()}\\modules')

from common import replace_chars, getDomainName

strings_list = [
    ('[test','test'),
    ('test]', 'test'),
    ("'test", "test"),
    ('test\\xa0', 'test'),
    ('\\ntest', ('test'))
]

@pytest.mark.parametrize('input, output', strings_list)
def test_replace_chars_back_square_brackets(input, output):
    assert replace_chars(input) == output

    
urls_list = [
    ('https://nofluffjobs.com/pl/testing?criteria=employment%3Db2b%20%20seniority%3Djunior', 'https://nofluffjobs.com'),
    ('https://bulldogjob.pl/companies/jobs/s/city,Remote/role,tester', 'https://bulldogjob.pl'),
    ('https://justjoin.it/api/offers', 'https://justjoin.it')
]
    
@pytest.mark.parametrize('input, output', urls_list)    
def test_getDomainName_urls(input, output):
    assert getDomainName(input) == output