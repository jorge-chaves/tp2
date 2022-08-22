import os
import sys
import time
import mysql.connector as mysql
from flask import Flask

app = Flask(__name__)

# Toma los parametros de variables de entorno
DBHOST=os.getenv('DB_HOST')
DBUSER=os.getenv('DB_USER')
DBPASSWD=os.getenv('DB_PASSWD')


def crear_datos():
    """
    Crea la BD y carga datos
    """
    count = 0
    maxcount = 5
    while True:
        count += 1
        if count > maxcount:
            sys.exit("No se pudo conectar con la base de datos")
        try:
            db = mysql.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD, database='tp2')
            break
        except Exception as e:
            print(f"Intento {count} de {maxcount}. Esperando 5 segundos...")
            time.sleep(5)

    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mensajes (`texto` varchar(200), UNIQUE KEY `texto` (`texto`));")
    cursor.execute("INSERT IGNORE INTO mensajes VALUES ('- Actividad 2 -'),('Grupo Nro. 5 - DevOps'),('Creamos contenedores Docker y mostramos estos mensajes');")
    db.commit()
    db.close()


def traer_mensajes():
    """
    """
    db = mysql.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD, database='tp2')
    cursor = db.cursor()
    cursor.execute('SELECT texto FROM mensajes;')
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
    crear_datos()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
   main()

