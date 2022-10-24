from app import app
from flask import request, jsonify, sqlite3

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

@app.get("api/auth")
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
    conn = sqlite3.connect('example.db')
    conn.row_factory = dict_factory
    curs = conn.cursor()

    res = curr.execute(query, to_filter).fetchall()

    if res['passw'] == passw:
        res['auth'] = True 
    else:
        res['auth'] = False 

    return jsonify(res)