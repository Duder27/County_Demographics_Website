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
		print(y)
	return y

@app.route("/")
def render_main():
	with open('county_demographics.json') as demographics_data:
		counties = json.load(demographics_data)
	return render_template('home.html', options = get_state_options(counties))


@app.route("/response")
def render_response():
	with open('county_demographics.json') as demographics_data:
		counties = json.load(demographics_data)
	fact = request.args['StateSelected']
	fact1 = ""
	for data in counties:
		if fact == data["State"]:
			first_county = counties[0]["Education"]["High School or Higher"]
			for amount in counties:
				amount["Education"]["High School or Higher"]
				if amount["Education"]["High School or Higher"] > first_county:
					print(first_county)
					first_county = amount["Education"]["High School or Higher"]
			fact1 = data["Education"]["High School or Higher"]
	return render_template('response.html', response = fact1)


if __name__=="__main__":
    app.run(debug=True, port=54321)
