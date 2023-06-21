from funciones_parcial1 import *
import json
import os


lista_elementos_con_marca_nueva = []
lista_insumos_act=[]

while True:
    os.system("cls")  # limpia el terminal de ejecuc
    opcion = mostrar_menu()  # importo el menu desde el archivo menu.py

    if opcion == "1":
        # abro el archivo insumos.csv, lo recorro y convierto en lista de # diccionarios
        with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos = []
            diccionario = {}
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            for elemento in lista_elementos0:
                lista_elementos.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                        "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})

    elif opcion == "2":
        motrar = mostrar_cantidad_por_marca(lista_elementos, "MARCA")
    elif opcion == "3":
        motrar = mostrar_marca_y_precios(lista_elementos, "MARCA")
    elif opcion == "4":
        motrar = mostrar_por_caracteristica(lista_elementos, "CARACTERISTICAS")
    elif opcion == "5":
        motrar = ordenar_listas_dict(lista_elementos, "MARCA", True)
    elif opcion == "6":  # hacer compras
        mostrar = hacer_compras(lista_elementos)

    # Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra "Alimento".
    elif opcion == "7":
        # abro "productos.js" modo escritura
        mostrar = obtener_productos ()

    elif opcion == "8":  # abro el archivo productos.js, lo recorro y convierto en lista de diccionarios
        with open("primer_parcial_labo\productos.json", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos_js = []
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            for elemento in lista_elementos0:
                print(elemento)
                lista_elementos_js.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                           "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})

    elif opcion == "9":  # actualizar precios
        # abro el archivo insumos.csv, lo recorro y convierto en lista de
        # diccionarios y lo guardo en el mismo archivo.
        with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
            lista = []
            lista_elementos0 = []
            lista_elementos = []
            diccionario = {}
            for linea in file:
                lista.append(linea.replace("\n", ""))
            for linea in lista:
                lista_elementos0.append(linea.split(","))
            # hago una funcion nueva con MAP recorriendo "lista_elementos0" y le doy el formato dict con las claves por cada indice de la lista y ademas,
            # directamente paso a float el PRECIO que es con el que vouy a hacer cuentas.
            lista_elementos = list(map(lambda elemento: {"ID": elemento[0], "NOMBRE": elemento[1], "MARCA": elemento[2], "PRECIO": float(
                elemento[3].replace("$", "")), "CARACTERISTICAS": elemento[4]}, lista_elementos0))

        with open("primer_parcial_labo\insumos.csv", "w", encoding="utf-8") as file:
            for elemento in lista_elementos:
                porcentaje = 8.4

                elemento["PRECIO"] = elemento["PRECIO"] + \
                    (elemento["PRECIO"]*porcentaje/100)

                file.write(
                    f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]:.2f}{","}{elemento["CARACTERISTICAS"]}\n')
            print(
                "se realizo incremento del 8.4'%' a los precios. y se guardo en archivo insumos2.csv")

    elif opcion == "10":
        
        with open("primer_parcial_labo\marcas.txt", "r", encoding="utf-8") as file:
            # diccionarios
            
            lista_marcas_nuevas=[]
            diccionario = {}
            for linea in file:
                lista_marcas_nuevas.append((linea.replace("\n","")).lower())
            print("Las marcas disponibles son:\n")
            for marca in lista_marcas_nuevas:
                print(marca)
            print("\n")
        marca_ingresada=input("ingrese una marca de las listadas: ").lower()
        while True:
            if (marca_ingresada.isdigit() or (marca_ingresada not in lista_marcas_nuevas)):
                print("Las marcas disponibles son:\n")
                for marca in lista_marcas_nuevas:
                    print(marca)
                print("\n")
                marca_ingresada=input("ingrese una marca de las listadas: ").lower()
            else:
                break
        print("Marca OK\n")
        lista_id=[]
        for elementos in lista_elementos:
            lista_id.append(elementos["ID"])
        id=input("Ingrese ID del producto: ")
        while (not id.isdigit() or id in lista_id):
            id=input("ID existente, Ingrese ID valido: ")

        nombre=input("Ingrese nombre del producto: ")
        while (not nombre.isalpha()):
            nombre=input("ERROR! Ingrese un nombre de producto correcto: ")
        precio=input("Ingrese precio del producto: $")
        while (not precio.isdigit()):
            precio=input("ERROR! Ingrese un precio de producto correcto: ")
        cont_carac=2
        caracteristicas=input("Ingrese caracteristicas del producto (1 a 3): ")
        while cont_carac < 4:
            cargar_otra=input("desea ingresar otra caracteristica?: (si/no)").lower()
            if cargar_otra == "no":
                break
            else:
                caracteristicas_=input("Ingrese caracteristicas del producto (1 a 3): ")
                caracteristicas+="~"+caracteristicas_
                cont_carac+=1
        
        lista_elementos_con_marca_nueva.append({"ID": id, "NOMBRE": nombre,
                                        "MARCA": marca_ingresada, "PRECIO": "$"+str(precio), "CARACTERISTICAS": caracteristicas})
        print(lista_elementos_con_marca_nueva)
        lista_elementos.append({"ID": id, "NOMBRE": nombre,
                                        "MARCA": marca_ingresada, "PRECIO": "$"+str(precio), "CARACTERISTICAS": caracteristicas})

    elif opcion == "11":

        tipo=input("Ingrese 1 para guardarlo como .csv 2 para guardarlo como .json: ")
        while (tipo != "1" and tipo != "2"):
            tipo=input("Error! Ingrese 1 para .csv 2 para .json: ")
        nombre_archivo = input("Ingrese el nombre del archivo a crear: ")
        while nombre_archivo.isdigit():
            nombre_archivo = input("ERROR!! Ingrese el nombre del archivo correcto: ")
        nombre_archivo = nombre_archivo.replace(" ","_")
        directorio="primer_parcial_labo"

        if tipo == "1":
            nombre_archivo+=".csv"
            ruta=os.path.join(directorio, nombre_archivo)
            with open(ruta, "w", encoding="utf-8") as file:
                for elemento in lista_elementos:
                    file.write(
                        f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')
                if len(lista_elementos_con_marca_nueva) > 1:
                        for elemento in lista_marcas_nuevas:
                            file.write(
                                f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')    
        elif tipo == "2":
            nombre_archivo+=".json"
            ruta=os.path.join(directorio, nombre_archivo)
            with open(ruta, "w", encoding="utf-8") as file:
                for elemento in lista_elementos:
                    file.write(
                        f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')
                if len(lista_elementos_con_marca_nueva) > 1:
                        for elemento in lista_marcas_nuevas:
                            file.write(
                                f'{elemento["ID"]}{","}{elemento["NOMBRE"]}{","}{elemento["MARCA"]}{",$"}{elemento["PRECIO"]}{","}{elemento["CARACTERISTICAS"]}\n')    


    elif opcion == "12":  # salir
        salida = input("Confirma salida?: s/n: ")
        if salida == "s" or "S":
            break
    os.system("pause")  # pausa el sistema para ver los resultados
