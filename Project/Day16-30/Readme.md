#This is all project from Day16 - Day30
-------------------------------------------

Proeject List in order by Learning Day:

1. Coffee Machine Project (OOP)
2. Quiz Game (OOP)
3. Hirst dot painting (OOP)(Turtle Module)
4. Turtle Race (OOP)(Turtle Module)
5. Snake Game (OOP)(Turtle Module)
6. PING PONG(OOP)(Turtle Module)
7. Turtle Cross(OOP)(Turtle Module)
8. Mail Merge Project(File Management)
9. US State Game(Pandas)
10. NATO Alphabet Project(Pandas)
11. Miles to Km Converter (Tkinter)
12. Pomodoro Timer (Tkinter)(Math)
13. Password Manager (Tkinter)(pyperclip)
14. Password Manager (JSON)(Tkinter)(pyperclip)


Concepts Used in Day16 - Day30
--------------------------------

Dictionary
---------------
Dictionary are pair of **key** : **value**.
1 value with 1 key

Dictionary similar to a **table**:
------------------
| KEY   |   Value  |
-------------------

```
{key: value}
```
```
{"China": "Beijing"}
```

**Dictionary save in a *list* **
------------------
```
capital_list = {
 "China": "Beijing",
 "USA": "Washington",
 "Japan": "Tokyo"
}

print(capital_list["China"])
Output: Beijing
```
**How to add a new key into dictionary**
------------------
```
capital_list["UK"] = "London"
```
**Wipe Dictionary**
------------------
```
capital_list = {}
```
**Edit item in dictionary**
------------------
```
capital_list["key 1"] = "value 1"
```
**loop a dictionary**
------------------
```
for key in capital_list:
 print(key)
 print(capital[key])

Output:
-----------
China
Beijing
USA
Washington
-----------
```
**Fucntion with input**
------------------
```
def function(input):
print(input)

function(123)
```
output:
123

**Function with output**
------------------
```
def add(n1, n2):
 return n1 + n2

print(add(1, 2))
```
output
3

We can use **return** to save variables inside function

**Recursion**
------------------
call function inside the fucntion based on some conditions:
1. while loop with boolean (value of boolean in condition is useful)

**Scope**
-------------------
```
x = 1
def increase():
	 x = 2
	 print(f"x = {x}")

increcese() ## show x = 2
print(x)    ## show x = 1
```
**Local Scope**
local scope = within the functions
inside the function:
change of variable on happened in function **inside**
Only can use these variable inside the function

**Global Scope**
```
player_health = 10
def increase_potion():
 print(player_health)
```
1. player_health is on top level.
2. Because player_health not inside of function.

```
x = 1
def x_increase():
	global x
	x += 1
	print(x)
x_increase() ## x = 2
```
**O**bject **O**riented **P**rogramming - OOP
---------------------------------------------
[Python OOP.pdf](https://github.com/EdmundLT/U-Python-100-Days/files/8218832/Python.OOP.pdf)

**OOP Class Create**
[Python - Oop Create Class.pdf](https://github.com/EdmundLT/U-Python-100-Days/files/8218840/Python.-.Oop.Create.Class.pdf)
```
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1


user_1 = User("001", "Edmund")
user_2 = User("002", "JACK")

user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
```
Module
----------------------
**Import Module**
```
import turtle
from turtle import Turtle
from turtle import * ##<--- All
import turtle as t ##<----- t = turtle
```
**Create multiple objects**
```
new_object_list = []
for object in range(6):
	new_object = Turtle()
	new_object_list.append(new_object)
```

Reverse Range
---------------------
```
for x in range(start= 5, stop= 0, step= 1)

x = 5
x = 4
x = 3
x = 2
x = 1
x = 0
```
Class Inheritance
-----------------------
For example
```
Chef → Pastry Chef
P.Chef should have some attribute from Chef
```
```
class Animal():
	def__init__(self):
		self.num_eyes = 2

class Fish(Animal):
	def __init__(self):
		super().__init__()

a = Fish()
print(a.num_eyes)
```
```
output
2
```
Slicing List & Tuple (Important)
------------------------
```
piano_keys = [#0 a, #1 b, #2 c,#3 d,#4 e,#5 f,#6 g #7]

#slicing
print(piano_keys[2:5])
# = cut #2 to #5
#output
#[c, d, e]
print(piano_keys[:5])
# = #0 to # 5
#output
#[a, b, c ,d ,e]
print(piano_keys[2:5:2])
# = #2, #5, no #3 and #4
#output
#[c, e]
print(piano_keys[::2])
# = #0, #2, #4, #6
#output
#[a, c, e, g]
print(piano_keys[::-1]) #<---- -1 = reverse
#output
#[g, f, e, d, c, b, a]
```

File of Python
-----------------------
```
open(”xxx”):
 XXX = file.read()
```
```
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
```
**With Method**
```
with open("my_file.txt") as file:
	contents = file.read()
	print(contents)
#w= write; #a= append
with open("my_file.txt", mode="a"):
	file.write("abc")

#create a new file
with open("new_file.txt", mode="w"): 
	file.write("abc")
```
Read CSV Files
-------------------------------
```
import csv
with open("weather_data.csv") as data_files:
    data = csv.reader(data_files)
    for row in data:
        print(row)
```
Python Pandas
--------------------------------
Pandas Documentation: https://pandas.pydata.org/docs/reference/index.html

- Python Pandas [https://pandas.pydata.org/docs/reference/index.html](https://pandas.pydata.org/docs/reference/index.html)
```
import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].to_list()

# find the max
maxtem = data.temp.max()

#data in row
print(data[data.temp == maxtem])
```
Python Pandas create Dataframe from scratch
------------------------------
**create data frame from scratch**
```
import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

#create .csv file
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
```
Pandas scratch data (NY Park)
---------------------------------
```
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Counts": [grey_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("color_count.csv")
```
