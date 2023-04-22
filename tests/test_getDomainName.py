import pytest
from modules.common import replaceChars, getDomainName

job_urls_list = [
    ('https://nofluffjobs.com/pl/testing?criteria=employment%3Db2b%20%20seniority%3Djunior', 'nofluffjobs.com'),
    ('https://bulldogjob.pl/companies/jobs/s/city,Remote/role,tester', 'bulldogjob.pl'),
    ('https://justjoin.it/api/offers', 'justjoin.it'),
    ('https://work4.dev/search/testing/', 'work4.dev'),
    ('https://devhunt.pl/lista-ofert?&specialisms=qa', 'devhunt.pl'),
    ('https://www.startupjobs.com/jobs/development/testing', 'www.startupjobs.com'),
    ('https://teamquest.pl/praca-w-it/k/test', 'teamquest.pl'),
    ('https://4programmers.net/Praca?q=tester', '4programmers.net')
]
    
@pytest.mark.parametrize('in_put, out_put', job_urls_list)    
def test_getDomainName_job_urls(in_put, out_put):
    assert getDomainName(in_put) == out_put
    
    
random_urls_list = [
    ('https://google.com/?utm_source=google-PL&utm_medium=referral&utm_campaign=hp-footer&fg=1', 'google.com'),
    ('https://www.facebook.com/policies_center/', 'www.facebook.com'),
    ('https://twitter.com/settings/cookie_preferences', 'twitter.com'),
    ('https://instagram.com/581066165581870/', 'instagram.com'),
    ('https://en.wikipedia.org/wiki/Mae_West', 'en.wikipedia.org'),
    ('https://www.tiktok.com/feedback', 'www.tiktok.com'),
    ('https://www.linkedin.com/learning/search?trk=guest_homepage', 'www.linkedin.com'),
    ('https://www.reddit.com/t/doja_cat/', 'www.reddit.com'),
    ('https://openai.com/about', 'openai.com'),
    ('https://dzen.ru/discover?searchfocus=1', 'dzen.ru'),
    ('https://www.bing.com/images/feed?form=Z9LH', 'www.bing.com'),
    ('https://vk.com/terms', 'vk.com'),
    ('https://www.samsung.com/pl/smartphones/', 'www.samsung.com'),
    ('https://weather.com/pl-PL/pogoda/weekend/l/e378104195bfa014e2b0c38805f60e755ec19a1d03be8cd16098478fc2ca26c3', 'weather.com'),
    ('https://twitch.tv/p/pl-pl/security/', 'twitch.tv'),
    ('https://bilibili.com/v/ent/fans/?spm_id_from=333.1007.0.0', 'bilibili.com'),
    ('https://microsoft.com/pl-pl/windows/?r=1', 'microsoft.com'),
    ('https://zoom.us/pl/pricing', 'zoom.us'),
    ('https://qq.com/ch/games/', 'qq.com'),
    ('https://quora.com/about/tos', 'quora.com'),
    ('https://msn.com/pl-pl/motoryzacja?ocid=hpmsn&cvid=027fa0ca882c4942857a42c31b25ff86&ei=10', 'msn.com'),
    ('https://fandom.com/topics/anime', 'fandom.com'),
    ('https://aajtak.in/entertainment', 'aajtak.in'),
]

@pytest.mark.parametrize('in_put, out_put', random_urls_list)    
def test_getDomainName_random_urls(in_put, out_put):
    assert getDomainName(in_put) == out_put