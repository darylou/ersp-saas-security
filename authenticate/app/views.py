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

    query = "INSERT INTO accounts (username, passw) VALUES ('{}', '{}');".format(user, passw)
    conn = get_db()
    curs = conn.cursor()

    res = curs.execute(query).fetchall()
    return res 

@app.get("/auth/auth")
def auth():
    #check if user and pass are passed correctly 
    if "user" not in request.args or "passw" not in request.args:
        return "Error: missing username or password"

    #parse request
    # user = request.args.get('user')
    # passw = request.args.get('passw')
    user = "daryl"
    passw = "12354125"
    to_filter = [user]

    # connect to db

    query = "SELECT * FROM accounts WHERE username = '{}' AND passw = '{}';".format(user, passw)
    conn = get_db()

    curs = conn.cursor()

    curs.execute(query)
    res = curs.fetchall()

    if res['passw'] == passw:
        res['auth'] = True 
    else:
        res['auth'] = False 

    return jsonify(res)