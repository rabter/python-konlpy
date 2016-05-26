from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()

pprint(kkma.sentences(u'네, 안녕하세요. 의류매장 입니다'));
pprint(kkma.nouns(u'구입하실 물건 있으시면 말씀해주세요.'));
pprint(kkma.pos(u'하하하 즐거운 쇼핑입니다.'));
