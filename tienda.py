#Se importa del archivo dispositivo las clases Dispositivo con sus hijos Computadora, Telefono, Tablet
from dispositivo import Dispositivo,  Computadora, Telefono, Tablet



#La clase tienda contiene una lista vacia, que es self.dispositivos[] sera utilizada de inmediato.
#Se crea el metodo agregar dispositivo, que re utiliza el codigo(Herencia) de Dispositivo, refiriendose a este directamente, entonces al usar .append se adhiere a la Clase de este archivo, gracias a su import
#Basicamente lo que hace, es que main utilizara este codigo para poder agregar valores o nuevos campos al ser solicitado, son solo "acciones"
class Tienda:
    def __init__(self):
        
        self.dispositivos = []

    def agregar_dispositivo(self,Dispositivo):
        
        self.dispositivos.append(Dispositivo)
        print(f" {Dispositivo.marca} {Dispositivo.modelo} agregado al catalogo")


#Muestra el catalogo,  con un inventario vacio
#ya que es for a in self.dispositivos, este pasa por toda la lista de este, junto a su precio
#Y al final total_inventario obtiene el valor final del inventario al sumar todos sus valores
    def mostrar_catalogo(self):

            print("---  Catálogo de la Concesionaria  ---")
            
            if not self.dispositivos:
                print("El catálogo está vacio. Añade algunos vehiculos")
                return 

            total_inventario = 0

            for a in self.dispositivos:

                print(f"- {a.descripcion()} | Precio: ${a.get_precio()}")
                

                total_inventario += a.get_precio()

            print("------------------------------------------")

            print(f" Valor total del inventario: ${total_inventario}")