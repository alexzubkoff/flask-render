from flask import Flask, render_template, request, flash
from forms import ContactForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecret'


@app.route('/', methods=['GET', 'POST'])
def contactForm():
	form = ContactForm()
	if request.method == 'GET':
		return render_template('contact.html', form=form)
	elif request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required !')
			return render_template('contact.html', form=form)
		else:
			result = [
				(form.name.label, form.name.data),
				(form.title.label, form.title.data),
				(form.company.label, form.company.data),
				(form.phone.label, form.phone.data),
				(form.email.label, form.email.data),
				(form.address.label, form.address.data),
				(form.template.label, form.template.data),
			]
			if form.template.data == "Template 1":
				return render_template("result.html", result=result)
			return render_template("result_2.html", result=result)
		return '<h1>Form submitted!</h1>'


if __name__ == '__main__':
	app.run(debug=True)