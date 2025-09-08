from flask import Flask, render_template

#, render_template, request, redirect, url_for
# import sqlite3

# remember to $ pip install flask

app = Flask(__name__)

pet_data = [
    {
        "name":"dorothy",
        "kind":"dog",
        "food":"dogfood",
        "noise":"arf"
    },
    {
        "name":"sandy",
        "kind":"cat",
        "food":"catfood",
        "noise":"meow"
    },
    {
        "name":"clarabelle",
        "kind":"cow",
        "food":"hay",
        "noise":"moo"
    },

]

@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html", item={
        "name":"Greg",
        "title":"Dr."
    }, count=10)

@app.route("/hi/<name>", methods=["GET"])
@app.route("/hi", methods=["GET"])
def get_hi(name="guest"):
    return render_template("index.html", item={
        "name":name
    }, count=1)

@app.route("/pets",methods=["GET"])
def get_pets():
    global pet_data
    data = pet_data
    return render_template("pets.html", data=data)


@app.route("/data", methods=["GET"])
def get_data():
    return {"data":[{
        "name":"Greg",
        "title":"Dr."

    },
    {
        "name":"Maletic",
        "title":"Professort."

    }
    ]}
