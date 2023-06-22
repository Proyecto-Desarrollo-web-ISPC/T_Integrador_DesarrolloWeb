from insertbase import InsertBase

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('CONSULTA POR NUMERO DE LEY', consultaPorNumeroLey),
        '2': ('CONSULTA POR PALABRA CLAVE', consultaPorPalabraClave),
        '3': ('INICIALIZAR BASE DE DATOS', incializarDB),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def consultaPorNumeroLey():
    print('Has elegido la opción 1')

def consultaPorPalabraClave():
    print('Has elegido la opción 2')

def incializarDB():
    initDataBase = InsertBase()
    initDataBase.initdb()
    
def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()