from datetime import datetime
from Entidades import *
from conexion import *
from Crud import *


#SERVICIOS CATEGORIAS
def insertar_categorias():
    
 try:

    categoria = input("Ingrese la categoria que desea agregar a la base de datos: ")
    if not categoria:
        raise ValueError("La categoria no puede estar vacía")
    elif categoria.isdigit():
        raise ValueError("La categoria debe ser una cadena de texto, no un número")
    # cuando ingrese una categoria valida
    else:
        resultado = buscarCategoria_id(categoria)
        if resultado is None:
           id_categoria= insertar_categoria(categoria)
           categoria1=Categorias(None,None)
           categoria1.categoria= categoria
           categoria1.ID_categoria= id_categoria



           print(f"felicitaciones,la categoria ya fue insertada con los siguientes datos:  {str(categoria1)}")
        else:
           print("¡LA CATEGORIA INGRESADA YA EXISTE EN NUESTRA BASE DE DATOS!")
        
            
 except ValueError as error:
    print("Error:", error)


def modificar_categorias():
 try:

    categoria = input("Ingrese la categoria que desea modificar en la base de datos: ")
    if not categoria:
        raise ValueError("La categoria no puede estar vacía")
    elif categoria.isdigit():
        raise ValueError("La categoria debe ser una cadena de texto, no un número")
    # cuando ingrese una categoria valida
    else:
      categoria2= Categorias(None,None)
      categoria3= Categorias(None,None)
      categoria_id = buscarCategoria_id(categoria)
      if categoria_id is None :
         return print("no se encontro una categoria existente en la base de datos")
         
      else:
       categoria2.ID_categoria= categoria_id
      categoria2.categoria= categoria
      categoria_vieja= categoria2
      
      nueva_categoria = input("Ingrese la  nueva categoria: ")
      if not nueva_categoria:
        raise ValueError("La categoria no puede estar vacía")
      elif nueva_categoria.isdigit():
        raise ValueError("La categoria debe ser una cadena de texto, no un número")
      else:
          modificar_categoria(categoria_id,nueva_categoria)
          categoria3=nueva_categoria
          print (f"felicitaciones,la categoria: {str(categoria2)} fue actualizada con los siguientes datos:  {str(categoria3)}")

 except ValueError as error:
    print("Error:", error)


def buscar_categoria():
   try:
       categoria = input("Ingrese la categoria que desea buscar en la base de datos: ")
       if not categoria:
        raise ValueError("La categoria no puede estar vacía")
       elif categoria.isdigit():
        raise ValueError("La categoria debe ser una cadena de texto, no un número")
    
       else:
          resultado = buscarCategoria_id(categoria)
          if resultado is None:
             print("no se encontro una categoria existente en la base de datos,por favor intente nuevamente")
          else:
             print (f"se encontro la categoria: {categoria} con el id: {resultado}")
   except ValueError as error:
    print("Error:", error)

     
def buscar_all_categorias():
   resultados=consultar_todas()
   print("Resultados:")
   for resultado in resultados:
     print("ID:", resultado[0])
     print("categoria:", resultado[1])
   


#SERVICIOS ORGANOS_LEGISLATIVOS

def buscar_organos():
   resultados=consultar_organos()
   for categoria in resultados:
    print(categoria)



#SERVICIOS NORMATIVAS

def buscar_normativa():
   try:
       numero_norma = int(input("Ingrese el numero de la norma que desea buscar en la base de datos: "))
       if not numero_norma:
        raise ValueError("el numero de norma no puede estar vacía")
      
       resultados = buscar_normativa_numero(numero_norma)
       if not resultados:
            print("No se encontraron normativas con ese numero. Por favor, intente nuevamente.")
       else:
            print("Resultados:")
            for resultado in resultados:
                print("ID:", resultado[0])
                print("Tipo:", resultado[1])
                print("Número:", resultado[2])
                print("Fecha:", resultado[3])
                print("Descripción:", resultado[4])
                print("Jurisdicción:", resultado[5])
                print("palabra clave:", resultado[6])
                print("ID categoria:", resultado[7])
                print("ID organo legislativo:", resultado[8])
                print("----------------------------------------")

   except ValueError as error:
        print("Error:", error)


def borrar_normativa():
   try:
    nro_normativa = int(input("Por favor ingrese el numero de la norma que desea eliminar: "))
    if nro_normativa <= 0:
        raise ValueError("el numero de la norma no puede ser cero o negativo")
    
    # cuando ingrese una categoria valida
    else:
       valor=buscar_normativa_numero(nro_normativa)
       if len(valor) == 0:
           return print("no existe una normativa con ese numero en la base de datos")
       delete_normativa( nro_normativa)
       print(f"La Normativa con numero: {nro_normativa} fue eliminada correctamente")

   except ValueError as error:
    print("el numero no puede estar vacio:", error)



def buscar_norma_palabra_clave():
    try:
        palabra_clave = input("Ingrese la palabra clave que desea buscar en la base de datos: ")
        if not palabra_clave:
            raise ValueError("La palabra clave no puede estar vacía")

        resultados = buscar(palabra_clave)
        if not resultados:
            print("No se encontraron normativas con esa palabra clave. Por favor, intente nuevamente.")
        else:
            print("Resultados:")
            for resultado in resultados:
                print("ID:", resultado[0])
                print("Tipo:", resultado[1])
                print("Número:", resultado[2])
                print("Fecha:", resultado[3])
                print("Descripción:", resultado[4])
                print("Jurisdicción:", resultado[5])
                print("palabra clave:", resultado[6])
                print("ID categoria:", resultado[7])
                print("ID organo legislativo:", resultado[8])
                print("----------------------------------------")

    except ValueError as error:
        print("Error:", error)



