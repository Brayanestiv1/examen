import json
def mostrar_menu():
    print('\033c')  # Limpia la consola
    print("\n" + "="*40)
    print("         ** CONTROL DE VENTAS **                ")
    print("="*40)
    print("         [1] Informe de ventas               ")
    print("="*40)

productos = []
clientes = []
ventas = []

def productos():
    try:
        with open("archivos/productos.json", "r") as fd:
            productos = json.load(fd)
    except (FileNotFoundError, json.JSONDecodeError):
        productos = []

    if not productos:
        print(">>> ❌ No hay productos registrados.")
        input("Presione Enter para continuar...")
        return
def clientes():
    try:
        with open("archivos/clientes.json", "r") as fd:
            clientes = json.load(fd)
    except (FileNotFoundError, json.JSONDecodeError):
        clientes = []

    if not clientes:
        print(">>> ❌ No hay clientes registrados.")
        input("Presione Enter para continuar...")
        return
def ventas():
    try:
        with open("archivos/ventas.json", "r") as fd:
            ventas = json.load(fd)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = []

    if not ventas:
        print(">>> ❌ No hay productos registrados.")
        input("Presione Enter para continuar...")
        return