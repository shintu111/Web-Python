# Task 3: Implement Data Binding and Server-Side Validation
# models.py
class Claim:
    def __init__(self, policy_number, claim_description):
        self.policy_number = policy_number
        self.claim_description = claim_description

    def save_to_database(self):
        # save claim to database
        pass

    def process_claim(self):
        # perform necessary actions to process the claim
        pass

# app.py
@app.route('/submit_claim', methods=['GET', 'POST'])
def submit_claim():
    form = ClaimForm()
    if form.validate_on_submit():
        claim = Claim(form.policy_number.data, form.claim_description.data)
        # save claim to database or perform other necessary actions
        return redirect(url_for('claim_confirmation', policy_number=claim.policy_number))
    return render_template('submit_claim.html', form=form)
