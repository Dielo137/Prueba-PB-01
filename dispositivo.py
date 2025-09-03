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
    
    
    
class Computadora(Dispositivo):
    
    def __init__(self,marca,modelo,precio,ramGB):
        super().__init__(marca,modelo,precio)
        self.ramGB = ramGB

    def descripcion(self):
        return f"Disositivo de marca {self.marca}, modelo {self.modelo}, con {self.ramGB}"
    
class Telefono(Dispositivo):
    
    def __init__(self,marca,modelo,precio,camaraMG):
        super().__init__(marca,modelo,precio)
        self.camaraMG = camaraMG
        
    def descripcion(self):
        return f"Dispositivo de marca {self.marca}, modelo {self.modelo}, con {self.camaraMG}"