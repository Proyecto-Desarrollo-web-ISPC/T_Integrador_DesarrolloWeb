import mysql.connector
from conexion import *
from datetime import date
from Entidades import *
from conexion import *

#crud normativas
def insertar_categoria(categoria):
    
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "INSERT INTO categorias (categoria) VALUES (%s)"
        values = (categoria,)
        cursor.execute(query, values)
        connection.connection.commit()
        id_insertado = cursor.lastrowid
        return id_insertado
        
    except mysql.connector.Error as err:
        print("Error al insertar categoria:", err)
    finally:
        cursor.close()
        connection.close()




def buscarCategoria_id(nombre_categoria):
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "SELECT ID_categoria FROM categorias WHERE categoria = %s"
        values = (nombre_categoria,)
        cursor.execute(query, values)
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]  
        else:
            return None 
    
    except mysql.connector.Error as err:
        print("Error al buscar categoria:", err)
    finally:
        cursor.close()
        connection.close()


def modificar_categoria(id_categoria,nueva_categoria):
     try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "UPDATE categorias SET categoria = %s WHERE ID_categoria = %s"
        cursor.execute(query,(nueva_categoria,id_categoria))
        connection.connection.commit()
        categoria_modificada = cursor.fetchone()
        
        if categoria_modificada:
            return categoria_modificada

     except mysql.connector.Error as err:
        print("Error al modificar una categoria:", err)
     finally:
        cursor.close()
        connection.close()


def consultar_todas():
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "SELECT * FROM categorias"
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados

    except mysql.connector.Error as err:
        print("Error al buscar categorias:", err)
    finally:
        cursor.close()
        connection.close()



#CRUD ORGANOS LEGISLATIVOS

def buscar_organo(organo_legislativo):
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "SELECT ID_organo_legislativo FROM organoslegislativos WHERE organo_legislativo = %s"
        values = (organo_legislativo,)
        cursor.execute(query, values)
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]  
        else:
            return None 
    
    except mysql.connector.Error as err:
        print("Error al buscar categoria:", err)
    finally:
        cursor.close()
        connection.close()




def consultar_organos():
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "SELECT * FROM organoslegislativos"
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados

    except mysql.connector.Error as err:
        print("Error al buscar categorias:", err)
    finally:
        cursor.close()
        connection.close()