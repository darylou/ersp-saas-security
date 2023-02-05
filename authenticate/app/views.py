from app import app
import sqlite3 
import psycopg2
from flask import request, jsonify, g

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

def get_db():
    """
      Returns the connection to the database, opening a new
      one if there is none
    """
    if not hasattr(g, 'db'):
        g.db = psycopg2.connect(dbname='saas', user='saas', password='saas', host='db')
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

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

    query = "INSERT INTO accounts (user, passw) VALUES ({}, {})".format(user, passw)
    conn = get_db()
    conn.row_factory = dict_factory
    curs = conn.cursor()

    res = curs.execute(query).fetchall()

    conn.commit()
    curs.close()

    return res 

@app.get("/auth/auth")
def auth():
    #check if user and pass are passed correctly 
    if "user" not in request.args or "passw" not in request.args:
        return "Error: missing username or password"

    #parse request
    user = request.args.get('user')
    passw = request.args.get('passw')
    # user = "daryl"
    # passw = "12354125"
    to_filter = [user]

    # connect to db
    query = "SELECT * FROM accounts WHERE user=?;"
    conn = get_db()
    conn.row_factory = dict_factory
    curs = conn.cursor()

    res = curs.execute(query, to_filter).fetchall()

    if res['passw'] == passw:
        res['auth'] = True 
    else:
        res['auth'] = False 

    curs.close()
    
    return jsonify(res)