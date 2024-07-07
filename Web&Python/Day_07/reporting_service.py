# Task 3: Manage configurations across microservices using environment variables or a centralized configuration service.
from flask import Flask, request, jsonify

app = Flask('reporting_service')

@app.route('/reports/policy_claims', methods=['GET'])
def get_policy_claims():
    # implement reporting logic here
    return jsonify({'message': 'Reporting service is up!'})

if __name__ == '__main__':
    app.run(debug=True)
