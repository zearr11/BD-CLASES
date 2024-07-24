from Clases.Herencias import Datos

class Proveedores(Datos):
    
    lstProv = [0]
    def __init__(self, razon_social, rubro, ruc, direccion, telefono, email):
        super().__init__(telefono, email)
        self.__codProv = Proveedores.generateCod()
        self.__razon_social = razon_social
        self.__RUC = ruc
        self.__direccion = direccion
        self.__rubro = rubro
    
    
    #GENERAR CODIGO UNICO
    def generateCod():
        Proveedores.lstProv[0] += 1
        c = Proveedores.lstProv[0]
        return f"COD_00_{c}"
    
    
    #CAMBIAR DATOS
    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social
        
    def set_RUC(self, ruc):
        self.__RUC = ruc
        
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
    def set_rubro(self, rubro):
        self.__rubro = rubro
        
        
    #OBTENER DATOS
    def get_codProv(self):
        return self.__codProv
        
    def get_razon_social(self):
        return self.__razon_social
    
    def get_RUC(self):
        return self.__RUC
    
    def get_direccion(self):
        return self.__direccion
    
    def get_rubro(self):
        return self.__rubro
    
        
    #MOSTRAR DATOS    
    def MostrarDTProv(self):
        print(f"Codigo Proveedor : {self.__codProv}")
        print(f"Razón Social : {self.__razon_social}")
        print(f"RUC : {self.__RUC}")
        print(f"Rubro : {self.__rubro}")
        print(f"Dirección : {self.__direccion}")
        super().MostrarDTBac()