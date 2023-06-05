from modNodo import Nodo
from modInterfaz import Interfaz
from zope.interface import implementer


@implementer(Interfaz)
class Lista:

    def __init__(self):
        
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):

        self.__actual = self.__comienzo
        
        return self

    def __next__(self):
        
        if self.__actual is None:
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def agregarElemento(self, elemento):
        
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
    def insertarElemento(self, posicion, elemento):
        
        if posicion == 0:
            
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        
        else:
            
            nodo_anterior = None
            nodo_actual = self.__comienzo
            index = 0
            
            while index < posicion and nodo_actual is not None and posicion < self.__tope:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
                nodo = Nodo(elemento)
                nodo.setSiguiente(nodo_actual)
                nodo_anterior.setSiguiente(nodo)
        
        self.__tope += 1

        
    def mostrarElemento(self, posicion):
        
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= posicion and nodo_actual is not None and posicion < self.__tope:
            
            if index == posicion:
                
                band = False
                print(nodo_actual)
            
            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1

    
    def modificarPrecio(self, patente):
        
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= self.__tope and nodo_actual is not None:
            
            if nodo_actual.getDato().getUsado():
                
                if nodo_actual.getDato().getPatente() == patente:
                    
                    print(f"Importe de venta {nodo_actual.getDato().importeVenta()}")
                    nodo_actual.getDato().setPrecio(float(input("Ingrese precio base nuevo:")))
                    print(f"Importe de venta {nodo_actual.getDato().importeVenta()}")
                    band = False
            
            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
        
    
    def masEconomico(self):
        
        menor = self.__comienzo.getDato() # type: ignore
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while index <= self.__tope and nodo_actual is not None:
            
            if menor > nodo_actual.getDato(): 
                
                menor = nodo_actual.getDato()

            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
                
        print(menor.importeVenta())
        print(menor)
        
    
    def mostrarElementos(self):
        
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while index <= self.__tope and nodo_actual is not None:
            
            print(f"modelo:{nodo_actual.getDato().getModelo()} - puertas:{nodo_actual.getDato().getPuertas()} - importe venta:{nodo_actual.getDato().importeVenta()}") 

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.getSiguiente()
            index += 1
    
    def __repr__(self) -> str:
        
        return f"actual:{self.__actual} - comienzo:{self.__comienzo}"
