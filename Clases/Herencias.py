
#1
class Datos:
    
    def __init__(self, telefono, email):
        self.__telefonoPer = telefono
        self.__emailPer = email
        
    
    #CAMBIAR DATOS 
    def set_telefono(self, telefono):
        self.__telefonoPer = telefono
        
    def set_email(self, email):
        self.__emailPer = email
        
        
    #OBTENER DATOS
    def get_telefono(self):
        return self.__telefonoPer
    
    def get_email(self):
        return self.__emailPer
        
        
    #MOSTRAR DATOS
    def MostrarDTBac(self):
        print(f"Teléfono : {self.__telefonoPer}")
        print(f"Email : {self.__emailPer}")



#2
class Persona (Datos):
    
    lst = [0]
    def __init__(self, nombres, apellidos, tipo_doc, num_doc, telefono, email):
        super().__init__(telefono, email)
        self.__codPer = Persona.generateCod()
        self.__nombresPer = nombres
        self.__apellidosPer = apellidos
        self.__tipo_docPer = tipo_doc
        self.__num_docPer = num_doc
        
    #GENERAR CODIGO UNICO
    def generateCod():
        Persona.lst[0] += 1
        c = Persona.lst[0]
        return f"COD_00_{c}"
    
    
    #CAMBIAR DATOS:
    def set_nombres(self, nombres):
        self.__nombresPer = nombres
        
    def set_apellidos(self, apellidos):
        self.__apellidosPer = apellidos
        
    def set_tipo_doc(self, tipo_doc):
        self.__tipo_docPer = tipo_doc
        
    def set_num_doc(self, num_doc):
        self.__num_docPer = num_doc
        
        
    #OBTENER DATOS
    def get_codPer(self):
        return self.__codPer
    
    def get_nombres(self):
        return self.__nombresPer
        
    def get_apellidos(self):
        return self.__apellidosPer
        
    def get_tipo_doc(self):
        return self.__tipo_docPer
        
    def get_num_doc(self):
        return self.__num_docPer


    #MOSTRAR DATOS
    def MostrarDTPersona(self):
        print(f"Código : {self.__codPer}")
        print(f"Nombres : {self.__nombresPer}")
        print(f"Apellidos : {self.__apellidosPer}")
        print(f"Tipo de Documento : {self.__tipo_docPer}")
        print(f"Numero de Documento : {self.__num_docPer}")
        super().MostrarDTBac()
        
        
        
#3
class Guias:
    
    lstGUI = [0]
    def __init__(self, codRemtent, codDestintr, fecha, partida, llegada):
        self.__codGuia = Guias.generateCod()
        self.__codRemitente = codRemtent
        self.__codDestinatario = codDestintr
        self.__fecha = fecha
        self.__partida = partida
        self.__llegada = llegada
        
        
    #GENERAR CODIGO UNICO
    def generateCod():
        Guias.lstGUI[0] += 1
        c = Guias.lstGUI[0]
        return f"COD_00_{c}"
    
    
    #CAMBIAR DATOS
    def set_codRemitente(self, codRemtent):
        self.__codRemitente = codRemtent
        
    def set_codDestinatario(self, codDestintr):
        self.__codDestinatario = codDestintr
        
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def set_partida(self, partida):
        self.__partida = partida
        
    def set_llegada(self, llegada):
        self.__llegada = llegada
    

    #OBTENER DATOS
    def get_codGuia(self):
        return self.__codGuia
    
    def get_codRemitente(self):
        return self.__codRemitente
        
    def get_codDestinatario(self):
        return self.__codDestinatario
        
    def get_fecha(self):
        return self.__fecha
        
    def get_partida(self):
        return self.__partida
        
    def get_llegada(self):
        return self.__llegada
    
    
    #MOSTRAR DATOS
    def MostrarDatosGuia(self):
        print(f"Código de Guía : {self.__codGuia}")
        print(f"Código Remitente : {self.__codRemitente}")
        print(f"Código Destinatario : {self.__codDestinatario}")
        print(f"Fecha : {self.__fecha}")
        print(f"Partida : {self.__partida}")
        print(f"Llegada : {self.__llegada}")