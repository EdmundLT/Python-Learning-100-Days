import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ACC = ""
PW = ""
driver_path = "/Users/tanglong/Development/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(5)
username = driver.find_element_by_xpath(
    "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
password = driver.find_element_by_xpath(
    "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
username.send_keys(ACC)
password.send_keys(PW)
password.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
