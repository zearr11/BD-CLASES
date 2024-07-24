
class Venta:
    
    lstVent = [0]
    def __init__(self, codVendedor, codCliente, codProducto, cantidad, medio_pago, fecha, tipo_comprobante):
         self.__codVenta = Venta.generateCod()
         self.__codVendedor = codVendedor
         self.__codCliente = codCliente
         self.__codProducto = codProducto
         self.__cantidad = cantidad
         self.__medio_pago = medio_pago
         self.__fecha = fecha
         self.__tipo_comprobante = tipo_comprobante
         
    #GENERAR CODIGO UNICO
    def generateCod():
        Venta.lstVent[0] += 1
        c = Venta.lstVent[0]
        return f"COD_00_{c}"
    
    
    #CAMBIAR DATOS
    def set_codVendedor(self, codVendedor):
        self.__codVendedor = codVendedor
        
    def set_codCliente(self, codCliente):
        self.__codCliente = codCliente
        
    def set_codProducto(self, codProducto):
        self.__codProducto = codProducto
        
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
        
    def set_medio_pago(self, medio_pago):
        self.__medio_pago = medio_pago
        
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def set_tipo_comprobante(self, tipo_comprobante):
        self.__tipo_comprobante = tipo_comprobante
        
        
        
    #OBTENER DATOS
    def get_codVenta(self):
        return self.__codVenta
    
    def get_codVendedor(self):
        return self.__codVendedor
        
    def get_codCliente(self):
        return self.__codCliente
        
    def get_codProducto(self):
        return self.__codProducto
        
    def get_cantidad(self):
        return self.__cantidad
        
    def get_medio_pago(self):
        return self.__medio_pago
        
    def get_fecha(self):
        return self.__fecha
        
    def get_tipo_comprobante(self):
        return self.__tipo_comprobante
        
    
    
    #MOSTRAR DATOS
    def MostrarDetallesVenta(self):
        print(f"Código Venta : {self.__codVenta}")
        print(f"Código Vendedor : {self.__codVendedor}")
        print(f"Código Cliente : {self.__codCliente}")
        print(f"Código Producto : {self.__codProducto}")
        print(f"Cantidad : {self.__cantidad}")
        print(f"Medio de Pago : {self.__medio_pago}")
        print(f"Fecha : {self.__fecha}")
        print(f"Tipo Comprobante : {self.__tipo_comprobante}")