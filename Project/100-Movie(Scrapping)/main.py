import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

txt_title = soup.title.getText()
movie_list = []
movie_titles = soup.find_all(class_="title", name="h3")
for title in movie_titles:
    movie_list.append(title.getText())
movie_list.reverse()

for x in range(0, len(movie_list)):
    with open(f"{txt_title}.txt", "a") as file:
        file.write(f"{movie_list[x]}\n")
