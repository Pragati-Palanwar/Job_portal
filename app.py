from flask import Flask, render_template, request, redirect, url_for
from models import db, JobSeeker, Employer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/job_seeker', methods=['GET', 'POST'])
def job_seeker():
    if request.method == 'POST':
        name = request.form['name']
        skills = request.form['skills']
        availability = request.form['availability']
        other_details = request.form['other_details']

        new_job_seeker = JobSeeker(name=name, skills=skills, availability=availability, other_details=other_details)
        db.session.add(new_job_seeker)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('job_seeker.html')

@app.route('/employer', methods=['GET', 'POST'])
def employer():
    if request.method == 'POST':
        name = request.form['name']
        company_name = request.form['company_name']
        job_requirements = request.form['job_requirements']
        contact_details = request.form['contact_details']

        new_employer = Employer(name=name, company_name=company_name, job_requirements=job_requirements, contact_details=contact_details)
        db.session.add(new_employer)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('employer.html')

if __name__ == '__main__':
    app.run(debug=True)
