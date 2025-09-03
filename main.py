from tienda import Tienda

from dispositivo import Dispositivo,  Computadora, Telefono, Tablet



if __name__ == "__main__":

    print(" Iniciando sistema de la Tienda...")


    mi_Tienda = Tienda()

    print(" Creando e instanciando Dispositivos...")

    computadora1 = Computadora("HP", "Notebook", 350000, 4)
    telefono1 = Telefono("Samsung", "Galaxy 7", 70000, "500")
    tablet1 = Tablet("Huaweii", "Marca generica", 285000, "1240x1090")
    computadora2 = Computadora("HP", "All in one", 450000, 16)


    print("Agregando Dispositivos al catálogo...")
    
    mi_Tienda.agregar_dispositivo(computadora1)
    mi_Tienda.agregar_dispositivo(telefono1)
    mi_Tienda.agregar_dispositivo(tablet1)
    mi_Tienda.agregar_dispositivo(computadora2)


    mi_Tienda.mostrar_catalogo()


    print("Probando el encapsulamiento (setter)...")
    print(f"Precio original del Computador: ${computadora2.get_precio()}")
    

    print("Intentando poner precio -500...")
    computadora2.set_precio(-500) 
    

    print("Cambiando precio a 600000...")
    computadora2.set_precio(600000)
    print(f"Nuevo precio del Tesla: ${computadora2.get_precio()}")


    mi_Tienda.mostrar_catalogo()

    print("\n Sistema finalizado.")