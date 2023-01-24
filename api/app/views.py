from app import app
from flask import abort, request, jsonify
import sqlite3

@app.get("/api/paste")
def get_paste():
    print("test1")
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM Pastes")

    counter = 0;
    body = {}

    for i in res.fetchall():
        body["post_id_" + str(counter)] = i[0]
        body["post_title_" + str(counter)] = i[1]
        body["post_body_" + str(counter)] = i[2]
        counter += 1;

    con.close()

    response = jsonify(body)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.post("/api/paste/<paste_id>/<title>/<body>")
def post_paste(paste_id, title, body):
    print("test2")
    #print(request.form['title'])
    #title = request.form['title']
    #body = request.form['body']
    #paste_id = request.form['id']

    print("test3")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM Pastes WHERE id = '" + paste_id + "'")

    
    if len(res.fetchall()) == 0:
        
        cur.execute("INSERT INTO Pastes (id, title, body) VALUES ('" + paste_id + "','"+ title + "','"+ body + "')")
        
    else:
        cur.execute("UPDATE Pastes SET body = '" + body + "' WHERE id = '" + paste_id + "'")
        cur.execute("UPDATE Pastes SET title = '" + title + "' WHERE id = '" + paste_id + "'")
    
    con.commit()

    data = cur.execute("SELECT * FROM Pastes")
    for row in data:
        print(row);



    con.close()
    
    response = jsonify({"status": 201})
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response