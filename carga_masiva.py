import mysql.connector
from datetime import date
from Entidades import *
from conexion import *

connection = DatabaseConnection(
    host='localhost',
    user='root', 


    password='***',
    port='****',
    database='****'
    password='****',
    port='****',
    database='****'


    password='*************',
    port='****',
    database='****'

    )
def insertar_categorias(connection, categoria):
    
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "INSERT INTO categorias (categoria) VALUES (%s)"
        values = (categoria,)
        cursor.execute(query, values)
        connection.connection.commit()
        print ("se registro correctamente")

    except mysql.connector.Error as err:
        print("Error al insertar categoria:", err)
    finally:
        cursor.close()
        connection.close()

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
    insertar_categorias(connection, categoria)



def insertar_organoLegislativo():
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "INSERT INTO organoslegislativos (organo_legislativo) VALUES (%s)"
        values =[("Congreso de la Nacion : NACIONAL",), ("Legislatura de la provincia de Cordoba : PROVINCIAL",)]
        cursor.executemany(query, values)
        connection.connection.commit()
        print ("se registro correctamente")

    except mysql.connector.Error as err:
        print("Error al insertar datos:", err)
    finally:
        cursor.close()
        connection.close()
    
insertar_organoLegislativo()

def insertar_Normativas():
    try:
        connection.connect()
        cursor = connection.connection.cursor()
        query = "INSERT INTO normativas(tipo_normativa,nro_normativa,fecha_sancion,descripcion,jurisdiccion,palabra_clave,ID_categoria,ID_organo_legislativo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values =("Ley","20744",date(1976, 5, 13),"""La Ley de Contrato de Trabajo establece los derechos y obligaciones tanto de los empleadores como de los trabajadores.Regula cuestiones basicas de una relacion laboral,como la jornada laboral, descansos, remuneración,
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
lo dispuesto por esta ley""","Provincial","Profesional de las ciencias informaticas","8","2"),("ley", "24241" ,date (1993,9,23), """La ley del Sistema Integrado de Jubilaciones y Pensiones establece las disposiciones legales y regulaciones relacionadas con el otorgamiento y el cálculo de las jubilaciones y pensiones para los ciudadanos argentinos. La ley aborda varios aspectos importantes, como los requisitos para acceder a una jubilación o pensión, los beneficios y derechos de los beneficiarios, el cálculo de los montos de jubilación o pensión, los mecanismos de actualización y ajuste de los montos, y las condiciones para la otorgación de pensiones por invalidez, entre otros temas relacionados.""", "Nacional", "de jubilaciones y pensiones","1","1"), ("ley", "24557" ,date (1996,5,1), """La ley de accidentes de trabajo establece que los empleadores deben tomar medidas para prevenir accidentes y enfermedades laborales, proporcionar condiciones de trabajo seguras y capacitar a sus empleados en temas de seguridad. Además, establece la obligatoriedad de contratar un seguro de riesgos del trabajo que cubra los accidentes y enfermedades laborales. En caso de ocurrir un accidente laboral, la ley establece los procedimientos para la atención médica, rehabilitación y compensación de los trabajadores afectados. También establece los mecanismos de determinación de responsabilidad y las formas de reclamo por parte de los trabajadores.""", "Nacional", "de accidentes laborales,","1","1"),  ("ley", "27555" ,date (2020, 8,14), """La ley de teletrabajo es una normativa que regula los derechos y obligaciones de las partes(empleador y trabajador) cuando la actividad laboral se desarrolla a distancia,ya sea de manera total o parcial en el domicilio del trabajador,o en lugares distintos al del establecimiento del empleador,por medio de tecnologías de la información y comunicación.Establece los derechos y garantías para los trabajadores que desempeñan su actividad bajo esta modalidad,como el derecho a la desconexión digital(art 5), a la intimidad, a la capacitación, a la igualdad de trato y oportunidades, a la protección de la salud y seguridad laboral.""", "Nacional", "teletrabajo","1","1") ,  ("ley", "26653" ,date (2010,11,3), """LEY DE ACCESIBILIDAD DE LA INFORMACION EN LAS PAGINAS WEB. Todo sitio web público o privado deberá respetar en los diseños de sus páginas web las normas y requisitos sobre accesibilidad de la información que faciliten el acceso a sus contenidos, a todas las personas con discapacidad con el objeto de garantizarles la igualdad real de oportunidades y trato, evitando así todo tipo de discriminación.""", "Nacional", "accesibilidad","8","1"), ("ley", "25326" ,date (2000,10,4), """La ley de protección de datos personales establece los principios y normas que deben seguir tanto los organismos públicos como las empresas privadas al recolectar, almacenar, utilizar y compartir datos personales. Garantiza el derecho de las personas a conocer qué información se recopila, para qué se utiliza y quiénes tienen acceso a ella. También establece la obligación de obtener el consentimiento de los individuos para el uso de sus datos personales.
Además, la ley establece medidas de seguridad para proteger los datos personales de posibles filtraciones, pérdidas o accesos no autorizados. También establece la creación de un ente de control, la Agencia de Acceso a la Información Pública, encargada de velar por el cumplimiento de esta ley.""", "Nacional", "Datos","8","1")
        # Valor a insertar

        cursor.executemany(query, values)
        connection.connection.commit()
        print ("se registro correctamente")

    except mysql.connector.Error as err:
        print("Error al insertar datos:", err)
    finally:

        cursor.close()
        connection.close()

insertar_Normativas()