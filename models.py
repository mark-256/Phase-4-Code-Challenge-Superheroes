from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    
    # Relationship with HeroPower
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }
    
    def to_dict_with_powers(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'hero_powers': [hp.to_dict_for_hero() for hp in self.hero_powers]
        }

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    
    # Relationship with HeroPower
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')
    
    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError("Description must be present")
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    
    # Foreign keys
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id', ondelete='CASCADE'), nullable=False)
    
    # Relationships
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')
    
    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError(f"Strength must be one of: {', '.join(valid_strengths)}")
        return strength
    
    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'hero': self.hero.to_dict(),
            'power': self.power.to_dict()
        }
    
    def to_dict_for_hero(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'power': {
                'id': self.power.id,
                'name': self.power.name,
                'description': self.power.description
            }
        }