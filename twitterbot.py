from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class Twitterbot:

    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot

        bot.get('https://twitter.com/login')
        time.sleep(3)

        email = bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        password = bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

        email.send_keys(self.email)
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def retweet(self, hashtag):
        bot = self.bot

        bot.get('https://twitter.com/search?q=%23'+hashtag+'&src=typed_query&f=live')
        time.sleep(3)

        links = set() #using set so that only unique links are present and to avoid unnecessary repeatation

        # obtaining the links of the tweets to retweet
        for i in range(300):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)') # using js to scroll the webpage
            time.sleep(4)
            [links.add(elem.get_attribute('href')) for elem in bot.find_elements_by_xpath("//a[@dir='auto']")]

        #traversing through the generated links
        for link in links:
            bot.get(link)
            time.sleep(4)

            try:
                bot.find_element_by_css_selector('.css-18t94o4[data-testid="retweet"]').click()
                actions = ActionChains(bot)
                actions.send_keys(Keys.RETURN).perform()
                time.sleep(10)
            except Exception as e:
                time.sleep(2)

        bot.get('https://twitter.com/')
