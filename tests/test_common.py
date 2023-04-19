import os
import sys
import pytest
sys.path.insert(0, f'{os.getcwd()}\\modules')

from common import replaceChars, getDomainName

strings_list = [
    ('[test','test'), ('test]', 'test'), ("'test", "test"), ('test\\xa0', 'test'), ('\\ntest', 'test'),
    ("p{'}'A~;qI", 'p{}A~;qI'), ('=(:B;GsKtw', '=(:B;GsKtw'), ('E!fv<bKvgS', 'E!fv<bKvgS'), 
    ("p{'}'A~;qI", "p{}A~;qI"), ("=(:B;GsKtw", "=(:B;GsKtw"), ("E!fv<bKvgS", "E!fv<bKvgS"),
    ("!d8(IcRhy*", "!d8(IcRhy*"), ("3dyg>\\xa0Qhw%", "3dyg>Qhw%"), ("%73e.g4j50", "%73e.g4j50"),
    ("7+HEJCpWWA", "7+HEJCpWWA"), ("DzE]wVK~>g", "DzEwVK~>g"), ("Ew\\xa0p5GHIN9", "Ewp5GHIN9"),
    ("HP;Sp2!â„–b8", "HP;Sp2!â„–b8"), ("Pij^T5^W~Y", "Pij^T5^W~Y"), ("PxGBr<#-!X", "PxGBr<#-!X"),
    ("xh~e<#'bwi", "xh~e<#bwi"), ("Zfâ„–Y-dli>i", "Zfâ„–Y-dli>i"), ("TUlHp!*yzh", "TUlHp!*yzh"),
    ("bU{DRDGtpi", "bU{DRDGtpi"), ("Yoâ„–'MOyZt~", "Yoâ„–MOyZt~"), ("0?`]2CSG'}", "0?`2CSG}"),
    ("N%RibO%v\\xa0a", "N%RibO%va"), (":zd6L{M+XO", ":zd6L{M+XO"), ("@q!?27B<Ge", "@q!?27B<Ge"),
    ("H#}.Z0AT-U", "H#}.Z0AT-U"), ("7*`UK{W<sK", "7*`UK{W<sK"), ("TWw+<oD]h'", "TWw+<oDh"), 
    ("s993B>=`*8", "s993B>=`*8"), ("a-Y#5;s5â„–'", "a-Y#5;s5â„–"), ("<8(W@0\\xa0Lâ„–)", "<8(W@0\Lâ„–)"), 
    ("PE%VQJ%^d;", "PE%VQJ%^d;"), ("dMhz8A:A.C", "dMhz8A:A.C"), ("7rj[?~62S`", "7rj?~62S`"), 
    ("n@z}5Y^kO7", "n@z}5Y^kO7"), (".TD}S.r@`h", ".TD}S.r@`h"), ("S5>FU0w<b%", "S5>FU0w<b%"), 
    ("b?t3-6Mz1S", "b?t3-6Mz1S"), ("LTxC5!:DoV", "LTxC5!:DoV"), ("o(&c<H;0Jo", "o(&c<H;0Jo"),
    ("bsclsEN^ws", "bsclsEN^ws"), ("X-qd6IVIl<", "X-qd6IVIl<"), ("};E3cZ+ycL", "};E3cZ+ycL"), 
    ("yIP7~Tw4mk", "yIP7~Tw4mk"), ("5%U+e+â„–Ust", "5%U+e+â„–Ust"), (">NovH)4xMO", ">NovH)4xMO"), 
    ("aCtzqnq[\\xa0W", "aCtzqnqW"), ("2OPM\\xa0+dmo`", "2OPM+dmo`"), ("SbbTy;l<9p", "SbbTy;l<9p"), 
    ("BK-.R9?ifI", "BK-.R9?ifI"), ("'B*#(qEQlH", "B*#(qEQlH"), ("@DMA(QWv34", "@DMA(QWv34"), 
    ("WQ}%9bCc?X", "WQ}%9bCc?X"), ("U<&ZT~H}0;", "U<&ZT~H}0;"), ("[I`t2Xmr2U", "I`t2Xmr2U"), 
    ("-okvjU3SWZ", "-okvjU3SWZ"), ("(Tr{?7f=>g", "(Tr{?7f=>g"), (";H}4Tb%Pa:", ";H}4Tb%Pa:"),
    ("pâ„–GR{NcT*:", "pâ„–GR{NcT*:"), ("0%QFNh0dQ9", "0%QFNh0dQ9"), ("r`9h?W;7'x", "r`9h?W;7x"),
    ("d%+2=r?â„–M7", "d%+2=r?â„–M7"), ("4Ci]54Pi!s", "4Ci54Pi!s"), ("i!~iIJ?~E(", "i!~iIJ?~E("),
    ("XVT.Pf9kch", "XVT.Pf9kch"), ("JwC:Qâ„–\\xa0Qp}", "JwC:Qâ„–Qp}"), ("^g6UOâ„–JFpE", "^g6UOâ„–JFpE"),
    ("rnaDLt7oN9", "rnaDLt7oN9"), ("zLAj6o7brs", "zLAj6o7brs"), ("yM]l@beL@M", "yMl@beL@M"), 
    ("\\nX(;UTqso<", "X(;UTqso<"), ("?+t)}'Ptmg", "?+t)}Ptmg"), ("7s}zn5r[^5", "7s}zn5r^5"), 
    ("aKlimbnsM#", "aKlimbnsM#"), ("?AxWmN=xA8", "?AxWmN=xA8"), ("lZA7.5(TLT", "lZA7.5(TLT"), 
    ("[Pa8vN=VZ9", "Pa8vN=VZ9"), ("1.cB8%x)!n", "1.cB8%x)!n"), ("bX4Y70#'mS", "bX4Y70#mS"),
    ("BBxAC4Gh:u", "BBxAC4Gh:u"), ("Afcp]>U[C?", "Afcp>UC?"), ("7?-JF}iM(G", "7?-JF}iM(G"), 
    ("Zp9(C0g!{4", "Zp9(C0g!{4"), ("g+sv\\xa0oi&Uc", "g+svoi&Uc"), ("~kTV@.+w7+", "~kTV@.+w7+"), 
    ("{27^I9'{#N", "{27^I9{#N"), ("WEuK%<3U'7", "WEuK%<3U7"), ("d;{KjV]@l6", "d;{KjV@l6"), 
    ("YJv6Q;pvR9", "YJv6Q;pvR9"), (";2TMzGâ„–Ax0", ";2TMzGâ„–Ax0")
]

@pytest.mark.parametrize('in_put, out_put', strings_list)
def test_replace_chars(in_put, out_put):
    assert replaceChars(in_put) == out_put

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
    
    
    
# with open("C:\\Users\\Wiktor Kobiela\\Documents\\GIT projects\\jobScrapper\\tests\\data.txt") as d:
#     lines = [line.rstrip() for line in d]
#     replaced = []
#     for line in lines:
#         replaced.append(replaceChars(line))    

# res = "\n".join('''("{}", "{}"),'''.format(x, y) for x, y in zip(lines, replaced))
# print(res)