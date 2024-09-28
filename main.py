import os
def mostrar_menu():
    os.system('clear' if os.name != 'nt' else 'cls')  # Limpia la consola
    print("\n" + "="*40)
    print("         ** Menú Principal **                ")
    print("="*40)
    print("         [1] control de ventas               ")
    print("="*40)

def main():
    while True:
            os.system('clear' if os.name != 'nt' else 'cls')  # Limpiar la consola después de ingresar
            mostrar_menu()
            # Solicitar al usuario que seleccione una opción
            opcion = input(">>> Seleccione una opción:? ")

            # Opciones del menú
            if opcion == "SI" or opcion == "si" or opcion == "Si":
                # Opción para registrar un grupo
                pass
            elif opcion == "NO" or opcion == "no" or opcion == "No":
                print("\n\nGracias por usar el software.\n")
                break  # Termina el bucle y cierra el programa
            else:
                # Mensaje de error si la opción no es válida
                print(">>> ❌ Error. debe ingresar (SI/NO).")  # Mensaje de error si la contraseña es incorrecta
                input("Presione enter para intentar de nuevo...")  # Esperar entrada del usuario
                pass

# Ejecutar la función main si este archivo es el programa principal 
if __name__ == "__main__":
    main()