#This is all project from Day31 - Day45
-------------------------------------------

Proeject List in order by Learning Day:

1. Flashy(Tkinter)(Pandas)
2. Birthday Mail sending (SMTP Library)
3. ISS Program (API)
4. Quiz Game (API)
5. Rain Alert SMS Program (API)
6. Stock Monitoring SMS Alert Program (API)
7. Pixela (API)
8. Google sheet workout tracker (API)
9. Flight Club (Capstone)
10. Scrapping Top 100 Movie (BeautifulSoup)



Concepts Used in Day31 - Day45
--------------------------------

Comprehension
---------------------
**LIST**
```
[new for new in list]
```
**old method**
```
numbers = [1, 2, 3]
new_list = []
for x in numbers;
	add_1 = n + 1
	new_list.append(add_1)
```
**New Method**
```
numbers = [1, 2, 3]
new_list = [n + 1 for x in number]

name = "Angela"
new_numbers = [n for n in numbers]
print(new_numbers)
```
**List Comprehension with if Statement**
```
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

short_name = [n for n in names if len(n) < 5]
print(short_name)
```
**DICTIONARY**
```
new_dict = {new_key:new_value for item in list if test}
new_dict = {new_key:new_value for (key, value} in dict.items() if test}
```
```
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

##
{'Alex': 22, 'Beth': 42, 'Caroline': 13, 'Dave': 89, 'Eleanor': 11}
```
```
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

student_scores = {name: random.randint(1, 100) for name in names}

passed_students = {
    k: v for (k, v) in student_scores.items() if v >= 60}

print(passed_students)
```
```
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {x: len(x) for x in sentence.split()}
print(result)
```
```
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# (temp_c * 9/5) + 32 = temp_f

# Write your code 👇 below:
weather_f = {day: ((value * 9/5) + 32) for (day, value) in weather_c.items()}


print(weather_f)
```
Pandas with Dictionary
------------------------
```
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

student_data = pandas.DataFrame(student_dict)

for (index, row) in student_data.iterrows():
    print(row)

###
student    Angela
score          56
Name: 0, dtype: object
student    James
score         76
Name: 1, dtype: object
student    Lily
score        98
Name: 2, dtype: object
```
**CSV to Dict**
```
import pandas as pd

data = pd.read_csv(
    "nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in data.iterrows()}
```
GUI Tkinter
---------------------
```
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
label_1 = Label(text="Label", font=("Arial", 24, "bold"))
label_1.pack()
label_1["text"] = "Try Click"
label_1.config(text="Try Click")


# button

def button_clicked():
    label_1["text"] = input.get()
    label_1.config(text=input.get())
    print("Hi")


button = Button(text="Click", command=button_clicked)
button.pack()

# Entry

input = Entry(width=50)
input.pack()

window.mainloop()
```
**Tkinter Widget Example**
```
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
```
**Canvas Widget**
```
canvas = Canvas(width=200, height=224)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
canvas.create_text(103, 130, text="00: 00", font=(FONT_NAME, 35, "bold"))
canvas.pack()
```
Advance Keyword Arguement
--------------------------
```
def function(a=5, b=6, c=7)

def add(n1, n2):
	return n1 + n2

##TO

def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)
```
Python Dynamic Typing
-----------------------
python strongly type and hold on, but dynamic type = dynamic change the type instantly
```
a = "abc" ##type = string
a = 4 ##type changed to Int
```

Try & Error
-----------------------
1. try
2. except
3. else
4. finally

```
try:
    file = open("data.txt")
    a = {"key": "value"}
    print(a["key"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
```
```
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0


print(total_likes)
```
Saving JSON Data （javaScriptObjectNotation)
-------------------------
```
json.dump() # Write
json.load() # Read
json.update() # Update
```

SMTP
-----------------------
```
import smtplib

my_email = "ptesting977@gmail.com"
password = "Qpzm9099099"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email,
                    to_addrs="tledmund0921@gmail.com", msg="Subject:hello\n\nThis is the body of my email")

connection.close()
```
Datetime Module
-------------------
```
import datetime as dt

current = dt.datetime.now()
year = current.year
month = current.month
day_of_week = current.weekday()

date_of_birth = dt.datetime(year=1998, month=9, day=21, hour=4)
print(date_of_birth)
```
**Exercise: Send Random Quote email**
```
import smtplib
import datetime as dt
import random


def sending_mail(quote):
    my_email = "ptesting977@gmail.com"
    password = "Qpzm9099099"
    message = quote
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="tledmund0921@gmail.com", msg=f"Subject:hello\n\n{message}")

    connection.close()


current = dt.datetime.now()
day_of_week = current.weekday()

quotes = open("quotes.txt")
quotes_list = quotes.readlines()

rd_quote = random.choice(quotes_list)
if day_of_week == 2:
    sending_mail(rd_quote)
```

**Format Date**
```
from datetime import datetime
today = datetime.now()

yyyymmdd = today.strftime("%Y%m%d")
```
API
----------
set of commands, functions, protocols, and objects that programmer can use.

Your program → API (Request) → External Program

Read API Document

API Endpoint:

location of data saved

e.g. [api.coinbase.com](http://api.coinbase.com) ← location of coinbase data

**API Request**
```
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]
print(data)
longitude = data["iss_position"]["longtitude"]
latitude = data["iss_position"]["latitude"]
```
**API Parameters**
```
import requests
from datetime import datetime
MY_LAT = 43.651890
MY_LONG = -79.381710
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()["iss_position"]
# print(data)
# longitude = data["iss_position"]["longtitude"]
# latitude = data["iss_position"]["latitude"]

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}
response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)
```
HTML Escape
-----------
```
import html

html.unescape()
```
API Authentication
-----------------------
**API KEY**
```
import requests
api_key = "4afb2423e9abb6458f97a66af8c60801"

api = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url=api, params=weather_params)
response.raise_for_status()
```

Environment Variables
---------------------
for Convenience, security (dont save API Keys on web)

save the important variables such as API KEY...etc to environment

and use os.environ.get(””) to get them
```
for Convenience, security (dont save API Keys on web)

save the important variables such as API KEY...etc to environment

and use os.environ.get(””) to get them
```
HTTP POST REQUEST
--------------------
```
import requests

requests.get()
requests.post() # save data to API
requests.put() # update some data in API
requests.delete() #delete data


## HEADER API TOKEN
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)
```

Beautiful Soup
---------------
```
from bs4 import BeautifulSoup
with open("html") as files:
	content = files.read()


## deep inside of html
soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.name)

all_anchor = soup.find_all(name="a")

for tag in all_anchor:
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

heading = soup.find(name="h3", class_="heading")
print(heading.getText())

company_url = soup.select_one(selector="#name")
print(company_url)
```
```
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
```





