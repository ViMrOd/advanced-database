from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# remember to $ pip install flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html", item={"name":"student", "title":"Grad"}, count=10)

@app.route("/hi/<name>", methods=["GET"])
@app.route("/hi", methods=["GET"])
def get_hi(name="guest"):
    return render_template("index.html", item={"name":name}, count=1)

@app.route("/data", methods=["GET"])
def get_data():
    return {"data": [{"name":"Stu Dent", "title":"Graduate"}, {"name":"Chadwick", "title":"Undergrad"}] }