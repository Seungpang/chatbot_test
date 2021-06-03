from flask import Flask, request, jsonify
from flask_restx import Api

import gspread

app = Flask(__name__)
api = Api(app)

gc = gspread.service_account(filename='key.json')

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/124H-71CHuUlOh-8c-w_I7Qh6lxc_esurq_fHjljvEjw/edit#gid=0'


@app.route('/response', methods=['POST'])
def post():
    content = request.get_json()
    content = content['action']['params']
    name = content['name']
    phone = content['phone']
    email = content['email']
    company = content['company']

    doc = gc.open_by_url(spreadsheet_url)
    worksheet = doc.worksheet('시트1')
    worksheet.insert_row([name, phone, email, company], 2)

    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "상담 신청이 완료되었습니다. 빠른 시일내에 연락드리겠습니다."
                    }
                }
            ]
        }
    }

    return jsonify(result)


@app.route('/agree', methods=['POST', 'GET'])
def agree_post():
    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "문의 신청을 하시겠습니까?"
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "네",
                    "action": "message",
                    "messageText": "입력받기"
                },
                {
                    "label": "아니요",
                    "action": "message",
                    "messageText": ""
                }
            ]
        }
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
