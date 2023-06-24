from datetime import date
from Entidades import *
from conexion import *
from Crud import *
from simulacion import *




# MENU
def menu_principal():

    continuar = True
  
    while continuar:
        opcion_correcta = False
     
        while not opcion_correcta:
            print("Bienvenido al sistema del Poder Judicial de la Provincia de Córdoba")
            print("===== Menú Principal =====")
            print("Por favor indique que accion desea realizar")
            print("1°- Ingresar a la base de datos de las Normativas")
            print("2°- Ingresar a la base de datos de Órganos Legislativos")
            print("3°- Ingresar a la base de datos de las Categorías")
            print("4°- Salir")
            print("==========================")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                menu_normativas()
                opcion_correcta = True
            elif opcion == 2:
                menu_organos()
                opcion_correcta = True
            elif opcion == 3:
                menu_categorias()
                opcion_correcta = True
            elif opcion == 4:
                continuar = False
                opcion_correcta = True
                print(" ¡MUCHAS GRACIAS POR USAR NUESTROS SERVICIOS,VUELVA PRONTO")
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

#MENU NORMATIVAS

def menu_normativas():
    continuar = True

    while continuar:
        
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú Normativas =====")
            print("1°- Insertar una nueva Normativa")
            print("2°- Buscar una Normativa")
            print("3°- Actualizar una Normativa")
            print("4°- Eliminar una Normativa")
            print("5°- Consultar todas las Normativas registradas en la base de datos")
            print("6°- buscar una normativa por palabra clave")
            print("7°- Volver al Menú Principal")
            print("==========================")
            
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                insertar_nueva_normativa ()
                opcion_correcta = True
            elif opcion == 2:
                buscar_normativa()
                opcion_correcta = True
            elif opcion == 3:
                modificar_descripcion_normativa()
                opcion_correcta = True
            elif opcion == 4:
                borrar_normativa()
                opcion_correcta = True
            elif opcion == 5:
                buscar_all_normativas()
                opcion_correcta = True
            elif opcion == 6:
                buscar_norma_palabra_clave()
                opcion_correcta = True
            elif opcion == 7:
                continuar = False
                opcion_correcta = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
            
        
 #MENU ORGANOS LEGISLATIVOS           

def menu_organos():
    continuar = True

    while continuar:
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú Órganos Legislativos =====")
            print("1°- Consultar todos los Órganos Legislativos registrados en la base de datos")
            print("2°- Volver al Menú Principal")
            print("==========================")
            opcion = int(input("Seleccione una opción: "))
         
            if opcion == 1:
                buscar_organos()
                opcion_correcta = True
            
            elif opcion == 2:
                continuar = False
                opcion_correcta = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
           
#MENU CATEGORIAS

def menu_categorias():
    continuar = True

    while continuar:
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú Categorías =====")
            print("1°- Insertar una nueva Categoría")
            print("2°- Buscar una Categoría")
            print("3°- Actualizar una Categoría")
            print("4°- Consultar todas las Categorías registradas en la base de datos")
            print("5°- Volver al Menú Principal")
            print("==========================")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                insertar_categorias()
                opcion_correcta = True
            elif opcion == 2:
                buscar_categoria()
                opcion_correcta = True
            elif opcion == 3:
                modificar_categorias()
                opcion_correcta = True
            elif opcion == 4:
                buscar_all_categorias()
                opcion_correcta = True
            elif opcion == 5:
                continuar = False
                opcion_correcta = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

menu_principal()