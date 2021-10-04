# -*- coding: utf-8 -*-
"""
Clase Bombilla que permite representar
focos que están encedidos o apagados
usando POO
@author: Jessica San

"""

class Bombilla:
    
    def __init__(self,estado=True):
        self.__estado = estado
        
    def setEstado(self, estado):
        self.__estado =  estado
    
    def getEstado(self):
        return self.__estado
    
    def imprimir_estado(self):
        if(self.__estado):
            print("on")
        else:
            print("off")
        
        
    
    

estaEncendida=bool(input("La bombilla está encendida: "))

print("Tipo de dato: ",type(estaEncendida))

print(estaEncendida)
bombilla=Bombilla()
print(bombilla.getEstado())
bombilla.imprimir_estado()
bombilla.setEstado(False)
bombilla.imprimir_estado()


bombilla=Bombilla(False);
bombilla.imprimir_estado()
