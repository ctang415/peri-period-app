from app import app, db
from flask import render_template, request, flash, redirect, url_for
from forms import DateForm, DeleteForm
from models import Note
from datetime import datetime
import sqlalchemy as sa
import csv
import requests

@app.route('/')
@app.route('/home')
def home():
    query = sa.select(Note)
    items = db.session.scalars(query).all()
    events = [ {"todo": item.title, "date": item.date, "url": f'/date/{datetime.strftime(item.date, "%Y-%m-%d")}'} for item in items ]
    toggle = "p-2 bg-light text-dark shadow m-2 rounded"
    return render_template('home.html', title="Peri", events=events, toggle=toggle)

@app.route('/date/<date>', methods=['GET', 'POST'])
def date(date):
    form = DateForm()
    note = db.session.scalar(sa.select(Note).where(Note.date.like(f'{date}%')))
    if note is not None:
        form2 = DeleteForm()
        if request.method == "GET":
            form.title.data = note.title
            form.symptoms.data = note.symptoms
            form.notes.data = note.notes
        elif form.validate_on_submit():
            note.title = form.title.data 
            note.symptoms = form.symptoms.data 
            note.notes =  form.notes.data
            db.session.commit()
            flash('Notes updated!')
            return redirect(f'/date/{date}')
        elif form2.validate_on_submit():
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted!')
            return redirect(f'/date/{date}')
        return render_template('date.html', date=date, title=date, form=form, form2=form2)
    else:
        if form.validate_on_submit():
            note = Note(title=form.title.data, date=datetime.strptime(date, '%Y-%m-%d'), symptoms=form.symptoms.data, notes=form.notes.data)
            db.session.add(note)
            db.session.commit()
            flash('Notes added!')
            return redirect(f'/date/{date}')
        return render_template('date.html', date=date, form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.route('/export')
def export():
    query = sa.select(Note)
    items = db.session.scalars(query).all()
    events = [ {"todo": item.title, "date": item.date, "url": f'/date/{datetime.strftime(item.date, "%Y-%m-%d")}'} for item in items ]
    with open("peridata.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Title", "Symptoms", "Notes"])
        writer.writeheader()
        for item in items:
            writer.writerow({"Date": datetime.strftime(item.date, '%Y-%m-%d'), "Title": item.title, "Symptoms": item.symptoms, "Notes": item.notes})
    file.close()
    return redirect(url_for('home'))

@app.route('/delete')
def delete_db():
    db.session.query(Note).delete()
    db.session.commit()
    return redirect(url_for('home'))