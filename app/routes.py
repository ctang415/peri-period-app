from app import app
from flask import render_template

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
    return render_template('home.html', title="Home", events=events)

@app.route('/date')
@app.route('/date/<date>')
def date(date):
    return render_template('date.html')