from dispositivo import Dispositivo,  Computadora, Telefono, Tablet

class Tienda:
    def __init__(self):
        
        self.dispositivos = []

    def agregar_dispositivo(self,Dispositivo):
        
        self.dispositivos.append(Dispositivo)
        print(f" {Dispositivo.marca} {Dispositivo.modelo} agregado al catalogo")

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