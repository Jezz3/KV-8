import sqlite3


# erstellt neue Tabelle in Datenbank mit Spalten zeit, temperatur, luftdruck,luftfeuchtigkeit,
# falls noch nicht vorhanden
def create_new_table(dbname, tablename):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS {} (
                         zeit DATETIME,
                         temperatur FLOAT,
                         luftdruck FLOAT,
                         luftfeuchtigkeit FLOAT)
                      """.format(tablename)
    c.execute(sql)
    conn.commit()
    conn.close()


# schreibt data in die Tabelle. Dabei hat data die Form zeit, temperatur, luftdruck,luftfeuchtigkeit
def write_data(dbname,data):
    tablename = '"' + str(data[0].date()) + '"'
    create_new_table(dbname, tablename)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = """ INSERT INTO {}
              VALUES(?,?,?,?)""".format(tablename)
    c.execute(sql, data)
    conn.commit()
    conn.close()


# ließt aus Tabelle tag die spalte aus und gibt sie als tuple zurück.
def read_data(dbname, tag, spalte):
    rows = []
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = """SELECT {} FROM {}""".format(spalte, tag)
    for i in c.execute(sql):
        rows.append(i[0])
    return rows

