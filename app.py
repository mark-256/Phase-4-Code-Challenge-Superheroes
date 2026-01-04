from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

class Heroes(Resource):
    def get(self):
        heroes = Hero.query.all()
        heroes_data = [hero.to_dict() for hero in heroes]
        return make_response(jsonify(heroes_data), 200)

class HeroByID(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return make_response(jsonify({"error": "Hero not found"}), 404)
        return make_response(jsonify(hero.to_dict_with_powers()), 200)

class Powers(Resource):
    def get(self):
        powers = Power.query.all()
        powers_data = [power.to_dict() for power in powers]
        return make_response(jsonify(powers_data), 200)

class PowerByID(Resource):
    def get(self, id):
        power = Power.query.get(id)
        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)
        return make_response(jsonify(power.to_dict()), 200)

class UpdatePower(Resource):
    def patch(self, id):
        power = Power.query.get(id)
        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)
        
        data = request.get_json()
        
        # Validate request body
        if not data or 'description' not in data:
            return make_response(jsonify({"error": "Description is required"}), 400)
        
        # Try to update the power
        try:
            power.description = data['description']
            db.session.commit()
            return make_response(jsonify(power.to_dict()), 200)
        except ValueError as e:
            db.session.rollback()
            return make_response(jsonify({"errors": [str(e)]}), 400)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"errors": [str(e)]}), 400)

class HeroPowers(Resource):
    def post(self):
        try:
            data = request.get_json()
            
            if not data:
                return make_response(jsonify({"errors": ["No data provided"]}), 400)
            
            # Check for required fields
            required_fields = ['strength', 'power_id', 'hero_id']
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return make_response(jsonify({"errors": [f"{field} is required" for field in missing_fields]}), 400)
            
            # Validate hero exists
            hero = Hero.query.get(data['hero_id'])
            if not hero:
                return make_response(jsonify({"errors": ["Hero not found"]}), 404)
            
            # Validate power exists
            power = Power.query.get(data['power_id'])
            if not power:
                return make_response(jsonify({"errors": ["Power not found"]}), 404)
            
            # Create HeroPower
            hero_power = HeroPower(
                strength=data['strength'],
                hero_id=data['hero_id'],
                power_id=data['power_id']
            )
            
            db.session.add(hero_power)
            db.session.commit()
            
            return make_response(jsonify(hero_power.to_dict()), 201)
            
        except ValueError as e:
            db.session.rollback()
            return make_response(jsonify({"errors": [str(e)]}), 400)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"errors": [str(e)]}), 400)

# Add routes
api.add_resource(Heroes, '/heroes')
api.add_resource(HeroByID, '/heroes/<int:id>')
api.add_resource(Powers, '/powers')
api.add_resource(PowerByID, '/powers/<int:id>')
api.add_resource(UpdatePower, '/powers/<int:id>')
api.add_resource(HeroPowers, '/hero_powers')

@app.route('/')
def home():
    return '<h1>Superheroes API</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)