def modificar_descripcion_normativa():
   try:
        nro_normativa=int(input("Para modificar la descripcion,por favor ingrese el numero de la normativa que desea modificar en la base de datos: "))
        if not nro_normativa:
         raise ValueError("La categoria no puede estar vacía")
    
        resultados = buscar_normativa_numero(nro_normativa)
        if len(resultados) == 0:
           return print("no existe una normativa con ese numero en la base de datos")
        
        
        else:
          for resultado in resultados:
                id_normativa=resultado[0]
         
        nueva_descripcion = input("Ingrese la  nueva descripcion: ")
        if not nueva_descripcion:
         raise ValueError("La descripcion no puede estar vacía")
        elif nueva_descripcion.isdigit():
         raise ValueError("La descripcion debe ser una cadena de texto, no un número")
        else:
          descripcion=modificar_descripcion(id_normativa, nueva_descripcion)
          print(f"El nuevo campo de la descripcion es : {nueva_descripcion}")
          

          
   except ValueError as error:
    print("Error:", error)




def buscar_all_normativas():
   resultados=consultar_normativas()
   print("Resultados:")
   for resultado in resultados:
       print("ID:", resultado[0])
       print("Tipo:", resultado[1])
       print("Número:", resultado[2])
       print("Fecha:", resultado[3])
       print("Descripción:", resultado[4])
       print("Jurisdicción:", resultado[5])
       print("palabra clave:", resultado[6])
       print("ID categoria:", resultado[7])
       print("ID organo legislativo:", resultado[8])
       print("----------------------------------------")
     
     
     


    
    
def insertar_nueva_normativa ():
    
 try:

    normativa1 =Normativas(None,None,None,None,None,None,None,None,None)
    tipo= input("Ingrese el tipo de normativa que desea agregar a la base de datos : ")
    if not tipo:
     raise ValueError("El tipo no puede estar vacío")
    elif tipo.isdigit():
        raise ValueError("El tipo de normativa debe ser una cadena de texto, no un número")
    else:
        normativa1.tipo_normativa=tipo
    numero_normativa=int(input("ingrese el numero de normativa "))
    if not numero_normativa:
         raise ValueError("el numero de normativa no puede estar vacía")
    else:
        resultados = buscar_normativa_numero(numero_normativa)
    normativa1.nro_normativa = numero_normativa
    
    fecha_str = input("Ingrese la fecha en (formato: dd/mm/aaaa): ") 
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
    normativa1.fecha_sancion=fecha
    descripcion =input("por favor, ingrese una descripcion de la normativa ")
    if not tipo:
     raise ValueError("La descripcion puede estar vacío")
    elif tipo.isdigit():
        raise ValueError("La descripcion debe ser una cadena de texto, no un número ")
    else:
        normativa1.descripcion= descripcion
        
    jurisdiccion= input("por favor,indique a que jurisdiccion pertenece la normativa ")
    if not tipo:
     raise ValueError("La jurisdiccion no puede estar vacía")
    elif tipo.isdigit():
        raise ValueError("La jurisdiccion debe ser una cadena de texto, no un número ")
    else:
        normativa1.jurisdiccion= jurisdiccion
    print("esta es la lista de palabras claves existentes en nuestra base de datos,omita seleccionar las que ya se encuentran en esta lista")
    lista_de_palabras_claves()
    palabra_clave=input("por favor,indique una palabra clave que pueda identificar la normativa a futuro ")
    if not tipo:
     raise ValueError("La palabra clave no puede estar vacía")
    elif tipo.isdigit():
        raise ValueError("La palabra clave debe ser una cadena de texto, no un número")
    else:
         normativa1.palabra_clave= palabra_clave
    print("Esta es la lista de categorias disponibles en la base de datos,si la que desea ingresar no esta en la lista,por favor dirigirse a menu principal,y crear una nueva categoria")
    buscar_all_categorias()
    categoria_id=int(input("por favor ingrese el id de la categoria a la que corresponde la normativa a ingresar "))
    if not categoria_id:
        raise ValueError("La categoria no puede estar vacía")
    else:
       normativa1.ID_categoria=categoria_id
            
    print("estos son los organos legislativos en nuestra base")
    buscar_organos()
    id_organo=int(input("ingrese el id del organo legislativo que sanciono la normativa.selecciona el 1 o el 2 segun corresponda "))
    if not tipo:
     raise ValueError("El organo legislativo no puede estar vacío")
    else:
             normativa1.ID_organo_legislativo= id_organo
        
    valor=insertar_Normativas(tipo,numero_normativa,fecha,descripcion,jurisdiccion,palabra_clave,categoria_id,id_organo)
    normativa1.ID_nroRegistro=valor
    
    print(f"felicitaciones,la categoria ya fue insertada con los siguientes datos:  {str(normativa1)}")
    print("¡LA CATEGORIA INGRESADA YA EXISTE EN NUESTRA BASE DE DATOS!")
        
            
 except ValueError as error:
    print("Error:", error)
    
    
    
    
    
def lista_de_palabras_claves():
    
    palabras_clave = listar_palabras()
    for palabra in palabras_clave:
     print(palabra)