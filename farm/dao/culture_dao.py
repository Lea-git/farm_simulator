from dao.db import get_connection

def inserer_culture(nom, temps_croissance):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO cultures (nom, temps_croissance) VALUES (?, ?)", (nom, temps_croissance))
    conn.commit()
    conn.close()

def charger_cultures():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT nom, temps_croissance FROM cultures")
    resultats = cur.fetchall()
    conn.close()
    return resultats
