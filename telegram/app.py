from flask import Flask, request
import random 
from utils import send_message

app = Flask('hi')

@app.route('/', methods=['POST'])
def home():
    # 서버로서 우리가 받은 요청 => Server
    data = request.json
    input_message = data['message']['text']
    sender_id = data['message']['from']['id']
    
    if input_message == '안녕':
        send_message('안녕하세요', sender_id)
    elif input_message == '로또':
        lotto = random.sample(range(1, 46), 6)
        send_message(lotto, sender_id)
    else:
        send_message('안녕 로또 중에 하나만 입력하세요.', sender_id)

    return 'Hello Server!'


app.run(port=80, debug=True)