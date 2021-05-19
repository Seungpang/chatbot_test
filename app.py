import json

from flask import Flask, request, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/hello', methods=['POST'])
def post():
    content = request.get_json()
    content = content['action']['params']
    content = content['country']

    country_dic = {'가봉': ['https://www.0404.go.kr/m/dev/country_view.do?idx=2&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0', 'http://overseas.mofa.go.kr/ga-ko/index.do', 'https://www.0404.go.kr/new_osm/index.jsp?a1=1315939.878958&a2=-73379.547154&a3=7&a4='],
                   '감비아': [
                       'https://www.0404.go.kr/m/dev/country_view.do?idx=5&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
                       'http://overseas.mofa.go.kr/sn-ko/index.do',
                       'https://www.0404.go.kr/new_osm/index.jsp?a1=-1707297.463778&a2=1518039.381744&a3=9&a4='],
                   '과테말라': [
                       'https://www.0404.go.kr/m/dev/country_view.do?idx=7&hash=&chkvalue=no1&pagenum=1&stext=&group_idx=&alert_level=0',
                       'http://overseas.mofa.go.kr/gt-ko/index.do',
                       'https://www.0404.go.kr/new_osm/index.jsp?a1=-10067673.869497&a2=1785568.980742&a3=8&a4=']
                   }

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
    app.run(debug=True, host='localhost', port=8080)
