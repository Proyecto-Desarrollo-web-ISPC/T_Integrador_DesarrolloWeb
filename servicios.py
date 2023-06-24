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
   