import mysql.connector
from conexion import DatabaseConnection
from datetime import date
import Entidades

#ESTE ES UN PROGRAMA PARA ACTUALIZAR LA BASE DE DATOS CON LOS DATOS BASE
#INSERT DE CATEGORIAS
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
    password="s1nc0d1f1c4r",
    port="3306",
    database="poderjudicial"
)

# Establecer la conexión con la base de datos
db_connection.connect()

# Obtener el cursor de la conexión
cursor = db_connection.connection.cursor()

# Ejecuta la consulta PARA INSERTAR LOS ORGANOS LEGISLATIVOS
sentencia = "INSERT INTO organoslegislativos (organo_legislativo) VALUES (%s)"
values = [("Nacional: Congreso de la Nacion"), ("Provincial: Legislatura de la provincia de Cordoba")]  # Valores a insertar

try:
    cursor.executemany(sentencia, [(value,) for value in values])
    db_connection.connection.commit()
    print("Registros insertados correctamente")
except mysql.connector.Error as error:
    print(f"Error al insertar los registros: {error}")

# Llamar a la función insertar_categoria para insertar LAS CATEGORIAS
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

#Ejecutar la consulta
sentencia = "INSERT INTO normativas (tipo_normativa,nro_normativa,fecha_sancion,descripcion,jurisdiccion,palabra_clave,ID_categoria,ID_organo_legislativo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
valor = ("Ley","20744",date(1976, 5, 13),"""La Ley de Contrato de Trabajo establece los derechos y obligaciones tanto de los empleadores como de los trabajadores.Regula cuestiones basicas de una relacion laboral,como la jornada laboral, descansos, remuneración,
licencias y las modalidades del contrato de trabajo. Es una ley que tiene como objetivo garantizar condiciones justas y
equitativas para el trabajador,estableciendo en su art 7 la nulidad de condiciones menos favorables para este a las
establecidas en esta ley, y en caso de duda prevalecera la mas favorable al trabajador (art 9).
A los efectos de esta ley,se considera relacion de trabajo cuando una persona realice actos, ejecute obras o preste
servicio en favor de otra, bajo la dependencia de ésta en forma voluntaria y mediante el pago de una remuneración,
cualquiera sea el acto que le dé origen""","Nacional","Trabajo","1","1" ),("Ley","26388",date(2008,6,4),"""La ley de delitos informaticos es una ley que ordena la modificacion de diversos articulos del codigo penal,regulando y
estableciendo una nueva escala penal para aquellos delitos cometidos con el uso de tecnologias., ya sea a través de
medios electrónicos, informáticos o telemáticos,como tambien a los delitos que afecten la confidencialidad, integridad y
disponibilidad de los datos y sistemas informáticos,entre otros. ""","Nacional","Delito Informatico","2","1"),("Ley","7642",date(1987,11,21),"""La ley de ejercicio profesional en ciencias informaticas es una ley que regula todo lo atinente al desenvolvimiento de la
actividad informatica en la provincia de Córdoba.Establece como condicion para el ejercicio de la profesion en la
provincia la matriculacion obligatoria, imponiendo como requisito contar con título oficial reconocido a nivel nacional o
provincial en carreras de Ciencias Informáticas de nivel terciario como mínimo. Ademas establece la constitucion y
funciones del CONSEJO PROFESIONAL,quien estara a cargo del gobierno de la matricula,y de dar cumplimiento a todo
lo dispuesto por esta ley""","Provincial","Profesional de las ciencias informaticas","8","2") # Valor a insertar
try:
    cursor.executemany(sentencia, valor)
    db_connection.connection.commit()
    print("Registro insertado correctamente")
except mysql.connector.Error as error:
    print(f"Error al insertar el registro: {error}")

#Cerrar el cursor
cursor.close()

#Cerrar Conexion
db_connection.close()    
