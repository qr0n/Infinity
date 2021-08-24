from flask import Flask, redirect, render_template, request
import json
import os
from key_gen import assigner
w_logs = []
app = Flask('app')

def user(value):
    if value == "KNDoSWe6U":
      return "Iron"
    elif value == "WvpIRvrjw":
      return "Phil"
    elif value == "meUbsGekh":
      return "Verrus"
    elif value == "g9fgLzaxh":
      return "Chiko"
    elif value == "mJkHzJeSu":
      return "Ally"
    elif value == "oBLv6BCPx":
      return "Mike"
    elif value == "sRPfQOKZ1":
      return "Rave"
    elif value == "cAiq4v8Es":
      return "Emily"
    elif value == "yA9WrgNHJ":
      return "Adam"
    elif value == "vk6KmL1bi":
      return "Kun"
    elif value == "avwuaPvEp":
      return "Lime"
    elif value == "a5WUsoDWm":
      return "Sam"
    elif value == "pWKi3MDXr":
      return "Lemon"
    elif value == "iudghQQaF":
      return "Eli"
    elif value == "N0VA":
      return "Nova"
    
#   "Kun": "vk6KmL1bi", 
#   "Lime": "avwuaPvEp", 
#   "Sam": "a5WUsoDWm", 
#   "Lemon": "pWKi3MDXr", 
#   "Eli": "iudghQQaF", 
#   "4162_ADMIN": "7mES3UObM"


@app.route('/')
def home():
  return redirect("https://google.com/")

@app.route('/tag-team/<name>')
def asd(name):

  with open(f"allowedKeys.json", "r") as logs:
    l_logs = json.load(logs)

    key_values = [key for key in l_logs.values()]
    key_name = [key for key in l_logs]

    if name == "7mES3UObM":
      return render_template('4162_config.json')
      with open("Weblogs.json", "r") as r:
        l_r = json.load(r)
        l_r["current user log in"] = user(value=name)
      with open("Weblogs.json", "w") as r:
        json.dump(l_r, r)
    if name in key_values:
      print(f"detected key {key_values} {name}")
      return render_template('the-game.html', name=user(value=name))
  
    else:
      print(f"did not detect key {key_values} {name}")
      return redirect("/")

@app.route('/logs/<name>')
def logs(name):
  if name == "KNDoSWe6U":
    with open("Weblogs.json", "r") as f:
      
      return json.load(f)
    
@app.route('/Data')
def page():
  return render_template("data-use.html")

@app.route('/logs')
def my_form():
    return render_template('activity-searcher.html')

@app.route('/logs/<name>', methods=['POST'])
def my_form_post(name):
    text = request.form['text']
    processed_text = text
    w_logs.append(processed_text)
    return processed_text

print(assigner.Create(integer=True))
print(assigner.Create())
app.run(host='0.0.0.0', port=8080,)
