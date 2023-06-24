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



#CRUD NORMATIVAS
def buscar_normativa_numero(numero_normativa):
    try:
        connection.connect()
        cursor =connection.connection.cursor()
        query = "SELECT * FROM normativas WHERE nro_normativa = %s"
        values = (numero_normativa,)
        cursor.execute(query, values)
        resultados = cursor.fetchall()
        
        return resultados
    except mysql.connector.Error as err:
        print("Error al buscar la normativa:", err)
    finally:
        cursor.close()
        connection.close()
        
       

       

def delete_normativa( nro_normativa):
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "DELETE FROM normativas WHERE nro_normativa = %s"
        values=(nro_normativa,)
        cursor.execute(query, values)
        norma = cursor.fetchone()
       

        connection.connection.commit()
       
    except mysql.connector.Error as err:
        print("Error al borrar la normativa:", err)
    finally:
        cursor.close()
        connection.close()

def buscar(palabra_clave):
    try:
        connection.connect()
        cursor =connection.connection.cursor()
        query = "SELECT * FROM normativas WHERE palabra_clave LIKE %s"
        values = ("%" + palabra_clave + "%",)
        cursor.execute(query, values)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as err:
        print("Error al buscar normativas por palabra clave:", err)
    finally:
        cursor.close()
        connection.close()


def modificar_descripcion(id_registro, nueva_descripcion):
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "UPDATE normativas SET descripcion = %s WHERE ID_nroregistro = %s"
        values = (nueva_descripcion, id_registro)
        cursor.execute(query, values)
        connection.connection.commit()
        objeto = cursor.fetchall()
        return objeto
        print("El campo 'descripcion' se ha modificado correctamente.")
    except mysql.connector.Error as err:
        print("Error al modificar el campo 'descripcion':", err)
    finally:
        cursor.close()
        connection.close()


def consultar_normativas():
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "SELECT * FROM normativas"
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados

    except mysql.connector.Error as err:
        print("Error al buscar normativas:", err)
    finally:
        cursor.close()
        connection.close()




def insertar_Normativas(tipo,numero_normativa,fecha,descripcion,jurisdiccion,palabra_clave,categoria_id,id_organo):
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "INSERT INTO normativas(tipo_normativa,nro_normativa,fecha_sancion,descripcion,jurisdiccion,palabra_clave,ID_categoria,ID_organo_legislativo)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (tipo,numero_normativa,fecha,descripcion,jurisdiccion,palabra_clave,categoria_id,id_organo)
        cursor.executemany(query, (values,))
        connection.connection.commit()
        id_insertado = cursor.lastrowid
        return id_insertado
        print("la normativa se inserto correctamente en la base de datos.")
    except mysql.connector.Error as err:
        print("Error al intentar insertar la normativa:", err)
    finally:
        cursor.close()
        connection.close()
        
def listar_palabras():
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "SELECT palabra_clave FROM normativas"

        cursor.execute(query)
        resultados = cursor.fetchall()
        palabras_clave = [resultado[0] for resultado in resultados]
        return palabras_clave
       
       
    except mysql.connector.Error as err:
        print("Error al buscar normativas por palabra clave:", err)
    finally:
         cursor.close()