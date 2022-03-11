from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        new_user_password = request.form["password"]
        new_user_password_hashed = generate_password_hash(
            password=new_user_password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=request.form["email"],
                        password=new_user_password_hashed,
                        name=request.form["name"]
                        )
        search_user = db.session.query(
            User).filter_by(email=request.form["email"]).first()
        if search_user:
            flash('Your email already registered.')
        else:
            db.session.add(new_user)
            db.session.commit()
            return render_template('secrets.html', user=new_user)
    return render_template("register.html", logged_in=current_user.is_authenticated)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        login_email = request.form.get("email")
        login_pw = request.form.get("password")

        search_user = db.session.query(
            User).filter_by(email=login_email).first()
        if search_user:
            if check_password_hash(search_user.password, login_pw):
                login_user(search_user)
                return redirect(url_for('secrets'))
            else:
                flash('Password incorrect, please try again.')
        else:
            flash("That email does not exist, please try again.")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", user=current_user, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(directory='static', path='files', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
