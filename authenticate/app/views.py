from app import app
import sqlite3 
from flask import request, jsonify

testAccounts = [
    {
        "user" : "Sparkles",
        "passw" : "Sparkles"
    },
    {
        "user" : "SecLab",
        "passw" : "password"
    }
]


@app.get("/auth/create")
def create():
    #check if user and pass are passed correctly 
    if "user" not in request.args or "passw" not in request.args:
        return "Error: missing username or password"

    #parse request
    user = request.args.get('user')
    passw = request.args.get('passw')

    conn = sqlite3.connect('test.db')
    curs = conn.cursor()

    query = "SELECT * FROM users WHERE user={};".format(user)
    res = curs.execute(query).fetchall()

    if res:
        curs.close()
        return "Username already in use"

    query = "INSERT INTO users (user, passw) VALUES ({}, {});".format(user, passw)

    res = curs.execute(query).fetchall()
    conn.commit()
    curs.close()
    return res

@app.get("/auth/verify")
def auth():
    #check if user and pass are passed correctly 
    if "user" not in request.args or "passw" not in request.args:
        return "Error: missing username or password"

    #parse request
    user = request.args.get('user')
    passw = request.args.get('passw')

    # connect to db
    query = "SELECT * FROM users WHERE user={} AND passw={};".format(user, passw)
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()

    res = curs.execute(query).fetchall()
    
    curs.close()

    if len(res) == 0:
        return "unverified"
    else:
        return "verified"