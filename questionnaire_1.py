from flask import Flask
from flask import render_template
from flask import request
import unicodecsv
import csv

app = Flask("myApp")


@app.route("/")
def enter():
	return render_template("index.html")

@app.route("/hackyourown.html")
def split():
	return render_template("hackyourown.html")


@app.route("/questionnaire_2.html",)
def questionnaire():
	return render_template('questionnaire_2.html')

@app.route("/questionnaire", methods=['POST'])
def save_data():

	form_data = request.form 
	name = form_data['name']
	email = form_data['email']
	age = form_data['age']
	answer_1 = form_data['Category1']
	answer_2 = form_data['Category2']
	answer_3 = form_data['Category3']

	result = answer_1+answer_2+answer_3

	with open("results.csv", mode="a") as csvfile:
		fieldnames = ['name', 'email', 'age', 'answer_1', 'answer_2', 'answer_3']
		writer = unicodecsv.DictWriter(csvfile,fieldnames=fieldnames)
		writer.writerow({'name': name, 'email':email, 'age':age, "answer_1": answer_1, "answer_2": answer_2, "answer_3": answer_3, })

	if result == 'musicalclassiccomedy':
		return render_template("PHOENIX.html")
	elif result == 'musicalclassicdrama':
		return render_template("SAVOY.html")
	elif result == 'musicalcontemporarydrama':
		return render_template("HAROLD.html")
	elif result == 'musicalcontemporarysmash':
		return render_template("PICCADILLY.html")
	elif result == 'musicalcontemporarycomedy':
		return render_template("APOLLOVICTORIA.html")
	elif result == 'musicalclassicsmash':
		return render_template("LYCEUM.html")
	elif result == 'playclassicdrama':
		return render_template("TRAFALGAR1.html")
	elif result == 'playcontemporarycomedy':
		return render_template("TRAFALGAR2.html")
	elif result == 'playclassiccomedy':
		return render_template("DONMAR.html")
	elif result == 'playcontemporarydrama':
		return render_template("PLAYHOUSE.html")
	elif result == 'playcontemporarysmash':
		return render_template("DUKE.html")
	elif result == 'playclassicsmash':
		return render_template("FORTUNE.html")
	else:
		return render_template("DIY.html")

@app.route("/APOLLOVICTORIA.html")
def apollovictoria():
	return render_template("APOLLOVICTORIA.html")

@app.route("/DONMAR.html")
def donmar():
	return render_template("DONMAR.html")

@app.route("/DUKE.html")
def duke():
	return render_template("DUKE.html")

@app.route("/DIY.html")
def diy():
	return render_template("DIY.html")

@app.route("/FORTUNE.html")
def fortune():
	return render_template("FORTUNE.html")

@app.route("/HAROLD.html")
def harold():
	return render_template("HAROLD.html")

@app.route("/LYCEUM.html")
def lyceum():
	return render_template("LYCEUM.html")

@app.route("/PICCADILLY.html")
def piccadilly():
	return render_template("PICCADILLY.html")

@app.route("/PHOENIX.html")
def phoenix():
	return render_template("PHOENIX.html")

@app.route("/PLAYHOUSE.html")
def playhouse():
	return render_template("PLAYHOUSE.html")

@app.route("/SAVOY.html")
def savoy():
	return render_template("SAVOY.html")

@app.route("/TRAFALGAR1.html")
def trafalgar1():
	return render_template("TRAFALGAR1.html")

@app.route("/TRAFALGAR2.html")
def trafalgar2():
	return render_template("TRAFALGAR2.html")

print "All Ok"


app.run(debug=True)