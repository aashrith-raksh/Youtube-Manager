import sqlite3


def init_db():
    con = sqlite3.connect('Youtube.db')
    cur = con.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS YOUTUBE(
        video_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT not null,
        views INTEGER not null,
        channel TEXT not null,
    )
    ''')

    return (con, cur)

