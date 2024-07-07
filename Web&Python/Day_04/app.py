# Task 1: Refactor policy-related operations to utilize Flask views and application context. 
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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

@app.route('/policies/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    return jsonify(policy.to_dict())

@app.route('/policies/<int:policy_id>', methods=['PUT'])
def update_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(policy, key, value)
    db.session.commit()
    return jsonify(policy.to_dict())

@app.route('/policies/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    db.session.delete(policy)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)