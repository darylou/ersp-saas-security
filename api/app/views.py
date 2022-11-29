from app import app
from flask import abort, request
import sqlite3

@app.get("/api/paste")
def get_paste():
    #username = request.form['username']
    username = 'daryl'

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM pastes WHERE username = '" + username + "'")
    body = res.fetchall()[0][1]
    con.close()
    return {
        "body": body,
    }


@app.post("/api/paste3")
def post_paste():
    #username = request.form['username']
    #body = request.form['body']
    username = 'daryl'
    body = 'this is my second paste'

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM pastes WHERE username = '" + username + "'")

    
    if len(res.fetchall()) == 0:
        cur.execute("INSERT INTO pastes ('username','paste') VALUES ('" + username + "','" + body + "')")
    else:
        cur.execute("UPDATE pastes SET paste = '" + body + "' WHERE username = '" + username + "'")
    
    con.commit()

    data = cur.execute("SELECT * FROM pastes")
    for row in data:
        print(row);



    con.close()
    
    return {
        "stub": "stub",
    }