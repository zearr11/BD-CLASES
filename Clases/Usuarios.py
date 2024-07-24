from Clases.Herencias import Persona

class Usuarios(Persona):
    
    def __init__(self, nombres, apellidos, tipo_doc, num_doc, telefono, email, nomUser, contrasenia, cargoUser, permisoUser):
        super().__init__(nombres, apellidos, tipo_doc, num_doc, telefono, email)
        self.__nomUser = nomUser
        self.__contrasenia = contrasenia
        self.__cargoUser = cargoUser
        self.__permisoUser = permisoUser
    
    
    #CAMBIAR DATOS
    def set_nomUser(self, nomUser):
        self.__nomUser = nomUser
        
    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
        
    def set_cargoUser(self, cargoUser):
        self.__cargoUser = cargoUser
        
    def set_permisoUser(self, permisoUser):
        self.__permisoUser = permisoUser
        
    
    #OBTENER DATOS
    def get_nomUser(self):
        return self.__nomUser
        
    def get_contrasenia(self):
        return self.__contrasenia
        
    def get_cargoUser(self):
        return self.__cargoUser
        
    def get_permisoUser(self):
        return self.__permisoUser
    
    
    #MOSTRAR DATOS    
    def MostrarDTUser(self):
        super().MostrarDTPersona()
        print(f"Nombre de Usuario : {self.__nomUser}")
        print(f"Contraseña : {self.__contrasenia}")
        print(f"Cargo : {self.__cargoUser}")
        print(f"Permiso : {self.__permisoUser}")
        