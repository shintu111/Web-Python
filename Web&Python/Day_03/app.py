# Task 1: Develop Flask routes to handle the workflow of submitting insurance claims. 
# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

class ClaimForm(FlaskForm):
    policy_number = StringField('Policy Number', validators=[DataRequired()])
    claim_description = TextAreaField('Claim Description', validators=[DataRequired()])
    submit = SubmitField('Submit Claim')

@app.route('/submit_claim', methods=['GET', 'POST'])
def submit_claim():
    form = ClaimForm()
    if form.validate_on_submit():
        # process claim submission
        policy_number = form.policy_number.data
        claim_description = form.claim_description.data
        # save claim to database or perform other necessary actions
        return redirect(url_for('claim_confirmation', policy_number=policy_number))
    return render_template('submit_claim.html', form=form)

@app.route('/claim_confirmation/<policy_number>')
def claim_confirmation(policy_number):
    return render_template('claim_confirmation.html', policy_number=policy_number)

if __name__ == '__main__':
    app.run(debug=True)