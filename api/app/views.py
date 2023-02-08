from app import app
from flask import abort, request, jsonify, g
import sqlite3
import psycopg2
import humanize

def get_db():
    """
      Returns the connection to the database, opening a new
      one if there is none
    """
    print("HI")
    if not hasattr(g, 'db'):
        g.db = psycopg2.connect(dbname='saas', user='saas', password='saas', host='db')
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

@app.get("/api/paste")
def get_paste():
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM pastes")

    counter = 0;
    body = {}

    for i in cur.fetchall():
        body["post_id_" + str(counter)] = i[0]
        body["post_title_" + str(counter)] = i[1]
        body["post_body_" + str(counter)] = i[2]
        counter += 1;

    cur.close()

    response = jsonify(body)
    return response

@app.get("/api/test")
def get_test():
    response = jsonify({"status": 400})
    return response


@app.post("/api/paste/<paste_id>/<title>/<body>")
def post_paste(paste_id, title, body):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM pastes WHERE id = '" + paste_id + "'")
    
    if len(cur.fetchall()) == 0: 
        cur.execute("INSERT INTO pastes (id, title, body) VALUES ('" + paste_id + "','"+ title + "','"+ body + "')") 
    else:
        cur.execute("UPDATE pastes SET body = '" + body + "' WHERE id = '" + paste_id + "'")
        cur.execute("UPDATE pastes SET title = '" + title + "' WHERE id = '" + paste_id + "'")
    
    db.commit()
    cur.close()
    
    return jsonify({})

@app.delete("/api/paste/<paste_id>")
def delete_paste(paste_id):
    db = get_db()
    cur = db.cursor()

    cur.execute("DELETE FROM pastes WHERE id = '" + paste_id + "'")

    db.commit()

    cur.close()

    return jsonify({})