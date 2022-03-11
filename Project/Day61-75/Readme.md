## #This is all project from Day61 - Day75

Proeject List in order by Learning Day:

1. Tindog (Bootstrap)(HTML)
2. WTF Form
3. Coffee & Wifi (WTF-Form)(Flask)
4. Library(HTML)(SQLite)
5. Top-100 Movie Website(HTML)(WTF-form)(Flask)(Bootstrap)(SQLite)(SQLAlchemy)
6. Cafe & Wifi Project(Building RESTful API)(SQL)(Flask)
7. RESTful blog
8. Authentication (Flask)

## Concepts Used in Day46 - Day60

## Jinja

Templating language for Python for changing dynamic contents each time reloading pages

```
<h1>Hello world </h1> = Hello world

<h1>{{3 * 6}}</h1> = 18
```

**HTML**

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>home</title>
    <meta name="description" content="" />
    <link rel="stylesheet" href="./static/css/style.css" />
  </head>
  <body>
    <h1>{{5 * 6}}</h1> ## anything in -> {{}} <-  will become Python Code
  </body>
</html>
```

**passing args to html**

```
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number)
```

**HTML**

```
<body>
    <h1>Hello World!</h1>
    <h1>{{5 * 6}}</h1>
    <h1>Random number = {{ num }}</h1>
  </body>
```

## multiline statement to html

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Blog</title>
  </head>
  <body>
    {% for blog in posts: %} {% if blog["id"] == 2:%}
    <h1>{{ blog["title"]}}</h1>
    <h2>{{ blog["subtitle"]}}</h2>
    {% endif %} {% endfor %}
  </body>
</html>
```

**URL**

```
<body>
    <h1>Hello World!</h1>
    <h1>{{5 * 6}}</h1>
    <h1>Random number = {{ num }}</h1>
    <a href="{{ url_for('get_blog', num=3) }}">Go to Blog</a>
  </body>
```

## SQLite Database

```
import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
```
![image](https://user-images.githubusercontent.com/98913678/157965393-a0366d73-10fc-4cff-8487-8a023a18d2b6.png)
![image](https://user-images.githubusercontent.com/98913678/157965458-acbcb5dd-8eb4-4f1f-bc79-4f33ba1c7bc4.png)

**New Entry**
```
cursor.execute(
    "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
```
