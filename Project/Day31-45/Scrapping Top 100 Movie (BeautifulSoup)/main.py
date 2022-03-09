from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://news.ycombinator.com/")

yc_web_page = response.text
article_link = []
article_text = []
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(class_="titlelink", name="a")
for article_tag in articles:
    article_text.append(article_tag.getText())
    article_link.append(article_tag.get("href"))

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]

# print(article_link)
# print(article_text)

pos = article_upvotes.index(max(article_upvotes))
print(article_text[pos])
