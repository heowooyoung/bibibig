import requests
import random

token = '5894130618:AAGJznYZbowFq1ZrsOj4oWpR7NRVO7qbO80'
me = '765946187'



while True:
    from time import sleep
    sleep(5)
    update_url = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(update_url).json()
    input_message = response['result'][-1]['message']['text']
    chat_id = response['result'][-1]['message']['from']['id']
    if input_message == '로또':
        output_message = random.sample(range(1, 46), 6)
    elif input_message == '안녕':
        output_message = '안녕하세요'
    else:
        output_message = '처리할수 없습니다 :('

    send_url =f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={output_message}'
    # 서버에 요청(URL)을 보낸다.
    requests.get(send_url)




# url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={me}&text={message}'

# requests.get(url)

'''
https://api.telegram.org
/bot5894130618:AAGJznYZbowFq1ZrsOj4oWpR7NRVO7qbO80
/sendMessage
?
chat_id=765946187
&
text=hi

https://api.telegram.org/bot5894130618:AAGJznYZbowFq1ZrsOj4oWpR7NRVO7qbO80/getUpdates
'''
