#run pip install selenuim for webdriver stuff
#needs geckodriver in you py path
#play with the timer delays to avoid getting detected
#some hashtags doesn't actually exist in IG 
# or maybe they're filtered so make sure the hashtag exists otherwise you are getting a 404
#have fun

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class AssellBot:
    def __init__(self,username,password):#__construct
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def pressLike(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag)
        time.sleep(5)
        for i in range(1,4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            posts = bot.find_elements_by_css_selector('.v1Nh3 a')
            links = [elem.get_attribute('href') for elem in posts]
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_class_name('dCJp8').click()
                    time.sleep(5)
                except Exception as ex :
                    print(ex)
                    break

ass = AssellBot('usernameGoesHere','passwordGoesHere')#enter your uid n pwd here
ass.login()
ass.pressLike('aesthetics')#your hashtag
