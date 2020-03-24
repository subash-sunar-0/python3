from selenium import webdriver
from selenium.webdriver.common.keys import *


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')

        email = bot.find_element_by_name('******')
        password = bot.find_element_by_name('*****')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)

ed = TwitterBot('use your username' , 'use your oun password')
ed.login()
