## #This is all project from Day61 - Day70

Proeject List in order by Learning Day:

1. Tindog (Bootstrap)(HTML)
2. WTF Form
3. Coffee & Wifi (WTF-Form)(Flask)
4. Library(HTML)(SQLite)
5. Top-100 Movie Website(HTML)(WTF-form)(Flask)(Bootstrap)(SQLite)(SQLAlchemy)
6. Cafe & Wifi Project(Building RESTful API)(SQL)(Flask)
7. RESTful blog
8. Authentication (Flask)
9. Blog-with-users (Capstone Project)

## Concepts Used in Day61 - Day70

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

## SQLite3 Database (Using Flask sqlalchemy)

**Create Database**

```
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)
```

**Create Sheet in Database**

```
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, primary_key=True)

    def __repr__(self):
        return f"<Book {self.title}>"
```

**New entry**

```
db.create_all()

new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3) ## Acutally the id will be auto-generated, because id is primary_key.
db.session.add(new_book)
db.session.commit()
```

**CRUD (Create, Read, Update, Delete)**

```
##Create##
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

##Read##
all_books = session.query(Book).all()

##Read particular record by Query##
book = Book.query.filter_by(title="Harry Potter").first()

##Update a particular record by Query##
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

##Update a particular record by Primary Key##
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

##Delete A Particular Record By PRIMARY KEY##
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
```

## RESTful API

REST = Representational State Transfer

1. Use HTTP Request Verbs
2. Use Specific Pattern of Routes/Endpoint URL
