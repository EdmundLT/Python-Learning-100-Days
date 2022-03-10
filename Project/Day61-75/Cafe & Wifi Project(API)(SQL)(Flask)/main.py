from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
import random
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Cafe TABLE Configuration
API_KEY = "TopSecretAPIKey"


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():

    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    loc = request.args.get('loc')
    cafe_searched = db.session.query(Cafe).filter_by(location=loc).first()
    if cafe_searched:
        return jsonify(cafe=cafe_searched.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    new_cafename = request.form.get('name')
    new_cafemap_url = request.form.get('map_url')
    new_cafeimg_url = request.form.get('img_url')
    new_cafelocation = request.form.get('location')
    new_cafeseats = request.form.get('seats')
    new_cafehas_toilet = bool(request.form.get('has_toilet'))
    new_cafehas_wifi = bool(request.form.get('has_wifi'))
    new_cafehas_sockets = bool(request.form.get('has_sockets'))
    new_cafecan_take_calls = bool(request.form.get('can_take_calls'))
    new_cafecoffee_price = request.form.get('price')

    new_cafe = Cafe(name=new_cafename, map_url=new_cafemap_url, img_url=new_cafeimg_url, location=new_cafelocation, seats=new_cafeseats, has_toilet=new_cafehas_toilet, has_wifi=new_cafehas_wifi, has_sockets=new_cafehas_sockets,
                    can_take_calls=new_cafecan_take_calls, coffee_price=new_cafecoffee_price)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
# HTTP PUT/PATCH - Update Record


@app.route('/update-price/<int:id>', methods=["GET", "POST", "PATCH"])
def update_price(id):
    cafe_id = id
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(success={"Success": "Successfully updated the price"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:id>', methods=["GET", "POST", "PATCH", "DELETE"])
def delete_cafe(id):
    cafe_id = id
    api = request.form.get('api-key')
    if api == API_KEY:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(success={"success": "The cafe are reported closed."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})


if __name__ == '__main__':
    app.run(debug=True)
