from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

EMAIL = "abc@gmail.com"
PW = "123"
driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://tinder.com")
login_button = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login_button.click()
time.sleep(3)
fb_login = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]")
fb_login.click()
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
email_input = driver.find_element_by_xpath(
    '//*[@id="email"]')
pw_input = driver.find_element_by_xpath(
    '//*[@id="pass"]')
# driver.quit()
time.sleep(3)
email_input.send_keys(EMAIL)
pw_input.send_keys(PW)
pw_input.send_keys(Keys.ENTER)
time.sleep(2)
continue_button = driver.find_element_by_xpath(
    '//*[@id="mount_0_0_0F"]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span/span')
continue_button.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
# Allow location
allow_location_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
