# Task 2: Implement service discovery with Consul and set up Flask applications as individual services.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask('claim_service')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/claim.db'
db = SQLAlchemy(app)

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'))
    claim_description = db.Column(db.String(200), nullable=False)
    claim_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(100), nullable=False)

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

if __name__ == '__main__':
    app.run(debug=True)