import sqlite3

# remember to $ pip install flask

connection = sqlite3.connect("pets.db", check_same_thread=False)

def retrieve_pets():
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
    return pet_data

def retrieve_pet(id):
    cursor = connection.cursor()
    row = cursor.execute("select * from pet where id = ?", (id,)).fetchone()
    pet_item = {
        "id":str(row[0]),
        "name":row[1],
        "kind":row[2],
        "noise":row[3],
        "food":row[4]
    }
    return pet_item

def create_pet(pet_item):
    cursor = connection.cursor()
    cursor.execute("insert into pet (name, kind, noise, food) values (?, ?, ?, ?)", (
            pet_item["name"],
            pet_item["kind"], 
            pet_item["noise"], 
            pet_item["food"]))
    connection.commit()

    connection.commit()

def update_pet(pet_item):
    cursor = connection.cursor()
    cursor.execute("update pet set name = ?, kind = ?, noise = ?, food = ? where id = ?", (
            pet_item["name"],
            pet_item["kind"], 
            pet_item["noise"], 
            pet_item["food"], 
            pet_item["id"]))
    connection.commit()

def delete_pet(id):
    cursor = connection.cursor()
    cursor.execute("delete from pet where id = ?", (id,))
    connection.commit()

