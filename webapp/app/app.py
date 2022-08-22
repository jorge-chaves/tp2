import os
import sys
import mysql.connector as mysql
from flask import Flask

app = Flask(__name__)

# Toma los parametros de variables de entorno
DBHOST=os.getenv('DB_HOST')
DBUSER=os.getenv('DB_USER')
DBPASSWD=os.getenv('DB_PASSWD')


def traer_mensajes():
    """
    """
    db = mysql.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD)
    cursor = db.cursor()
    cursor.execute('SELECT texto FROM tp2.mensajes;')
    rows = cursor.fetchall()
    mensajes = [x[0] for x in rows]
    db.close()
    return mensajes


@app.route('/')
def index():
    """
    """
    mensajes = traer_mensajes()
    lista = " ".join([ f'<ul>{x}</ul>' for x in mensajes ])

    html = f"""
      <h3>Mensajes</h3>
      <ul>
        {lista}
      </ul>
    """

    return html


def main():
    """
    Punto de entrada de la aplicacion
    """
    app.run(host='0.0.0.0')


if __name__ == '__main__':
   main()

