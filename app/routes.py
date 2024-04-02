from app import app, db
from flask import render_template, request, flash, redirect
from forms import DateForm, DeleteForm
from models import Note
from datetime import datetime, date
import sqlalchemy as sa

events = [
    {
        'todo': 'tutorial',
        'date': '2024-03-21',
        'url': '/date/2024-03-21'
    },
    {
        'todo': 'hi',
        'date': '2024-04-01',
        'url': '/date/2024-04-01'
    }
]

@app.route('/')
@app.route('/home')
def home():
    current = datetime.today().strftime("%Y-%m")
    query = sa.select(Note).where(Note.date.like(f'{current}%'))
    items = db.session.scalars(query).all()
    events = [ {"todo": item.title, "date": datetime.strftime(item.date, '%Y-%m-%d'), "url": f'/date/{item.date}'} for item in items ]
    return render_template('home.html', title="Home", events=events)

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
        return render_template('date.html', date=date, form=form, form2=form2)
    else:
        if form.validate_on_submit():
            note = Note(title=form.title.data, date=datetime.strptime(date, '%Y-%m-%d'), symptoms=form.symptoms.data, notes=form.notes.data)
            db.session.add(note)
            db.session.commit()
            flash('Notes added!')
            return redirect(f'/date/{date}')
        return render_template('date.html', date=date, form=form)