import json
import os
import smtplib
import time

import requests
from bs4 import BeautifulSoup


def check_price():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    price = soup.find_all(class_='_1vC4OE _3qQ9m1')

    price = int(price[0].text[1:].replace(',', ''))

    if(price < settings['COST_YOU_AFFORD']):
        send_mail(price)


def send_mail(price):

    USER_NAME = settings['USER_NAME']
    PASSWORD = settings['USER_PASS']
    FROM_ADDRS = settings['FROM_ADDRS']
    TO_ADDRS = settings['TO_ADDRS']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(USER_NAME, PASSWORD)

    msg = f'Price Dropped to {price}\nCheck the link below\n{URL}'

    server.sendmail(FROM_ADDRS, TO_ADDRS, msg)

    print(f'\n\nPrice dropped to {price}\nMail Sent to {TO_ADDRS}')


if __name__ == '__main__':
    with open('settings.json', 'r') as file:
        settings = json.load(file)

    URL = settings["URL"]

    os.system('cls')
    while True:
        check_price()
        time.sleep(60*60)
