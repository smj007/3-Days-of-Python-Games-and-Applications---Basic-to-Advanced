import sqlite3

def connect():
    conn = sqlite3.connect('schedule.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS schedule (Id INTEGER PRIMARY KEY, date text, earnings integer, exercise text, study text, diet text, python text)")
    conn.commit()
    conn.close()


def insert(date, earnings, exercise, study, diet, python):
    conn = sqlite3.connect('schedule.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO schedule VALUES (NULL, ?, ?, ?, ?, ?, ?)", (date, earnings, exercise, study, diet, python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('schedule.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schedule")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('schedule.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM schedule WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def search(date = '', earnings = '', exercise = '', study = '', diet = '', python = ''):
    conn = sqlite3.connect('schedule.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schedule WHERE date = ? OR earnings = ? OR exercise = ? OR study = ? OR diet = ? OR python = ?", (date, earnings, exercise, study, diet, python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


connect()
insert('4-1-2019', 8000, 'did exercise', 'study', 'did diet', 'no python')
insert('6-1-2019', 18000, 'no exercise', 'no study', 'no diet', 'did python')
insert('9-1-2019', 38000, 'no exercise', 'study', 'did diet', 'no python')
insert('9-1-2019', 81000, 'did exercise', 'study', 'no diet', 'did python')
print(view())
