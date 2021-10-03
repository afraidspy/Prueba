# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 04:40:06 2021

@author: guest
"""
import math
from abc import ABC, abstractmethod

class Poligono(ABC): 
    
    def __init__(self, lados):
        self._lados = lados
        self._num_lados = len(self._lados)
        print('Numero de lados',self._num_lados)
    
    def calcular_perimetro(self):
       sum = 0
       for valor in self._lados:
           print("Valor: ", valor)
           sum += valor
       print("Suma", sum)
       return sum
   
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        estado=""
        for valor in self._lados:
            estado+= "Lado: " + str(valor)
        return estado
            
        

class Triangulo(Poligono):
    
    def __init__(self, lados):
        super().__init__(lados);
        
        
    def calcular_semiperimetro(self):
        s = 0
        for valor in self._lados:
            s+=valor
        return s
    
    def area(self):
        print("Area",math.sqrt(2))
        return math.sqrt(2)
    
    def __str__(self):
        return "Triangulo: " + super().__str__()
    
        
        
        
        

poligono = Triangulo([1,2.3])

poligono.calcular_perimetro()
poligono.area()

print(poligono)



    