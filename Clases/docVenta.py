from Clases.Venta import Venta

class GenerarDocVenta(Venta):
    
    def __init__(self, codVendedor, codCliente, codProducto, cantidad, medio_pago, fecha, tipo_comprobante):
        super().__init__(codVendedor, codCliente, codProducto, cantidad, medio_pago, fecha, tipo_comprobante)
        
    