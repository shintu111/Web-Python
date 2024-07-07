# Task 1: Integrate Flask-SocketIO for handling real-time updates to claim status. from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit 
#pip install flask_socketio
from flask_sqlalchemy import SQLAlchemy

app = Flask('claim_service')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/claim.db'
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins='*')

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'))
    claim_description = db.Column(db.String(200), nullable=False)
    claim_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(100), nullable=False)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('update_claim_status')
def handle_update_claim_status(data):
    claim_id = data['claim_id']
    new_status = data['new_status']
    claim = Claim.query.get(claim_id)
    if claim:
        claim.status = new_status
        db.session.commit()
        emit('claim_status_updated', {'claim_id': claim_id, 'new_status': new_status}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)