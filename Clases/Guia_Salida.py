from Clases.Herencias import Guias

class Guia_Salida(Guias):
    
    def __init__(self, codRemtent, codDestintr, fecha, partida, llegada):
        super().__init__(codRemtent, codDestintr, fecha, partida, llegada)