# Task 2: Implement server-side validation in Flask to maintain policy data integrity. 
# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy(app)

class Policy(db.Model):
    # ...

    @validates('policy_number')
    def validate_policy_number(self, key, policy_number):
        if not policy_number:
            raise ValueError('Policy number is required')
        return policy_number

    @validates('policyholder')
    def validate_policyholder(self, key, policyholder):
        if not policyholder:
            raise ValueError('Policyholder is required')
        return policyholder

    @validates('type')
    def validate_type(self, key, type):
        if not type:
            raise ValueError('Policy type is required')
        return type

    @validates('status')
    def validate_status(self, key, status):
        if not status:
            raise ValueError('Policy status is required')
        return status