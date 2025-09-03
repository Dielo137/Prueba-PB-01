# Creacion de la clase Dispositivo, que tendra los atributos marca, modelo y precio. Tambien con los metodos solicitados.
# Sus metodos son get_precio para obtener el precio cuando se lo solicite main, set_precio para establecer uno y descripcion que sera lo que dice sus atributos.


#En este caso , usamos siempre __init__ que es el indicador de constructor, para darle atributos y parametros a nuestra Clase.
class Dispositivo:

    def __init__ (self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El valor debe ser un numero positivo")
    
    def descripcion(self):
        return f"Dispositivo de marca {self.marca}, modelo {self.modelo}"
    
    
#__precio es una forma de encapsulamiento, para ocultar sus detalles intimos o evitar su acceso sin restricciones.    
    
#Usando la herencia de la clase Dispositivo se crea un hijo (Computadora), que reutiliza el codigo del padre, en este caso Dispositivo 
#Se crea un atributo extra , ramGB para la cantidad de ram de este PC.

class Computadora(Dispositivo):
    
    def __init__(self,marca,modelo,precio,ramGB):
        super().__init__(marca,modelo,precio)
        self.ramGB = ramGB

    def descripcion(self):
        return f"Dispositivo de marca {self.marca}, modelo {self.modelo}, con {self.ramGB} GB de Ram"
    
    
#En el caso de los 3 se puede ver Poliformismo de el metodo descripcion, que se adapta en los  3 hijos
#Se repite el mismo paso, pero en este caso camara en Megapixeles
class Telefono(Dispositivo):
    
    def __init__(self,marca,modelo,precio,camaraMG):
        super().__init__(marca,modelo,precio)
        self.camaraMG = camaraMG
        
    def descripcion(self):
        return f"Dispositivo de marca {self.marca}, modelo {self.modelo}, con {self.camaraMG} Megapixeles"


#Lo mismo que los 2 pasos anteriores, pero ahora se agrega resolucion de la pantalla
class Tablet(Dispositivo):
    
    def __init__(self,marca,modelo,precio,tamañopantalla):
        super().__init__(marca,modelo,precio)
        self.tamañopantalla = tamañopantalla
        
    def descripcion(self):
        return f"Dispositivo de marca {self.marca}, modelo {self.modelo}, con Resolucion {self.tamañopantalla}"