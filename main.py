#Se importa del archivo tienda  y dispositivo sus propias Clases
from tienda import Tienda

from dispositivo import Dispositivo,  Computadora, Telefono, Tablet


#Si __name__ no es "__main__" entonces el archivo no abrira, como buen metodo de seguridad.
if __name__ == "__main__":

    print(" Iniciando sistema de la Tienda...")


    mi_Tienda = Tienda()

    print(" Creando e instanciando Dispositivos...")
    
# Al hacer esto estamos agregando las instancias o valores, utilizando el codigo anterior, por eso todo va en orden, de izquierda a derecha.
#El archivo main simplemente, atravez del import esta utilizando este codigo, que era como un canvas vacio

    computadora1 = Computadora("HP", "Notebook", 350000, 4)
    telefono1 = Telefono("Samsung", "Galaxy 7", 70000, "500")
    tablet1 = Tablet("Huaweii", "Marca generica", 285000, "1240x1090")
    computadora2 = Computadora("HP", "All in one", 450000, 16)


    print("Agregando Dispositivos al catálogo...")
    
# Aca simplemente se esta agregandon al catalogo, atravez de los metodos que fueron creados en tienda.py
    
    mi_Tienda.agregar_dispositivo(computadora1)
    mi_Tienda.agregar_dispositivo(telefono1)
    mi_Tienda.agregar_dispositivo(tablet1)
    mi_Tienda.agregar_dispositivo(computadora2)

#Con esto se muestra el catalogo
    mi_Tienda.mostrar_catalogo()


#Con esto de aca abajo estamos haciendo la prueba de setter, tambien para verificar si nos deja o no nos deja agregar valores negativos a los productos, que seria mala practica
#Tambien establecemos el precio final que aparecera en consola

    print("Probando el encapsulamiento (setter)...")
    print(f"Precio original del Computador: ${computadora2.get_precio()}")
    

    print("Intentando poner precio -500...")
    computadora2.set_precio(-500) 
    

    print("Cambiando precio a 600000...")
    computadora2.set_precio(600000)
    print(f"Nuevo precio del Tesla: ${computadora2.get_precio()}")


    mi_Tienda.mostrar_catalogo()

    print("\n Sistema finalizado.")