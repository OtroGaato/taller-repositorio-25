import products

producto = []
eleccion = 0
def menu():
    print("*"*7,"Bienvenidos al Control de stock 3000","*"*8)
    print("*"*18,"MENU PRINCIPAL","*"*19)
    print("1) Agregar productos")
    print("2) Visualizar productos")
    print("3) Buscador de productos")
    print("4) Eliminar productos")
    print("5) Cerrar programa")
    print("*" *53)
    global eleccion
    eleccion = input("Ingrese su opcion: ").strip()
    if eleccion.isdigit():
        eleccion = int(eleccion)
    else:
        print("Opcion incorrecta, intente nuevamente")
        print("-" *53)
        eleccion = 0
    print("-" *53)
menu()
while True:
    if eleccion <=5:
        match eleccion:
            case 1:
                products.agregar(producto)
                menu()           
            case 2:
                products.mostrar(producto)
                menu()                    
            case 3:
                products.buscar(producto)
                menu()                    
            case 4:
                products.eliminar(producto)
                menu()                 
            case 5:
                print("Gracias, vuelvas prontos")
                print("-" *53)
                break                   
            case _:
                print("Opcion incorrecta, intente nuevamente")
                print("-" *53)
                eleccion = 0
                menu()