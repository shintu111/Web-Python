# Task 1: Refactor the application to a microservices architecture with Flask. 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask('policy_service')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/policy.db'
db = SQLAlchemy(app)

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(100), unique=True, nullable=False)
    policyholder = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

@app.route('/policies', methods=['GET'])
def get_policies():
    policies = Policy.query.all()
    return jsonify([policy.to_dict() for policy in policies])

@app.route('/policies', methods=['POST'])
def create_policy():
    data = request.get_json()
    policy = Policy(**data)
    db.session.add(policy)
    db.session.commit()
    return jsonify(policy.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)