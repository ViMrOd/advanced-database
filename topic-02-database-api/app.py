from flask import Flask, render_template, request

#, render_template, , redirect, url_for

import sqlite3

# remember to $ pip install flask

app = Flask(__name__)

connection = sqlite3.connect("pets.db", check_same_thread=False)

# pet_data = [
#     {
#         "name":"dorothy",
#         "kind":"dog",
#         "food":"dogfood",
#         "noise":"arf"
#     },
#     {
#         "name":"sandy",
#         "kind":"cat",
#         "food":"catfood",
#         "noise":"meow"
#     },
#     {
#         "name":"clarabelle",
#         "kind":"cow",
#         "food":"hay",
#         "noise":"moo"
#     },

# ]

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
    cursor = connection.cursor()
    rows = cursor.execute("select * from pet").fetchall()
    pet_data = [
        {
            "id":str(id),
            "name":name,
            "kind":kind,
            "noise":noise,
            "food":food
        }
        for id, name, kind, noise, food in rows
    ]
    return render_template("pets.html", data=pet_data)

@app.route("/create", methods=["GET"])
def get_create():
    return render_template("create.html")

@app.route("/create", methods=["POST"])
def post_create():
    name = request.form.get("name")
    kind = request.form.get("kind")
    noise = request.form.get("noise")
    food = request.form.get("food")

    cursor = connection.cursor()
    cursor.execute("insert into pet (name, kind, noise, food) values (?, ?, ?, ?)", (name, kind, noise, food))
    connection.commit()

    return redirect(url_for("get_pets"))

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
