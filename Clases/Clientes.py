from Clases.Herencias import Persona


class Clientes(Persona):
    
    def __init__(self, nombres, apellidos, tipo_doc, num_doc, telefono, email, direccion):
        super().__init__(nombres, apellidos, tipo_doc, num_doc, telefono, email)
        self.__direccion = direccion
        
        
    #CAMBIAR DIRECCION
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
        
    #OBTENER DATOS
    def get_direccion(self):
        return self.__direccion
        
        
    #MOSTRAR DATOS        
    def MostrarDTCliente(self):
        super().MostrarDTPersona()
        print(f"Dirección : {self.__direccion}")
    