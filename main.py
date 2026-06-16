#Trabajo Practico Integrador - Gestion de Paises
#Programacion I
Continentes = ["Africa", "America", "Asia", "Europa", "Oceania"]

def pedir_entero(mensaje):
    """Pide al usuario que ingrese un numero entero mayor a 0."""
    while True: #El ciclo se repetira hasta que el usuario ingrese un numero valido
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("El numero debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un numero valido.")              

def pedir_texto(mensaje):
    """Pide al usuario que ingrese un texto no vacio."""
    while True: #El ciclo se repetira hasta que el usuario ingrese un texto no vacio
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("El campo no puede estar vacio.")

def seleccionar_continente():
    """Muestra una lista de continentes y pide al usuario que seleccione uno."""
    while True:
        print("\nSeleccione un continente:")
        for i, continente in enumerate(Continentes, start=1):
            print(f"{i}. {continente}")

        opcion = input("Opcion: ")
        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(Continentes):
                return Continentes[indice]

        print("Opcion invalida, intente nuevamente.")

def cargar_csv(nombre_archivo):
    paises = []
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        archivo.readline()

        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                datos = linea.split(",")
                if len(datos) == 4:
                    pais = {
                        "nombre": datos[0],
                        "poblacion": int(datos[1]),
                        "superficie": int(datos[2]),
                        "continente": datos[3]
                    }
                    paises.append(pais)
        archivo.close()
    except FileNotFoundError:
        print("Error: No se encontro el archivo CSV.")
    except ValueError:
        print("Error: Datos invalidos en el CSV.")
    return paises

def guardar_csv(nombre_archivo, paises):
    
    try:
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        archivo.write("nombre,poblacion,superficie,continente\n")

        for pais in paises:
            linea = (
                f"{pais['nombre']},"
                f"{pais['poblacion']},"
                f"{pais['superficie']},"
                f"{pais['continente']}\n"
            )
            archivo.write(linea)
        archivo.close()
        print("Datos guardados correctamente.")
    except Exception:
        print("Error al guardar el archivo.")

def pausar():
    input("\nPresione Enter para continuar...")

def diseño_lista():
    """Funcion para mantener el diseño de columnas alineadas"""
    print(f"\n{'Nombre':<18} | {'Población':<12} | {'Superficie':<15} | {'Continente':<12}")
    print("-" * 68)

def diseño_fila(pais):
    """Funcion para mostrar un pais alineado en la tabla"""
    print(f"{pais['nombre']:<18} | {pais['poblacion']:<12} | {pais['superficie']:<11} km² | {pais['continente']:<12}")

def mostrar_paises(paises):
    if len(paises) == 0:
        print("\nNo hay paises registrados.")
        return

    print("\n   Lista de Paises   ")
    diseño_lista()
    for pais in paises:
        diseño_fila(pais)
    
def agregar_pais(paises):
    print("\n   Agregar Pais   ")
    nombre = pedir_texto("Nombre del pais: ").strip().title()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("El pais ya existe.")
            return
    poblacion = pedir_entero("Poblacion: ")
    superficie = pedir_entero("Superficie (km²): ")
    continente = seleccionar_continente()
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    print("Pais agregado correctamente.")

def actualizar_pais(paises):
    print("\n   Actualizar Pais   ")
    nombre = pedir_texto("Ingrese el nombre del pais a actualizar: ").strip().lower()

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            print(f"Actualizando datos de {pais['nombre']}...")
            nueva_poblacion = pedir_entero("Nueva poblacion: ")
            nueva_superficie = pedir_entero("Nueva superficie (km²): ")
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            print("Datos actualizados correctamente.")
            return
    print("No se encontro el pais especificado.")

