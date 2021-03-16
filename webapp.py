from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
  
@app.route("/response")
def render_response():
  
  return render_template()

if __name__=="__main__":
    app.run(debug=False, port=54321)