from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

def get_state_options(counties):
	get_state_options = []
	for s in counties:
		s["County"]
		if s in get_state_options:
			print("in list")
		else:
			get_state_options.append(s)
	for x in get_state_options:
		y = y + Markup("<option value=\"" + x + "\">" + x + "</option>")
	return y

@app.route("/")
def render_main(counties):
		counties["County"]
    return render_template('home.html', options=(get_state_options(counties)))


@app.route("/response")
def render_response():
  return render_template()


if __name__=="__main__":
    app.run(debug=True, port=54321)
