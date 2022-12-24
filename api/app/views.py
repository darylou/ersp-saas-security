from app import app
from flask import abort, request, jsonify, g, render_template, redirect, url_for
import sqlite3
import psycopg2
import humanize

def get_db():
    """
      Returns the connection to the database, opening a new
      one if there is none
    """
    if not hasattr(g, 'db'):
        g.db = psycopg2.connect(dbname='postgres', user='saas', password='saas', host='db')
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

@app.get('/api/db')
def show_guestbook():
    sql = """SELECT author,comment_text,posted_at,id FROM guestbook order by posted_at DESC;"""
    cur = get_db().cursor()
    cur.execute(sql)

    posts = []
    for post_in_db in cur.fetchall():
        posts.append(
            {
                'author': post_in_db[0],
                'comment_text': post_in_db[1],
                'posted_at': humanize.naturaltime(post_in_db[2]),
                'id': post_in_db[3]
            }
        )
        cur.close()
    return render_template('index.html', posts=posts)

@app.route('/api/db/add', methods = ['POST'])
def add_post():
    sql = """INSERT INTO guestbook (author,comment_text,posted_at) VALUES (%s,%s, now());"""
    db = get_db()
    cur = db.cursor()
    cur.execute(sql,(request.form['author'], request.form['comment_text']))
    db.commit()
    return redirect(url_for('show_guestbook'))



@app.get("/api/paste")
def get_paste():
    # username = request.form['username']
    username = 'daryl'

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM pastes WHERE username = '" + username + "'")
    body = res.fetchall()[0][1]
    con.close()

    response = jsonify({"body": body})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.post("/api/paste")
def post_paste():
    # username = request.form['username']
    # body = request.form['body']
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