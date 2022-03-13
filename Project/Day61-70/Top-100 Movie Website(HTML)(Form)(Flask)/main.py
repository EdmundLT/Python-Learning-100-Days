from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)
Bootstrap(app)

# ----- TMDB -----#
API_KEY = "55a764184948db155b0284897955ac2f"
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NWE3NjQxODQ5NDhkYjE1NWIwMjg0ODk3OTU1YWMyZiIsInN1YiI6IjYyMjhlNDlkMTEzMGJkMDA0NWRmMDRiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZR2zpBw6Vg-0b6wu2PSXiZ0Uosig1rsMNWzyDDU8zw0"
# Create Table #


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()

# Server


@app.route("/")
def home():
    existing = db.session.query(Movie).count()
    all_movies = Movie.query.order_by(Movie.rating.asc())
    for index in range(existing):
        all_movies[index].ranking = existing - index
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        movie_id = request.form["id"]
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))

    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie_selected)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie = request.args.get('id')
    movie_to_delete = Movie.query.get(movie)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


class FindMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get("https://api.themoviedb.org/3/search/movie",
                                params={"api_key": API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route('/find')
def find_movie():
    movie_id = request.args.get("id")
    if movie_id:
        api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(api_url)
        data = response.json()
        new_movie = Movie(id=movie_id, title=data["original_title"],
                          year=data["release_date"], description=data["overview"], rating=0, review="none", img_url=f"https://www.themoviedb.org/t/p/w1280/{data['poster_path']}")
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)
