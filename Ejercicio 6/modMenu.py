from modLista import Lista
from modVehiculo import Vehiculo
import json


class Menu:
    
    def menu(self):
        
        lista = Lista()
        
        print("1 - Insertar un vehículo en la colección en una posición determinada")
        print("2 - Agregar un vehículo a la colección")
        print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado")
        print("4 - Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta")
        print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
        print("6 - Mostrar para todos los vehículos")
        print("7 - Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”")
        print("8 - Salir")
        
        op = input("Ingrese opción:")
        
        while(op != "8"):
            
            if op == "1":
                
                lista.insertarElemento(1,Vehiculo(False,"Fiat","Uno",2,"verde",25000,"full"))
                
            elif op == "2":
                
                auto1 = Vehiculo(False,"Ford","Focus",4,"Rojo",25000,"full")
                auto2 = Vehiculo(True,"Chevrolet","Cruze",4,"Azul",15000,"","ABC123",2017,50000)
                lista.agregarElemento(auto1)
                lista.agregarElemento(auto2)
            
            elif op == "3":
                
                lista.mostrarElemento(2)
                
            elif op == "4":
            
                lista.modificarPrecio(input("Ingrese patente:"))
            
            elif op == "5":
                
                lista.masEconomico()
            
            elif op == "6":
                
                lista.mostrarElementos()
            
            elif op == "7":
                
                datos = []
                
                for vehiculo in lista:
                    
                    datos.append({
                    
                    "usado": vehiculo.getUsado(),
                    "marca": vehiculo.getMarca(),
                    "modelo": vehiculo.getModelo(),
                    "puertas": vehiculo.getPuertas(),
                    "color": vehiculo.getColor(),
                    "precio": vehiculo.getPrecio(),
                    "version": vehiculo.getVersion(),
                    "patente": vehiculo.getPatente(),
                    "anio": vehiculo.getAnio(),
                    "kilometraje": vehiculo.getKilometraje()
                    
                    })
                
                with open("vehiculos.json", "w") as archivo:
                    
                    json.dump(datos, archivo)

            
            print("1 - Insertar un vehículo en la colección en una posición determinada")
            print("2 - Agregar un vehículo a la colección")
            print("3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado")
            print("4 - Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta")
            print("5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico")
            print("6 - Mostrar para todos los vehículos")
            print("7 - Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”")
            print("8 - Salir")
            
            op = input("Ingrese opción:")