
class Compra:
    
    lstCompr = [0]
    def __init__(self, CodProveedor, Num_Pedido, fecha, CodProducto, Cantidad):
        self.__CodCompra = Compra.generateCod()
        self.__CodProveedor = CodProveedor
        self.__Num_Pedido = Num_Pedido
        self.__fecha = fecha
        self.__CodProducto = CodProducto
        self.__Cantidad = Cantidad
        
        
    #GENERAR CODIGO UNICO
    def generateCod():
        Compra.lstCompr[0] += 1
        c = Compra.lstCompr[0]
        return f"COD_00_{c}"
    
    
    #CAMBIAR DATOS
    def set_CodProveedor(self, CodProveedor):
        self.__CodProveedor = CodProveedor
        
    def set_Num_Pedido(self, Num_Pedido):
        self.__Num_Pedido = Num_Pedido
        
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def set_CodProducto(self, CodProducto):
        self.__CodProducto = CodProducto
        
    def set_Cantidad(self, Cantidad):
        self.__Cantidad = Cantidad
        
    
    #OBTENER DATOS
    def get_CodProveedor(self):
        return self.__CodProveedor
        
    def get_Num_Pedido(self):
        return self.__Num_Pedido
        
    def get_fecha(self):
        return self.__fecha
        
    def get_CodProducto(self):
        return self.__CodProducto
        
    def get_Cantidad(self):
        return self.__Cantidad
    
    
    #MOSTRAR DATOS
    def MostrarDetalleCompra(self):
        print(f"Código Compra : {self.__CodCompra}")
        print(f"Código Proveedor : {self.__CodProveedor}")
        print(f"Numero de Pedido : {self.__Num_Pedido}")
        print(f"Fecha : {self.__fecha}")
        print(f"Código Producto : {self.__CodProducto}")
        print(f"Cantidad : {self.__Cantidad}")