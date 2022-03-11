## #This is all project from Day46 - Day60

Proeject List in order by Learning Day:

1. Scrapping Billboard Top 100 to Spotify(BeautifulSoup)(Spotipy)
2. Scrapping Amazon Price Python Bot(Scrapping)
3. Instagram Auto Follow Bot (Scrapping)
4. Higher Lower (Flask)
5. name-card (flask)
6. Blog Capstone Project Part1

## Concepts Used in Day46 - Day60

## Selenium

```
from selenium import webdriver


driver_path = "/Users/tanglong/Development/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.python.org/")
event_list = []
for x in range(1, 6):
    data = driver.find_elements_by_xpath(
        f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{x}]")
    data_pair = data[0].text
    event_list.append(data_pair.split("\n"))

driver.quit()
data_dict = {}
for x in range(len(event_list)):
    for y in event_list:
        data_dict[x] = {
            "date": y[0],
            "event name": y[1],
        }


print(data_dict)
```

**.click()**

```
from selenium import webdriver
driver_path = "/Users/tanglong/Development/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num_articles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
num_articles = driver.find_element_by_css_selector("#articlecount a")
num_articles.click()

driver.quit()
```

**input something**

```
from selenium.webdriver.common.keys import Keys

email_input.send_keys(EMAIL)
pw_input.send_keys(PW)
pw_input.send_keys(Keys.ENTER)
```

**switch window**

```
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
```

## Command Line

```
#pwd = print working drive
#ls = list out current files and folders
#cd = goto
#mkdir xxx = create new folders
#touch xxx = create file
#rm xxx = delete file
#cd .. = go back one step
#rm -rf delete folder
```

## Flask (Back-end)

**basic**

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

#$ export FLASK_APP=hello.py
#$ python -m flask run
#* Running on http://127.0.0.1:5000/
```

**basic code to run Flask**

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return "bye!"


if __name__ == "__main__":
    app.run()
```

**app.route**

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return 'bye!'


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"hello {name}, You are {number} years lod!!"


if __name__ == "__main__":
    app.run(debug=True)
```

**Rendering HTML using Flask**

```
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1> ' \
        '<p>Paragraph</p>' \
        '<img src="https://c.tenor.com/ZhfMGWrmCTcAAAAM/cute-kitty-best-kitty.gif">'
```

```
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/angela')
def angela():
    return render_template("angela.html")


if __name__ == "__main__":
    app.run(debug=True)
```

**Flask Form request**

```
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form["username"]
    pw = request.form["password"]
    return f"<h1>Name: {name}, Password: {pw}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
```

**HTML**

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Title</title>
  </head>
  <body>
    <form action="/login" method="post">
      <label>Name</label>
      <input type="text" placeholder="name" name="username" />
      <label>Password</label>
      <input type="text" placeholder="password" name="password" />
      <button type="submit">Ok</button>
    </form>
  </body>
</html>
```

## Flask Form

```
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
```

**HTML**

```
<form method="POST" action="{{ url_for('login') }}">
        {{ form.csrf_token }}
        <p>
          {{ form.email.label }} <br />
          {{ form.email(size=30) }} {% for err in form.email.errors %}
          <span style="color: red">{{ err }}</span>
          {% endfor %}
        </p>
        <p>
          {{ form.password.label }} <br />
          {{ form.password(size=30) }} {% for err in form.email.errors %}
          <span style="color: red">{{ err }}</span>
          {% endfor %}
        </p>
        {{ form.submit }}
      </form>
```

## Python Decorators

@ ← add new functions to existing functions

```
from time import sleep


def decorator_function(function):
    def wrapper_function():
        sleep(2)
				#do something before
        function()
				#do something after
    return wrapper_function

@decorator_function
def say_hello():
    print("hello")
```

**Exercise:**

```
import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapped():
        start = time.time()
        function()
        end = time.time()
        print(f"{function.__name__} run speed: {end - start}s")
    return wrapped


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
```

**Argument and keyword inside function decorator**

```
class User:
	def __init(self, name):
		self.name = name
		self.logged_in = False

def is_auth_decorator(function):
	def wrapper(*args, **kwargs):
		if args[0].logged_in = True
			function(args[0])
	return wrapper

@is_auth_decorator
def create_blog_post(user):
	print(f"This is {user.name}'s new blog post.")


new_user = User("Edmund")
new_user.logged_in = True
create_blog_post(new_user)
```

**Exercise**

```
# Create the logging_decorator() function 👇

def logging_decorator(fnc):
    def wrapped(*args):
        result = fnc(args[0], args[1], args[2])
        print(f"You called {fnc.__name__}:{args}")
        print(f"It returned: {result}")
    return wrapped

# Use the decorator 👇


@logging_decorator
def a_function(*args):
    ans = 0
    for x in args:
        ans += x
    return ans


a_function(1, 2, 3)
```
Nested Fucntions
-----
```
def outer_function():
	print("Outer")
	def inner_fucntion():
		print("Inner")
	innter_function()
```
**return function in function**
```
def outer_function():
	print("Outer")
	def inner_fucntion():
		print("Inner")
	return inner_function

inner_function = outer_function()
inner_function()
```
OUTPUT:
Outer
Inner

![image](https://user-images.githubusercontent.com/98913678/157964258-e3868826-8ec2-4c8f-92b4-7dd77c00c311.png)



