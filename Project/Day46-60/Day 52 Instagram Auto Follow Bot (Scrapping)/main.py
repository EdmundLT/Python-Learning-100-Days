from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = "YOUR INSTAGRAM USERNAME"
PW = "YOUR INSTAGRAM PASSWORD"
SIMILAR_ACCOUNT = ""  # Account you want to stalk
driver_path = "/Users/tanglong/Development/chromedriver"


class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        username_input = self.driver.find_element_by_name("username")
        pw_input = self.driver.find_element_by_name("password")
        username_input.send_keys(USERNAME)
        pw_input.send_keys(PW)
        pw_input.send_keys(Keys.ENTER)

        sleep(3)
        not_now_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()

        sleep(3)
        not_now_button2 = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now_button2.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span')
        followers.click()
        sleep(2)
        modal = modal = self.driver.find_element_by_css_selector('.isgrP')
        for i in range(1000):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    def follow(self):
        all_button = self.driver.find_elements_by_css_selector("li button")
        for button in all_button:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
