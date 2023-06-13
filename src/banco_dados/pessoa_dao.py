from . import db

def insert(id, nome, cpf):
    conn = db.conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoa (id, nome, cpf) VALUES (%s, %s, %s)", (id, nome, cpf))
    cursor.close()
    conn.commit()
    conn.close()