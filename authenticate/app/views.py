from app import app
import sqlite3 
from flask import request, jsonify

testAccounts = [
    {
        "user" : "sparkles",
        "passw" : "password"
    },
    {
        "user" : "seclab",
        "passw" : "seclab"
    }
]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.get("/auth/create")
def create():
    #check if user and pass are passed correctly 
    if "user" not in request.args or "passw" not in request.args:
        return "Error: missing username or password"

    #parse request
    user = request.args.get('user')
    passw = request.args.get('passw')

    query = "INSERT INTO users (user, passw) VALUES ({}, {})".format(user, passw)
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    curs = conn.cursor()

    res = curs.execute(query).fetchall()
    return res 

@app.get("/auth/auth")
def auth():
    #check if user and pass are passed correctly 
    if "user" not in request.args or "passw" not in request.args:
        return "Error: missing username or password"

    #parse request
    user = request.args.get('user')
    passw = request.args.get('passw')
    to_filter = [user]

    # connect to db
    query = "SELECT * FROM accounts WHERE user=?;"
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    curs = conn.cursor()

    res = curs.execute(query, to_filter).fetchall()

    if res['passw'] == passw:
        res['auth'] = True 
    else:
        res['auth'] = False 

    return jsonify(res)