from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/tanglong/Development/chromedriver"
TWITTER_URL = "https://twitter.com/"
SPEED_TEST_URL = "https://www.speedtest.net/"
EMAIL = "abc@gmail.com"
PW = "123"
USERNAME = "AbbCC"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        sleep(5)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        sleep(40)
        down_idx = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.down = down_idx.text
        print(f"Down: {self.down}")
        up_idx = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        self.up = up_idx.text
        print(f"Up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(5)
        login_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        login_button.click()
        sleep(5)
        email_input = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.ENTER)
        sleep(3)
        # unusal act
        username_input = self.driver.find_element_by_name("text")
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)

        sleep(3)
        pw_input = self.driver.find_element_by_name(
            "password")
        pw_input.send_keys(PW)
        pw_input.send_keys(Keys.ENTER)

        sleep(5)
        ##typing##
        tweet_inbox = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_inbox.send_keys(
            f"Hi Carry Telecom, my download speed is {self.down} and upload speed is {self.up}.")
        sleep(1)
        send_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        send_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
