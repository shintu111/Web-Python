# Task 2: Develop CRUD Operations for Claims and Policies using SQLAlchemy Session and Query Objects

# Task 3: Write and Test SQL Queries using SQLAlchemy for Advanced Data Retrieval and Reporting
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'qlite:////tmp/test.db'
db = SQLAlchemy(app)

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

@app.route('/claims', methods=['GET'])
def get_claims():
    claims = Claim.query.all()
    return jsonify([claim.to_dict() for claim in claims])

@app.route('/claims', methods=['POST'])
def create_claim():
    data = request.get_json()
    claim = Claim(**data)
    db.session.add(claim)
    db.session.commit()
    return jsonify(claim.to_dict()), 201

@app.route('/claims/<int:claim_id>', methods=['GET'])
def get_claim(claim_id):
    claim = Claim.query.get_or_404(claim_id)
    return jsonify(claim.to_dict())

@app.route('/claims/<int:claim_id>', methods=['PUT'])
def update_claim(claim_id):
    claim = Claim.query.get_or_404(claim_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(claim, key, value)
    db.session.commit()
    return jsonify(claim.to_dict())

@app.route('/claims/<int:claim_id>', methods=['DELETE'])
def delete_claim(claim_id):
    claim = Claim.query.get_or_404(claim_id)
    db.session.delete(claim)
    db.session.commit()
    return '', 204
# Task 3: Write and Test SQL Queries using SQLAlchemy for Advanced Data Retrieval and Reporting

@app.route('/reports/policy_claims', methods=['GET'])
def get_policy_claims():
    claims = db.session.query(Claim).join(Policy).filter(Policy.status == 'active').all()
    return jsonify([claim.to_dict() for claim in claims])

@app.route('/reports/top_claims', methods=['GET'])
def get_top_claims():
    top_claims = db.session.query(Claim).order_by(Claim.claim_date.desc()).limit(10).all()
    return jsonify([claim.to_dict() for claim in top_claims])

@app.route('/reports/policy_claim_counts', methods=['GET'])
def get_policy_claim_counts():
    claim_counts = db.session.query(Policy.id, Policy.policy_number, db.func.count(Claim.id).label('claim_count')).join(Claim).group_by(Policy.id).all()
    return jsonify([{'policy_id': policy_id, 'policy_number': policy_number, 'claim_count': claim_count} for policy_id, policy_number

