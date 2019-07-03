
from datetime import datetime

from app import app, db
from flask import request, redirect, url_for, render_template

from .forms import AddDetailForm
from .models import Details

@app.route('/', methods=['GET'])
def landing():
    return render_template('landing/landing.html')

@app.route('/list', methods=['GET'])
def list_details():
    all_details = Details.query.all()

    return render_template('landing/list_details.html', details=all_details)

@app.route('/add', methods=['GET', 'POST'])
def add_detail():
    form = AddDetailForm()

    if request.method == 'POST' and form.validate_on_submit():
        name = request.form.get('name')
        email_address = request.form.get('email')

        new_detail = Details(name=name, email_address=email_address, date_registered=datetime.now())
        db.session.add(new_detail)
        db.session.commit()

        return redirect(url_for('list_details'))
    
    return render_template('landing/add_detail.html', form=form)