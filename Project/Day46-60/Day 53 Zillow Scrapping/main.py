from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep
GGL_FORM = "https://forms.gle/TPizEUhGQTE7FXZp6"
ZILLOW = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
driver_path = "/Users/tanglong/Development/chromedriver"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


class FindProperty():
    def __init__(self):
        self.address_list = []
        self.price_list = []
        self.link_list = []
        self.index = 0

    def scrap_data(self):
        response = requests.get(ZILLOW, headers=header)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        listings_links = soup.find_all(class_="list-card-link")
        listings_prices = soup.find_all(class_="list-card-price")
        listings_address = soup.find_all(class_="list-card-addr")
        for link in listings_links:
            self.link_list.append(link.get("href"))

        for price in listings_prices:
            x = price.getText()
            self.price_list.append(x)

        for add in listings_address:
            x = add.getText()
            self.address_list.append(x)

    def fill_form(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(GGL_FORM)
        for _ in range(len(self.address_list)):
            sleep(3)
            address_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

            price_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

            link_input = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

            address_input.send_keys(self.address_list[self.index])
            price_input.send_keys(self.price_list[self.index])
            link_input.send_keys(self.link_list[self.index])

            submit_button.click()
            sleep(3)
            another_response = self.driver.find_element_by_link_text(
                "Submit another response")
            another_response.click()
            self.index += 1
            sleep(2)


bot = FindProperty()
bot.scrap_data()
bot.fill_form()