def buscar_pais(paises):
    print("\n   Buscar Pais   ")
    busqueda = input("Ingrese el nombre del pais: ").strip().lower()

    if busqueda == "":
        print("Debe ingresar un nombre.")
        return

    encontrados = 0
    for pais in paises:
        if busqueda in pais["nombre"].lower():
            if encontrados == 0:
                diseño_lista()
            diseño_fila(pais)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron paises.")
        
def filtrar_paises(paises):
    print("\n   Filtrar Pais   ")
    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        continente = seleccionar_continente()
        encontrados = 0
        for pais in paises:
            if pais["continente"] == continente:
                if encontrados == 0:
                    diseño_lista()
                diseño_fila(pais)
                encontrados += 1
        if encontrados == 0:
            print("No se encontraron paises en ese continente.")

    elif opcion == "2":
        minimo = pedir_entero("Poblacion minima: ")
        maximo = pedir_entero("Poblacion maxima: ")
        encontrados = 0
        for pais in paises:
            if minimo <= pais["poblacion"] <= maximo:
                if encontrados == 0:
                    diseño_lista()
                diseño_fila(pais)
                encontrados += 1
        if encontrados == 0:
            print("No se encontraron paises en ese rango de poblacion.")

    elif opcion == "3":
        minimo = pedir_entero("Superficie minima: ")
        maximo = pedir_entero("Superficie maxima: ")
        encontrados = 0
        for pais in paises:
            if minimo <= pais["superficie"] <= maximo:
                if encontrados == 0:
                    diseño_lista()
                diseño_fila(pais)
                encontrados += 1
        if encontrados == 0:
            print("No se encontraron paises en ese rango de superficie.")
    else:   
        print("Opcion invalida.")

def ordenar_paises(paises):
    print("\n   Ordenar Pais   ")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")

    criterio = input("Seleccione criterio: ")
    orden = input("Ascendente (A) o Descendente (D): ").lower()

    reverso = False
    if orden == "d":
        reverso = True

    if criterio == "1":
        ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower(), reverse=reverso)
    elif criterio == "2":
        ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=reverso)
    elif criterio == "3":
        ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=reverso)
    else:
        print("Opcion invalida.")
        return

    print("\n   Paises Ordenados   ")
    diseño_lista()
    for pais in ordenados:
        diseño_fila(pais)

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay paises registrados.")
        return

    mayor = paises[0]
    menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]
        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n   Estadisticas   ")
    print(f"Pais con mayor poblacion: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Pais con menor poblacion: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de poblacion   : {promedio_poblacion:.2f}")
    print(f"Promedio de superficie  : {promedio_superficie:.2f} km²")

    print("\nCantidad de paises por continente:")
    for continente, cantidad in continentes.items():
        print(f" - {continente:<10}: {cantidad}")

def mostrar_menu():
    print("\n   Menu Principal   ")
    print("1. Mostrar paises")
    print("2. Agregar pais")
    print("3. Actualizar pais")
    print("4. Buscar pais")
    print("5. Filtrar paises")
    print("6. Ordenar paises")
    print("7. Mostrar estadisticas")
    print("8. Guardar cambios")
    print("9. Salir")

#Programa principal
paises = cargar_csv("paises.csv")

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":
        mostrar_paises(paises)
        pausar()
    elif opcion == "2":
        agregar_pais(paises)
        pausar()
    elif opcion == "3":
        actualizar_pais(paises)
        pausar()
    elif opcion == "4":
        buscar_pais(paises)
        pausar()
    elif opcion == "5":
        filtrar_paises(paises)
        pausar()
    elif opcion == "6":
        ordenar_paises(paises)
        pausar()
    elif opcion == "7":
        mostrar_estadisticas(paises)
        pausar()
    elif opcion == "8":
        guardar_csv("paises.csv", paises)
        pausar()
    elif opcion == "9":
        respuesta = input("¿Desea guardar antes de salir? (s/n): ").lower()
        if respuesta == "s":
            guardar_csv("paises.csv", paises)
        print("Programa finalizado.")
        break
    else:
        print("Opcion invalida.")