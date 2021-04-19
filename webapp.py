from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_state_options(counties):
	get_state_options = []
	for s in counties:
		if not(s['State']) in get_state_options:
			get_state_options.append(s['State'])
	y = ''
	for x in get_state_options:
		y = y + Markup("<option value=\"" + x + "\">" + x + "</option>")
	return y

def get_county_options(counties):
	get_county_options = []
	for c in counties:
		if not(c['County']) in get_county_options:
			get_county_options.append(c['County'])
	y = ''
	for x in get_county_options:
		y = y + Markup("<option value=\"" + x + "\">" + x + "</option>")
	return y


@app.route("/")
def render_main():
	with open('county_demographics.json') as demographics_data:
		counties = json.load(demographics_data)
	return render_template('home.html', options = get_state_options(counties), county_options = get_county_options(counties))


@app.route("/response", method = 'POST')
def render_response():
	with open('county_demographics.json') as demographics_data:
		counties = json.load(demographics_data)
	state = request.form['StateSelected']
	county = request.form['county_name']
	fact1 = 0
	fact2 = ""
	factC = ""
	factS = ""
	for data in counties:
		if state == data["State"] and fact1 < data["Education"]["High School or Higher"]:
			data["Education"]["High School or Higher"]
			fact1 = data["Education"]["High School or Higher"]
			fact2 = data["County"]
		if county == data["County"]:
			#data["Miscellaneous"]["Language Other than English at Home"]
			factC = data["Miscellaneous"]["Language Other than English at Home"]
			factS = data["State"]
	return render_template('response.html', response = fact1, response2 = state, response3 = fact2, response4 = factC, response5 = factS, response6 = county)


if __name__=="__main__":
    app.run(debug=True, port=54321)
