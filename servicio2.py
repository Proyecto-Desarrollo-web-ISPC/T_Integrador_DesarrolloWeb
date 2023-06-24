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
     