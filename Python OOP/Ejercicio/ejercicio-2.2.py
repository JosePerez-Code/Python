# Crea una clase Tienda con nombre y productos (lista vacía). Con métodos:

# agregar_producto(nombre, precio) — agrega un producto
# mostrar_productos() — muestra todos los productos con su precio
# producto_mas_caro() — imprime el producto más caro

class Tienda:
    def __init__(self, nombre):

        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre" : nombre, "precio" : precio})
        print(f"producto: {nombre} precio: {precio}")
        print("Agregado \n")
    
    def mostrar_productos(self):
        for i in self.productos:
            print(f"\n{i['nombre']} — ${i['precio']}")

    def producto_mas_caro(self):
        mas_caro = max(self.productos, key=lambda p: p["precio"])
        print("\nMas caro")
        print(f"{mas_caro['nombre']} - ${mas_caro['precio']}")
        
        

ver = Tienda("Colmado")
ver.agregar_producto("Azucar", 40)
ver.agregar_producto("leche", 40)
ver.agregar_producto("pan", 50)
ver.mostrar_productos()
ver.producto_mas_caro()
