from flask import Flask, request, jsonify
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

country_dic = {'가봉': [
    'https://www.0404.go.kr/m/dev/country_view.do?idx=2&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
    'http://overseas.mofa.go.kr/ga-ko/index.do',
    'https://www.0404.go.kr/new_osm/index.jsp?a1=1315939.878958&a2=-73379.547154&a3=7&a4='],
    '감비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=5&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1707297.463778&a2=1518039.381744&a3=9&a4='],
    '과테말라': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=7&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-10067673.869497&a2=1785568.980742&a3=8&a4='],
    '그리스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=11&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2475336.723987&a2=4774562.534805&a3=6&a4='],
    '기니': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=13&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1230330.407278&a2=1196086.618606&a3=7&a4='],
    '기니비사우': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=14&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1660823.75058&a2=1355228.511496&a3=8&a4='],
    '나미비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=15&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ao-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1917652.165619&a2=-2573176.120192&a3=5&a4='],
    '나이지리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=18&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ng-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=885446.535655&a2=1071341.388445&a3=6&a4='],
    '남아프리카공화국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=20&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/za-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2768854.912602&a2=-3365675.229453&a3=6&a4='],
    '네덜란드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=21&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/nl-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=621280.165902&a2=6858541.673972&a3=6&a4='],
    '네팔': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=22&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/np-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=9373014.156441&a2=3262943.863438&a3=7&a4='],
    '노르웨이': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=23&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/no-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1506726.701557&a2=9871995.077087&a3=4&a4='],
    '뉴질랜드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=25&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/nz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=19391768.327836&a2=-5126784.361143&a3=4&a4='],
    '니제르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=27&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ci-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1076233.358255&a2=2010599.592013&a3=6&a4='],
    '니카라과': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=28&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ni-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-9458623.628121&a2=1384427.456301&a3=7&a4='],
    '덴마크': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=31&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/dk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1066449.418635&a2=7597229.11532&a3=6&a4='],
    '도미니카공화국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=33&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/do-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-7844273.590738&a2=2153689.708963&a3=8&a4='],
    '독일': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=34&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/de-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1149612.905409&a2=6648186.972131&a3=5&a4='],
    '라오스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=36&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/la-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11422749.506937&a2=2186710.505182&a3=6&a4='],
    '라이베리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=37&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ng-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1054219.494109&a2=682429.78853&a3=7&a4='],
    '러시아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=39&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ru-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=10879740.857999&a2=9470853.552646&a3=3&a4='],
    '레바논': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=40&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/lb-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3977782.951961&a2=4019976.191574&a3=9&a4='],
    '루마니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=43&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ro-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2778638.852223&a2=5752956.496856&a3=6&a4='],
    '르완다': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=45&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/rw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3344884.357759&a2=-220138.641461&a3=9&a4='],
    '리히텐슈타인': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=48&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ch-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1063391.937503&a2=5967591.67228&a3=10&a4='],
    '마다가스카르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=49&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5214839.817728&a2=-2162250.656131&a3=6&a4='],
    '말라위': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=55&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/zw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=&a2=&a3=&a4='],
    '말레이시아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=56&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/my-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=12117409.219992&a2=401141.524441&a3=6&a4='],
    '말리': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=57&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-313086.067856&a2=1844272.618465&a3=6&a4='],
    '멕시코': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=58&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mx-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-11271098.442819&a2=2563392.180572&a3=5&a4='],
    '모로코': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=60&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ma-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-726457.516822&a2=3779046.678419&a3=6&a4='],
    '모리셔스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=61&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=6415818.406145&a2=-2299225.810818&a3=9&a4='],
    '모리타니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=62&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ma-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1132491.011073&a2=2301671.795723&a3=6&a4='],
    '모잠비크': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=63&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3918467.818011&a2=-2128006.867459&a3=6&a4='],
    '몰도바': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=65&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ua-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3189564.316284&a2=5987771.047748&a3=6&a4='],
    '몽골': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=68&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11466777.235229&a2=5860579.832681&a3=4&a4='],
    '미국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=69&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/us-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-10860172.978758&a2=4647371.319739&a3=4&a4='],
    '미얀마': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=75&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mm-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=10664494.186348&a2=2044843.380685&a3=5&a4='],
    '방글라데시': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=82&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bd-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=10052997.960066&a2=2739503.093741&a3=7&a4='],
    '베네수엘라': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=85&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ve-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-7377090.473859&a2=748471.380968&a3=6&a4='],
    '베트남': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=86&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/vn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11863026.789859&a2=1976355.803342&a3=5&a4='],
    '벨기에': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=87&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/be-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=495311.943288&a2=6535671.666496&a3=8&a4='],
    '보츠와나': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=91&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/za-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2612311.878674&a2=-2504688.542849&a3=5&a4='],
    '볼리비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=92&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bo-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-7227885.394646&a2=-1854056.558085&a3=6&a4='],
    '부룬디': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=93&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/rw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3331431.440781&a2=-388300.103689&a3=9&a4='],
    '부르키나파소': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=94&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ci-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-203016.747125&a2=1372197.531775&a3=7&a4='],
    '불가리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=98&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2822666.580515&a2=5258867.54602&a3=6&a4='],
    '브라질': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=104&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/br-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6017122.866609&a2=-1496942.761937&a3=4&a4='],
    '브루나이': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=105&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=12753365.295325&a2=503872.890456&a3=8&a4='],
    '사우디아라비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=107&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sa-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5028944.964938&a2=2798206.731464&a3=5&a4='],
    '사모아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=112&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/nz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-19142277.867513&a2=-1548308.444945&a3=8&a4='],
    '세네갈': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=114&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1604566.097762&a2=1627802.954361&a3=7&a4='],
    '소말리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=120&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ke-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5361598.912035&a2=574806.452705&a3=6&a4='],
    '수단': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=122&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sd-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3390135.078504&a2=1800244.890172&a3=6&a4='],
    '스리랑카': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=124&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/lk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=8977987.594264&a2=867101.648867&a3=8&a4='],
    '에스와티니': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=125&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'https://overseas.mofa.go.kr/mz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3509988.338855&a2=-3064819.086122&a3=8&a4='],
    '스웨덴': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=126&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/se-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1858948.527895&a2=9275174.760236&a3=4&a4='],
    '스위스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=127&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ch-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=929474.263948&a2=5924175.440214&a3=6&a4='],
    '스페인': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=128&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/es-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-435385.313112&a2=4862617.99139&a3=6&a4='],
    '슬로바키아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=129&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2093763.078788&a2=6203017.719399&a3=6&a4='],
    '슬로베니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=130&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/at-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1663269.735485&a2=5782308.315717&a3=7&a4='],
    '시리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=131&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/lb-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4326947.297167&a2=4167958.278334&a3=7&a4='],
    '싱가포르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=134&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11561559.150303&a2=150733.819778&a3=9&a4='],
    '아랍에미리트': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=135&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ae-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=6075826.504332&a2=2744395.063551&a3=6&a4='],
    '아르헨티나': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=138&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ar-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-7347738.654997&a2=-4686507.078221&a3=4&a4='],
    '아이슬란드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=139&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/no-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-2049735.350495&a2=9568692.948852&a3=5&a4='],
    '아일랜드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=141&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ie-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-880554.565845&a2=7005300.76828&a3=6&a4='],
    '알제리': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=150&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/dz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=273950.309374&a2=3306971.59173&a3=5&a4='],
    '앙골라': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=151&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ao-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1927436.105239&a2=-1350183.667629&a3=6&a4='],
    '에스토니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=154&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fi-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2871586.278618&a2=8130453.824638&a3=6&a4='],
    '에콰도르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=155&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ec-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8766409.89997&a2=-154097.049023&a3=7&a4='],
    '에티오피아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=156&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/et-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4334285.251883&a2=958826.082809&a3=6&a4='],
    '엘살바도르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=157&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sv-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-9889116.971423&a2=1534855.527966&a3=9&a4='],
    '영국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=159&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gb-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-229922.581082&a2=7240115.319172&a3=6&a4='],
    '오만': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=162&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/om-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=6281289.236363&a2=2284549.901387&a3=5&a4='],
    '오스트리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=163&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/at-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1594782.158142&a2=6046474.685471&a3=6&a4='],
    '온두라스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=164&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/hn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-9646964.465816&a2=1682837.614726&a3=8&a4='],
    '요르단': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=165&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/jo-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4072564.867034&a2=3664085.387878&a3=7&a4='],
    '우간다': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=166&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ug-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3634733.569017&a2=156543.033928&a3=7&a4='],
    '우루과이': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=167&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/uy-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6212801.659019&a2=-3835304.331237&a3=6&a4='],
    '우즈베키스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=168&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/uz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=7132491.983346&a2=5048512.844179&a3=6&a4='],
    '우크라이나': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=169&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ua-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3507542.35395&a2=6256829.387311&a3=6&a4='],
    '이라크': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=174&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/iq-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4862617.99139&a2=3884224.02934&a3=6&a4='],
    '이란': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=176&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ir-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5924175.440214&a2=3864656.150099&a3=5&a4='],
    '이스라엘': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=177&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/il-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3903791.908581&a2=3755809.82182&a3=7&a4='],
    '이집트': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=178&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/eg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3419486.897366&a2=3121076.73894&a3=6&a4='],
    '이탈리아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=179&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/it-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1389319.426111&a2=5293111.334692&a3=5&a4='],
    '인도네시아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=181&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/id-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=13130046.970714&a2=-498980.920646&a3=5&a4='],
    '일본': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=183&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/jp-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=15571139.90603&a2=4476152.37638&a3=5&a4='],
    '잠비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=186&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/zw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3160212.497422&a2=-1545862.460039&a3=5&a4='],
    '적도기니': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=187&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gq-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1059111.463919&a2=269058.339564&a3=8&a4='],
    '중국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=189&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11642888.148398&a2=3991847.365165&a3=4&a4='],
    '중앙아프리카공화국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=190&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cm-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2289441.871198&a2=719119.562107&a3=6&a4='],
    '지부티': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=191&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/et-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4739095.753681&a2=1317468.619523&a3=9&a4='],
    '짐바브웨': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=193&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/zw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3331431.440781&a2=-2172034.595752&a3=6&a4='],
    '체코': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=195&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1702405.493967&a2=6413372.421239&a3=6&a4='],
    '칠레': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=197&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cl-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-7895639.273746&a2=-4148390.399093&a3=3&a4='],
    '카메룬': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=199&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cm-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1396657.380827&a2=814512.973407&a3=6&a4='],
    '카보베르데': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=200&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-2617203.848484&a2=1707297.463778&a3=7&a4='],
    '카자흐스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=201&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/kz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=7611905.024751&a2=6144314.081676&a3=4&a4='],
    '카타르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=202&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/qa-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5699144.828943&a2=2891154.157859&a3=7&a4='],
    '캐나다': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=204&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ca-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-12288628.163351&a2=8296780.798186&a3=2&a4='],
    '케냐': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=206&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ke-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4211986.006626&a2=56257.652818&a3=6&a4='],
    '코스타리카': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=209&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-9368122.186631&a2=1085405.80165&a3=8&a4='],
    '코트디부아르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=212&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ci-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-616388.196092&a2=821850.928122&a3=7&a4='],
    '콜롬비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=213&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/co-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8101102.005776&a2=401141.524441&a3=5&a4='],
    '콩고': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=214&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://congo.mofa.go.kr/korean/af/congo/main/index.jsp',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1790460.950552&a2=-51365.683008&a3=6&a4='],
    '콩고민주공화국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=215&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cd-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2680799.456018&a2=-254382.430133&a3=6&a4='],
    '쿠웨이트': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=216&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/kw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5293111.334692&a2=3421932.882271&a3=9&a4='],
    '크로아티아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=218&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/hr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=707297.463778&a2=5611089.372358&a3=6&a4='],
    '탄자니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=225&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3972279.485924&a2=-763147.290399&a3=6&a4='],
    '터키': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=228&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3982063.425545&a2=4745210.715944&a3=6&a4='],
    '통가': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=230&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/nz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=20037508.342789&a2=-2406849.146644&a3=9&a4='],
    '튀니지': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=233&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tn-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1076233.358255&a2=4011415.244406&a3=6&a4='],
    '파나마': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=235&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pa-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8916837.971636&a2=934977.729984&a3=8&a4='],
    '파라과이': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=237&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/py-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6408480.451429&a2=-2661231.576777&a3=6&a4='],
    '파키스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=239&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=7846719.575643&a2=3600489.780345&a3=6&a4='],
    '파푸아뉴기니': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=240&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=16378314.924721&a2=-694659.713056&a3=5&a4='],
    '페루': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=243&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pe-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8296780.798186&a2=-1134936.995978&a3=5&a4='],
    '포르투갈': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=244&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-860986.686604&a2=4833266.172528&a3=5&a4='],
    '폴란드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=246&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pl-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2191602.474993&a2=6858541.673972&a3=5&a4='],
    '프랑스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=248&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=332653.947097&a2=5968203.168507&a3=5&a4='],
    '피지': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=249&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=19890749.248482&a2=-1951895.95429&a3=7&a4='],
    '핀란드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=251&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fi-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3013453.403115&a2=9803507.499744&a3=4&a4='],
    '필리핀': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=252&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ph-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=13707299.408324&a2=1318385.863863&a3=5&a4='],
    '헝가리': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=254&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/hu-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2211170.354234&a2=5948635.289266&a3=4&a4='],
    '호주': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=255&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/au-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=564616.631434&a2=-5185487.998866&a3=3&a4='],
    '사이프러스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=258&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3725235.010506&a2=4170404.263239&a3=7&a4='],
    '캄보디아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=259&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/kh-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11699145.801216&a2=1413779.275163&a3=7&a4='],
    '태국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=260&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/th-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=11227070.714527&a2=1538524.505324&a3=6&a4='],
    '아프가니스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=284&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/af-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=7416226.232341&a2=4040767.063268&a3=6&a4='],
    '인도': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=285&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/in-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=8854465.356555&a2=2563392.180572&a3=5&a4='],
    '세르비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=287&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/rs-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2313901.720249&a2=5459438.30824&a3=6&a4='],
    '바레인': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=288&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bh-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5626911.837213&a2=3005503.952173&a3=11&a4='],
    '베냉': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=289&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gh-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=259274.399943&a2=1017529.720532&a3=6&a4='],
    '몬테네그로': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=290&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/rs-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2132898.83727&a2=5278435.425261&a3=7&a4='],
    '세이셸': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=291&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/et-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=6183449.840158&a2=-511210.845171&a3=9&a4='],
    '시에라리온': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=292&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ng-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-1320831.848768&a2=953934.112999&a3=8&a4='],
    '예멘': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=294&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ye-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5332247.093174&a2=1790460.950552&a3=7&a4='],
    '차드': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=295&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/cm-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2083979.139167&a2=1741541.252449&a3=5&a4='],
    '토고': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=296&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gh-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=122299.245256&a2=963718.05262&a3=6&a4='],
    '몰타': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=297&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/it-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1609458.067573&a2=4282919.568875&a3=10&a4='],
    '보스니아-헤르체고비나': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=298&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/hr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1980024.780699&a2=5460661.300693&a3=8&a4='],
    '산마리노': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=299&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/it-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1385650.448754&a2=5453323.345978&a3=11&a4='],
    '알바니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=300&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2233184.21838&a2=5041174.889464&a3=6&a4='],
    '키르기스스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=301&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/kg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=8365268.37553&a2=5107216.481902&a3=7&a4='],
    '타지키스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=302&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=7939667.002038&a2=4681615.10841&a3=7&a4='],
    '동티모르': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=304&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tl-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=14025277.44599&a2=-981451.443182&a3=9&a4='],
    '나우루': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=306&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=18579701.339334&a2=-68487.577344&a3=13&a4='],
    '마셜제도': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=307&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=&a2=&a3=&a4='],
    '마이크로네시아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=308&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=&a2=&a3=&a4='],
    '몰디브': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=309&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/lk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=8107216.968039&a2=320424.022571&a3=7&a4='],
    '바누아투': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=310&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=18721568.463832&a2=-1971463.833531&a3=6&a4='],
    '솔로몬제도': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=311&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=17660011.015007&a2=-949042.143189&a3=5&a4='],
    '키리바시': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=312&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-17508359.950889&a2=220138.641461&a3=10&a4='],
    '투발루': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=313&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fj-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=19949452.886205&a2=-939258.203568&a3=11&a4='],
    '팔라우': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=314&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ph-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=14977377.070311&a2=831634.867743&a3=8&a4='],
    '가이아나공화국': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=315&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ve-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6557685.530642&a2=555238.573464&a3=6&a4='],
    '그레나다': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=316&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6848757.734352&a2=1390848.166677&a3=9&a4='],
    '바베이도스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=318&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6618835.15327&a2=1477374.882696&a3=10&a4='],
    '벨리즈': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=319&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sv-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-9876887.046897&a2=1932328.075049&a3=7&a4='],
    '세인트키츠네비스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=320&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/do-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6972891.468287&a2=1948226.976933&a3=9&a4='],
    '세인트루시아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=321&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6790054.096629&a2=1594782.158142&a3=10&a4='],
    '세인트빈센트그레나딘': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=322&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6821851.900395&a2=1440073.612893&a3=8&a4='],
    '수리남': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=323&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ve-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6203017.719399&a2=459845.162164&a3=6&a4='],
    '아이티': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=324&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/do-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8096210.035966&a2=2141459.784437&a3=8&a4='],
    '앤티가바부다': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=325&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/do-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6881778.530571&a2=1957399.420327&a3=9&a4='],
    '자메이카': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=326&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/jm-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8608643.87359&a2=2057684.801437&a3=8&a4='],
    '쿠바': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=327&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mx-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8805545.658452&a2=2494904.603228&a3=5&a4='],
    '트리니다드토바고': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=328&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tt-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6838973.794731&a2=1178964.724271&a3=9&a4='],
    '부탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=329&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bd-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=10079903.794023&a2=3172442.421948&a3=7&a4='],
    '쿡제도': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=330&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/nz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-17787202.230074&a2=-2421525.056074&a3=7&a4='],
    '코모로': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=331&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/mg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4828374.202718&a2=-1315939.878958&a3=8&a4='],
    '조지아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=332&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ge-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4799022.383857&a2=5168366.10453&a3=7&a4='],
    '벨라루스': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=333&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/by-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3135752.648371&a2=7117816.073916&a3=5&a4='],
    '아르메니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=334&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ru-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5008154.093245&a2=4885854.847988&a3=8&a4='],
    '아제르바이잔': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=335&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/az-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=5327355.123364&a2=4913983.674397&a3=8&a4='],
    '룩셈부르크': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=337&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/be-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=681206.796077&a2=6410926.436334&a3=9&a4='],
    '에리트레아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=338&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/sd-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=4446800.557518&a2=1663269.735485&a3=7&a4='],
    '바하마': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=339&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/do-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-8668570.503765&a2=2807990.671084&a3=7&a4='],
    '안도라': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=340&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/es-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=176110.913169&a2=5245414.629042&a3=10&a4='],
    '모나코': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=341&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/fr-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=&a2=&a3=&a4='],
    '라트비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=344&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/se-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2754179.003171&a2=7731758.285102&a3=6&a4='],
    '리투아니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=345&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/pl-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2673461.501302&a2=7435794.111582&a3=7&a4='],
    '투르크메니스탄': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=366&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tm-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=6623727.12308&a2=4740318.746133&a3=6&a4='],
    '코소보': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=367&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/at-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=2327966.133453&a2=5247249.117721&a3=9&a4='],
    '북마케도니아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=368&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/bg-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=&a2=&a3=&a4='],
    '도미니카연방': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=369&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/do-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-6824297.885301&a2=1736649.282639&a3=10&a4='],
    '레소토': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=370&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/za-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3144313.595539&a2=-3447615.723775&a3=8&a4='],
    '상투메프린시페': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=371&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ga-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=786995.643224&a2=116795.77922&a3=8&a4='],
    '대만': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=372&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/tw-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=13452916.978191&a2=2710151.274879&a3=6&a4='],
    '남수단': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=373&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ug-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=3390135.078504&a2=794945.094166&a3=6&a4='],
    '리비아': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=375&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/ly-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=1981247.773152&a2=3086832.950269&a3=6&a4='],
    '홍콩(중국)': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=377&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/hk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=12699553.627412&a2=2543824.301331&a3=5&a4='],
    '마카오(중국)': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=378&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/hk-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=&a2=&a3=&a4='],
    '니우에': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=380&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'https://overseas.mofa.go.kr/nz-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-18907463.316621&a2=-2167142.625941&a3=11&a4='],
    '가나': [
        'https://www.0404.go.kr/m/dev/country_view.do?idx=390&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
        'http://overseas.mofa.go.kr/gh-ko/index.do',
        'https://www.0404.go.kr/new_osm/index.jsp?a1=-117407.275446&a2=919690.324327&a3=6&a4='],
}


@app.route('/hello', methods=['POST'])
def post():
    content = request.get_json()
    content = content['action']['params']
    content = content['country']

    webSiteList = list(country_dic.get(content))

    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": content,
                        "description": "{} 갈거임?".format(content),
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "국가별 페이지 링크",
                                "webLinkUrl": webSiteList[0]
                            },
                            {
                                "action": "webLink",
                                "label": "대사관링크",
                                "webLinkUrl": webSiteList[1]
                            },
                            {
                                "action": "webLink",
                                "label": "여행경보 지도 링크",
                                "webLinkUrl": webSiteList[2]
                            },
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
