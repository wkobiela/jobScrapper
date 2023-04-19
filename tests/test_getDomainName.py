import os
import sys
import pytest
sys.path.insert(0, f'{os.getcwd()}\\modules')

from common import replaceChars, getDomainName

urls_list = [
    ('https://nofluffjobs.com/pl/testing?criteria=employment%3Db2b%20%20seniority%3Djunior', 'https://nofluffjobs.com'),
    ('https://bulldogjob.pl/companies/jobs/s/city,Remote/role,tester', 'https://bulldogjob.pl'),
    ('https://justjoin.it/api/offers', 'https://justjoin.it'),
    ('https://work4.dev/search/testing/', 'https://work4.dev'),
    ('https://devhunt.pl/lista-ofert?&specialisms=qa', 'https://devhunt.pl'),
    ('https://www.startupjobs.com/jobs/development/testing', 'https://www.startupjobs.com'),
    ('https://teamquest.pl/praca-w-it/k/test', 'https://teamquest.pl'),
    ('https://4programmers.net/Praca?q=tester', 'https://4programmers.net')
]
    
@pytest.mark.parametrize('in_put, out_put', urls_list)    
def test_getDomainName_urls(in_put, out_put):
    assert getDomainName(in_put) == out_put