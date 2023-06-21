import mysql.connector
from conexion import DatabaseConnection

#Crear funcion insertar categoria
def insertar_categoria(connection, categoria):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO categorias (categoria) VALUES (%s)"
        values = (categoria,)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Categoria agregada")
    except mysql.connector.Error as err:
        print("Error al insertar categoria:", err)

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="root",
    port="3306",
    database="poderjudicial"
)

#Establecer conexion
db_connection.connect()


# Llamar a la función insertar_categoria para insertar múltiples categorías
categorias = [
    "Laboral",
    "Penal",
    "Civil",
    "Comercial",
    "Familia y Sucesiones",
    "Agrario y Ambiental",
    "Minería",
    "Derecho informático"
]

for categoria in categorias:
    insertar_categoria(db_connection, categoria)


#Cerrar conexion
db_connection.close()