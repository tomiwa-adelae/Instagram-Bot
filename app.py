from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(10)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_post(self, hastag):
        bot = self.bot
        bot.get('https://www.instagram.com/'+hastag+'/')
        time.sleep(10)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            posts = bot.find_elements_by_class_name('_9AhH0')

tom = InstagramBot('theemail', 'thepassword')
tom.login()
tom.like_post('wizkidayo')