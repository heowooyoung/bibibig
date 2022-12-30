# utils.py

import requests
import random

token = '5894130618:AAGJznYZbowFq1ZrsOj4oWpR7NRVO7qbO80'
me = '765946187'

def send_message(msg, sender_id):
    token = '5894130618:AAGJznYZbowFq1ZrsOj4oWpR7NRVO7qbO80'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={sender_id}&text={msg}'
    requests.get(url)


# if __name__ == '__main__':
#     send_message('안녕', '765946187')

'''
https://api.telegram.org/bot5894130618:AAGJznYZbowFq1ZrsOj4oWpR7NRVO7qbO80/setWebhook?url=eduneo.pythonanywhere.com
'''