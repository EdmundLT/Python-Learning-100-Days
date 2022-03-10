import requests
from bs4 import BeautifulSoup
import lxml
from send_mail import send_email
URL = "https://www.amazon.ca/Protector-Addtam-Extension-Overload-Protection/dp/B08F58MXQG?ref_=Oct_DLandingS_D_a97292be_61&smid=A1BGDLOO430MHB"


headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = requests.get(url=URL, headers=headers)
raw_data = resp.text
soup = BeautifulSoup(raw_data, "lxml")
pd_name_data = soup.find(
    class_="a-size-large product-title-word-break", name="span")
pd_name = pd_name_data.get_text().split(",")[0]
price_data = soup.find(class_="a-offscreen", name="span")
float_price = float(price_data.get_text().split("$")[1])

mail_contents = f"Subject:Price of {pd_name} is drop\n\nPrice: ${float_price}\nURL: {URL}"
if float_price > 1:
    send_email(contents=mail_contents)
