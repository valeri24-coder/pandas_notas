import mysql.connector
import pandas as pd


# CONEXION A MYSQL
def conectar():

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="notas_estudiantes"
    )

    return conexion


# OBTENER USUARIOS
def obtenerusuarios(username):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM usuarios WHERE username = %s"

    cursor.execute(query, (username,))

    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    return usuario


# OBTENER ESTUDIANTES
def obtenerestudiantes():

    conn = conectar()

    query = "SELECT * FROM estudiantes"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


# INSERTAR ESTUDIANTE
def insertar_estudiante(
        nombre,
        edad,
        carrera,
        nota1,
        nota2,
        nota3,
        promedio,
        desempeno
):

    conn = conectar()
    cursor = conn.cursor()

    query = """
    INSERT INTO estudiantes
    (nombre_estu, edad_estu, carrera, nota1, nota2, nota3, promedio, desempeno)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (
        nombre,
        edad,
        carrera,
        nota1,
        nota2,
        nota3,
        promedio,
        desempeno
    ))

    conn.commit()

    cursor.close()
    conn.close()


# PROBAR CONEXION
if __name__ == "__main__":

    conn = conectar()

    if conn.is_connected():
        print("Conexión exitosa a MySQL")

    conn.close()