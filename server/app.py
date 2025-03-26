# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>')
def earthquake_id(id):
    earthquake = Earthquake.query.get(id)

    if not earthquake:
        return jsonify({'message': f'Earthquake {id} not found.'}), 404

    earthquake_data = {
        'id': earthquake.id,
        'location': earthquake.location,
        'magnitude': earthquake.magnitude,
        'year': earthquake.year
    }

    return jsonify(earthquake_data)


@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_magnitude(magnitude):
    magnitude = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    earthquakes = [{
        'id': quakes.id,
        'location': quakes.location,
        'magnitude': quakes.magnitude,
        'year': quakes.year
    } for quakes in magnitude]

    response = {
        'count': len(earthquakes),
        'quakes': earthquakes
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
