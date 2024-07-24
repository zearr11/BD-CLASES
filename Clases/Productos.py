
class Productos:
    
    lstP = [0]
    def __init__(self, desc_prod, stock_min, stock_max, categoria, marca, estadoProducto, medida, precio):
        self.__codProd = Productos.generateCod()
        self.__desc_prod = desc_prod
        self.__stock_min = stock_min
        self.__stock_max = stock_max
        self.__categoria = categoria
        self.__marca = marca
        self.__estadoProduc = estadoProducto
        self.__medida = medida
        self.__precio = precio
        
        
    #GENERAR CODIGO UNICO
    def generateCod():
        Productos.lstP[0] += 1
        c = Productos.lstP[0]
        return f"COD_00_{c}"
    
    
    #CAMBIAR DATOS
    def set_desc_prod(self, desc_prod):
        self.__desc_prod = desc_prod
        
    def set_stock_min(self, stock_min):
        self.__stock_min = stock_min
        
    def set_stock_max(self, stock_max):
        self.__stock_max = stock_max
        
    def set_categoria(self, categoria):
        self.__categoria = categoria
        
    def set_marca(self, marca):   
        self.__marca = marca
        
    def set_estadoProducto(self, estadoProducto):  
        self.__estadoProduc = estadoProducto
        
    def set_medida(self, medida):
        self.__medida = medida
        
    def set_precio(self, precio):  
        self.__precio = precio
        
        
    #OBTENER DATOS
    def get_codProd(self):
        return self.__codProd
    
    def get_desc_prod(self):
        return self.__desc_prod
        
    def get_stock_min(self):
        return self.__stock_min
        
    def get_stock_max(self):
        return self.__stock_max
        
    def get_categoria(self):
        return self.__categoria
        
    def get_marca(self):   
        return self.__marca
        
    def get_estadoProducto(self):  
        return self.__estadoProduc
        
    def get_medida(self):
        return self.__medida
        
    def get_precio(self):  
        return self.__precio
    
    
    #MOSTRAR DATOS
    def MostrarDTProd(self):
        print(f"Código Producto: {self.__codProd}")
        print(f"Descripción Producto : {self.__desc_prod}")
        print(f"Stock Mínimo : {self.__stock_min}")
        print(f"Stock Máximo : {self.__stock_max}")
        print(f"Categoría : {self.__categoria}")
        print(f"Marca : {self.__marca}")
        print(f"Estado del Producto : {self.__estadoProduc}")
        print(f"Medida : {self.__medida}")
        print(f"Precio : {self.__precio}")