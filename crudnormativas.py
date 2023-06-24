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