import mysql.connector
from mysql.connector import Error
# definimos una clase llamada DatabaseConnection que establece la conexión con la base de datos MySQL
class DatabaseConnection:


    def __init__(self, host, user, password, port, database): 

# establecemos los atributos de la clase, datos necesarios para establecer la conexión
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None 
# Este valor inicial puede ser útil para verificar posteriormente si la conexión ha sido exitosa o no.

    def connect(self):
# se define el método connect dentro de la clase DatabaseConnection, que permite establecer la conexión con la base de datos MySQL utilizando los atributos de la instancia de la clase
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port, 
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
# si ocurre algún error durante la conexión, se captura la excepción y se imprime un mensaje de error más descriptivo
            print("No se pudo establecer la conexión: {}".format(error))


    def close(self):  #cerramos conexion
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

