class Categorias:
    def __init__(self, ID_categoria, categoria):
        self._ID_categoria = ID_categoria
        self._categoria = categoria
    @property
    def ID_categoria(self):
        return self._ID_categoria
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria


    def mostrar_detalle(self):
        print(f"categoria: {self._categoria}")

    def __str__(self):
        return f"Categoria ID: {self._ID_categoria}, Categoria: {self._categoria}"

 


class organosLegislativos :
    def __init__(self, ID_organo_legislativo, organo_legislativo):
        self._ID_organo_legislativo = ID_organo_legislativo
        self._organo_legislativo = organo_legislativo
    
    @property
    def id_organo_legislativo(self):
        return self._ID_organo_legislativo
    
    @property
    def organo_legislativo(self):
        return self._organo_legislativo
    
    @organo_legislativo.setter
    def organo_legislativo(self,organo_legislativo):
        self._organo_legislativo = organo_legislativo



    def mostrar_detalleOrgano(self):
        print (f"organo legislativo: {self._organo_legislativo}")

    def __str__(self):
        return f"OrganosLegislativo ID: {self._ID_organo_legislativo}, OrganoLegislativo: {self._organo_legislativo}"


     
class Normativas:
    def __init__(self,id_nroRegistro,tipo_normativa,nro_normativa,fecha_sancion,descripcion,jurisdiccion,palabra_clave,ID_categoria,ID_organo_legislativo):
       self._id_nroRegistro = id_nroRegistro
       self._tipo_normativa = tipo_normativa
       self._nro_normativa= nro_normativa
       self._fecha_sancion = fecha_sancion
       self._descripcion = descripcion
       self._jurisdiccion = jurisdiccion
       self._palabra_clave = palabra_clave
       self._ID_categoria = ID_categoria
       self._ID_organo_legislativo= ID_organo_legislativo
    
    @property
    def id_nroRegistro(self):
        return self._id_nroRegistro
    
    @property
    def tipo_normativa(self):
        return self._tipo_normativa
    

    @property
    def nro_normativa(self):
        return self._nro_normativa
    
    @property
    def fecha_sancion(self):
        return self._fecha_sancion
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def jurisdiccion(self):
        return self._jurisdiccion
    
    @property
    def palabra_clave(self):
        return self._palabra_clave
    
    @property
    def ID_categoria(self):
        return self._ID_categoria
    
    @property
    def ID_organo_legislativo(self):
        return self._ID_organo_legislativo
    
    
    @tipo_normativa.setter
    def tipo_normativa(self,tipo_normativa):
        self._tipo_normativa = tipo_normativa



    @nro_normativa.setter
    def nro_normativa(self,nro_normativa):
        self._nro_normativa = nro_normativa

    @fecha_sancion.setter
    def fecha_sancion(self,fecha_sancion):
        self._fecha_sancion = fecha_sancion
    
    @descripcion.setter
    def descripcion(self,descripcion):
        self._descripcion = descripcion

    @jurisdiccion.setter
    def jurisdiccion(self,jurisdiccion):
        self._jurisdiccion = jurisdiccion

    
    @palabra_clave.setter
    def palabra_clave(self,palabra_clave):
        self._palabra_clave = palabra_clave


    @ID_categoria.setter
    def ID_Categoria(self,ID_categoria):
        self._ID_categoria= ID_categoria
    
    @ID_organo_legislativo.setter
    def ID_organo_legislativo(self,ID_organo_legislativo):
        self._ID_organo_legislativo = ID_organo_legislativo
        

  
    def __str__(self):
      return f"NroRegistro ID: {self._id_nroRegistro},TipoNormativa:{self._tipo_normativa},nroNormativa: {self._nro_normativa},Fecha Sancion: {self._fecha_sancion} ,Descripcion: {self._descripcion},Jurisdiccion {self._jurisdiccion},Palabra Clave : {self._palabra_clave} ,Categoria ID: {self._ID_categoria}, ID Organo Legislativo: {self._ID_organo_legislativo}"