from Clases.Clientes import Clientes #1
from Clases.Compra import Compra #2
from Clases.docVenta import GenerarDocVenta #3
from Clases.Guia_Entrada import Guia_Entrada #4
from Clases.Guia_Salida import Guia_Salida #5
from Clases.Productos import Productos #6
from Clases.Proveedores import Proveedores #7
from Clases.Usuarios import Usuarios #8
from Clases.Venta import Venta #9
#Herencias #10

#CLIENTES
objCliente = Clientes("Eduardo Antonio", "Perez Aguilar", "DNI", "09167212",
                      900231711, "eduaguil03@hotmail.com", "Calle Las Palmeras 2531")

objCliente.MostrarDTCliente()
print()


#COMPRA
objCompra = Compra("COD_00_23", "COD_00_732","19/07/2020","COD_00_04",50)
objCompra.MostrarDetalleCompra()
print()


#GENERAR DOCUMENTO VENTA
objGenerarDoc = GenerarDocVenta("COD_00_72","COD_00_123","COD_00_98",5,"Efectivo","20/02/2024","Boleta")
objGenerarDoc.MostrarDetallesVenta()
print()


#Guia Entrada
objEntrada = Guia_Entrada("COD_00_923","COD_00_810","28/03/2023","01/04/2023","05/04/2023")
objEntrada.MostrarDatosGuia()
print()


#Guia Salida
objSalida = Guia_Salida("COD_00_102","COD_00_321","19/02/2024","21/02/2024","24/02/2024")
objSalida.MostrarDatosGuia()
print()


#PRODUCTOS
objProducto = Productos("Gaseosa 1lt", 25, 100, "Bebidas", "Inka Kola", "Disponible", "Unidad", f"S/{4}")
objProducto.MostrarDTProd()
print()


#PROVEEDORES
objProveedor = Proveedores("Leche Gloria S.A", "Lacteos y Embutidos", 20100190797, 
                           "Av. Paseo de la República N° 2357", 942022564, "contactcenterinforma@gloria.com.pe")
objProveedor.MostrarDTProv()
print()


#USUARIOS
objUsuario = Usuarios("Jorge Antonio", "Baltazar Campos", "DNI", 85096714, 902761811, 
                      "jorgcampo11@gmail.com", "JorCamp03", 123456, "Vendedor", "Usuario Estandar")
objUsuario.MostrarDTUser()
print()


#VENTA
objVenta = Venta("COD_00_23","COD_00_91","COD_00_103",3,"Pago Online","21/05/2023","Boleta")
objVenta.MostrarDetallesVenta()
print()