from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, RadioField
from wtforms import validators


class ContactForm(FlaskForm):
    name = StringField("Full name", [validators.data_required('Please enter your full name !')])
    title = StringField("Job title", [validators.data_required('Please enter your email title !')])
    company = StringField("Company", [validators.data_required('Please enter your company !')])
    phone = StringField("Phone", [validators.data_required('Please enter your phone number !')])
    email = StringField("E-mail", [validators.data_required('Please enter your email address !'), validators.Email()])
    address = TextAreaField("Address ", [validators.data_required('Enter your address !')])
    template = RadioField('Layouts', choices=[('Template 1', 'Template 1'), ('Template 2', 'Template 2')])
    submit = SubmitField("Submit")
