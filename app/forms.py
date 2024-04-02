from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class DateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Period - Day 1, Ovulation, etc."})
    symptoms = TextAreaField('Symptoms', validators=[Length(min=0, max=140)], render_kw={"placeholder": "Flow, pain, fatigue, etc."})
    notes = TextAreaField('Extra notes', validators=[Length(min=0, max=140)], render_kw={"placeholder": "Everything else"})
    submit = SubmitField('Submit')