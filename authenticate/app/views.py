from app import app
import sqlite3 
import psycopg2
from flask import abort, request, jsonify, g

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

@app.post("/auth/create/<user>/<passw>")
def create(user, passw):
    #check if user and pass are passed correctly 
    # if "user" not in request.args or "passw" not in request.args:
    #     abort(400)

    #parse request
    # user = request.args.get('user')
    # passw = request.args.get('passw')

    query = "INSERT INTO accounts (username, passw) VALUES ('{}', '{}')".format(user, passw)
    conn = get_db()
    curs = conn.cursor()

    curs.execute(query)

    conn.commit()
    curs.close()

    return jsonify({})

@app.get("/auth/auth/<user>/<passw>")
def auth(user, passw):
    #check if user and pass are passed correctly 
    # if "user" not in request.args or "passw" not in request.args:
    #     abort(400)

    #parse request
    # user = request.args.get('user')
    # passw = request.args.get('passw')
    # user = "daryl"
    # passw = "12354125"
    # to_filter = [user]

    # connect to db
    query = "SELECT * FROM accounts WHERE username = '{}' AND passw = '{}';".format(user, passw)
    conn = get_db()
    curs = conn.cursor()

    curs.execute(query)
    
    res = curs.fetchall()

    if not res:
        abort(401)

    curs.close()
    
    return jsonify(res)