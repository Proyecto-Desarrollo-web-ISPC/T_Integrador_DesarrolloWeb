import mysql.connector          
                        
def buscar_normativa_por_numero(numero_normativa):
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect('ProyectoPoder_judicial.sql')

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Crear la consulta SQL con el número de normativa
    consulta = "SELECT * FROM normativas WHERE nro_normativa = ?"

    try:
        # Ejecutar la consulta con el número de normativa
        cursor.execute(consulta, (numero_normativa))
        resultado = cursor.fetchall()

        if resultado:
            for row in resultado:
                print(f"ID: {row[0]}, Tipo: {row[1]}, Número: {row[2]}, Fecha: {row[3]}, Descripción: {row[4]}")  # Ajusta los índices según tu estructura de tabla
        else:
            print("No se encontraron resultados para el número de normativa ingresado")
    except mysql.connector.Error as error:
        print(f"Error al buscar la normativa: {error}")
    finally:
        cursor.close()
        conexion.close()

#Ejemplo de uso
numero_normativa_buscar = input("Ingrese el número de normativa a buscar: ")

buscar_normativa_por_numero(numero_normativa_buscar)                        