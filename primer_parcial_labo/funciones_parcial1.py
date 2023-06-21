import json
import csv

lista=[]
lista_marca=[]

def mostrar_menu(): #Menu del programa
    opcion=""
    print("****************** MENU *****************")
    print("1 - Cargar datos desde archivo") #Esta opción permite cargar el contenido del archivo "Insumos.csv" en una colección
    print("2 - Listar cantidad por marca")
    print("3 - Listar insumos por marca")
    print("4 - Buscar insumo por característica")
    print("5 - Listar insumos ordenados")# ASCENDENTE ante marcas iguales, por precio descendente.
    print("6 - Realizar compras")
    print("7 - Guardar en formato JSON") #Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra Alimento"
    print("8 - Leer desde formato JSON")# y listar insumos"
    print("9 - Actualizar precios")
    print("10 - Agregar un nuevo producto a la lista")
    print("11 - Guardar todos los datos actualizados incluye las altas (.csv o .json)")
    print("12 - Salir del programa")
    print("****************** MENU *****************")
    while True:
        opcion = input("Ingrese una opción para continuar: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 11:
            break
        else:
            print("Error: Ingrese nuevamente una opción válida (1 al 11).")
    return opcion


#Muestra todas las marcas y la cantidad .de insumos correspondientes a cada una
def mostrar_cantidad_por_marca(lista:list, key):
    for elemento in lista:
        lista_marca.append(elemento[key].lower())
    lista_marca_sin_repetir=set(lista_marca)
    print("----------------------------------------------------")
    print(f'{"MARCA".ljust(24)} {"CANTIDAD".ljust(5)}')
    print("----------------------------------------------------")
    for marca in lista_marca_sin_repetir:
        retepiciones=lista_marca.count(marca)
        if retepiciones>1:
            #print(marca, "tiene", retepiciones, "insumos")
            
            print(f'{str(marca).ljust(24)} {str(retepiciones).ljust(5)}')
        else:
            #print(marca, "tiene", retepiciones, "insumo")
            print(f'{str(marca).ljust(24)} {str(retepiciones).ljust(5)}')
            #print(f'{marca:15} {"tiene"} {retepiciones:2} {"insumo."}')
    print("----------------------------------------------------")
#---------------- 3 ----------------------
#PARA CADA MARCA: EL NOMBRE Y PRECIO DE LOS INSUMOS

def mostrar_marca_y_precios(lista:list, key):
    for elemento in lista:
        lista_marca.append(elemento[key].lower())
    lista_marca_sin_repetir=set(lista_marca)
    for marca in lista_marca_sin_repetir:
        print("\n---------",str(marca).upper(),"\n")
        for elemento in lista:
            if marca == elemento[key].lower():
                print("*",elemento["NOMBRE"], elemento["PRECIO"])

#El usuario ingresa una característica (por ejemplo, "Sin Granos") 
#y se listarán todos los insumos que poseen dicha característica

def mostrar_por_caracteristica(lista:list, key):
    caracteristica_ingresada=input("ingrese caracteristica: ")
    #validar ingreso de caracteristica
    validacion=0
    while validacion==0:
        for elemento in lista:
            if str(caracteristica_ingresada).lower() in str(elemento[key]).lower():
                validacion+=1
        if validacion==0:
            caracteristica_ingresada=input("Error! ingrese caracteristica: ")
        else:
            break

    print(caracteristica_ingresada)
    for elemento in lista:
        if str(caracteristica_ingresada).lower() in str(elemento[key]).lower():
            print(elemento)
            

#ordenados por marca de forma ascendente (A-Z) y, ante marcas iguales, por precio descendente.
def ordenar_listas_dict(lista: list, key: str, ascendente=True)->list:
    tamaño_lista = len(lista)
    for i in range(tamaño_lista-1):
        for j in range(i+1, tamaño_lista):
            if (lista[i][key]).isdigit():
                if (ascendente and float(lista[i][key]) > float(lista[j][key])) or (not ascendente and float(lista[i][key]) < float(lista[j][key])):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
            else:
                if (ascendente and lista[i][key] > lista[j][key]) or (not ascendente and lista[i][key] < lista[j][key]):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
    for i in range(tamaño_lista-1):
        for j in range(i+1, tamaño_lista):
            if (lista[i][key]==lista[j][key] and lista[i]["PRECIO"]<lista[j]["PRECIO"]):
                    aux = lista[i] 
                    lista[i] = lista[j]  
                    lista[j] = aux
    for elemento in lista:
        caracteristica=elemento["CARACTERISTICAS"]
        caracteristica = caracteristica.split("~", 1)
        if len(caracteristica) > 1:
            resultado = caracteristica[0]
        else:
            resultado = caracteristica
        print(elemento["ID"], elemento["MARCA"], elemento["PRECIO"], resultado)

#Leer desde formato JSON: Permite mostrar un listado de los insumos guardados en el archivo JSON generado en la opción anterior.
def mostrar_elementos_js(lista:list)->list:
    with open("primer_parcial_labo\productos.json", "r") as file: #abro el archivo productos.js, lo recorro y convierto en lista de diccionarios 
        lista = []
        lista_elementos0 = []
        lista_elementos_js = []
        for linea in file: 
            lista.append(linea.replace("\n", ""))
        for linea in lista:
            lista_elementos0.append(linea.split(","))
        for elemento in lista_elementos0:
            lista_elementos_js.append({"ID": elemento[0], "NOMBRE": elemento[1],
                                "MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})
    print(lista_elementos_js)

#Actualizar precios: Aplica un aumento del 8.4% a todos los productos Los productos actualizados se guardan en el archivo "Insumos.csv".
def actualizar_precios(lista:list, key:str, porcentaje:float)->list:

    for elemento in lista:
        print(f"{'Precio anterior: '}             {elemento[key]}")
        elemento[key]=str(elemento[key]).replace("$","")
        elemento[key]=float(elemento[key])+(float(elemento[key])*porcentaje/100)
        #print(f"{'Precio con aumento del: '} {porcentaje}{'%'} {'$'}{elemento[key]:2f}")


def hacer_compras(lista):
    total = 0
    with open("primer_parcial_labo\compras.txt", "w") as file:
        file.write("                           FACTURA DE COMPRA\n")
        file.write(
            "\nCANTIDAD                   PRODUCTO/MARCA                     SUBTOTAL                    \n")
        file.write("\n")
        while True:
            # dato = input("Ingrese un dato (o escriba 'salir' para terminar): ")
            coincidencia = 0
            marca_ingresada = input("ingrese marca: (o salir)").lower()
            for elemento in lista:
                if (marca_ingresada == str(elemento["MARCA"]).lower()):
                    coincidencia += 1
            while (coincidencia == 0 and marca_ingresada != "salir"):
                marca_ingresada = input(
                    "ERROR: ingrese marca de la lista: (o salir)")
                for elemento in lista:
                    if ((marca_ingresada == str(elemento["MARCA"]).lower()) or marca_ingresada == "salir"):
                        coincidencia += 1
            if marca_ingresada == 'salir':
                file.write(
                    "\n" + "TOTAL A PAGAR                                                $"+str(total))
                file.close
                break
        # declaro la lista donde voy a appendear los id que coincidan con la caracteristica ingresada
            lista_id_caracteristica = []
            for elemento in lista:
                # appendeo los id que coincidan con la caracteristica
                if str(marca_ingresada) in str(elemento["MARCA"]).lower():
                    lista_id_caracteristica.append(elemento["ID"])
                    print(elemento)
            producto_id = input("ingrese numero del producto: ")
        # valido que numero de producto este en la lista id y que no sea alfabetico
            while ((producto_id not in lista_id_caracteristica) or producto_id.isalpha()):
                producto_id = input("Error, ingrese numero del producto: ")

            for elemento in lista:
                if elemento["ID"] == producto_id:
                    precio_producto = elemento["PRECIO"]
                    producto = elemento["NOMBRE"]
                    precio_producto = precio_producto.replace("$", "")
                    precio_producto = float(precio_producto)
                    print("El precio del producto es: $",
                            str(precio_producto))
            cantidad = input("ingrese cantidad: ")
        # valido que la cantidad de productos este entre (0 y 100) y que no sea alfabetico

            # while ((cantidad.isalpha() or cantidad.isalnum()) or (int(cantidad) < 0 or int(cantidad)>100 )):
            while ((cantidad.isalpha()) or (int(cantidad) < 0 or int(cantidad) > 100)):
                cantidad = input(
                    "Error, ingrese una cantidad correcta (1-100): ")

            cantidad = int(cantidad)
            subtotal = precio_producto*cantidad
            total += subtotal
            file.write(str(cantidad) + "                   " + producto +
                        ", " + marca_ingresada + "          " + str(subtotal) + "\n")
    with open("primer_parcial_labo\compras.txt", "r") as file:
        for linea in file.readlines():
            print(linea)

def obtener_productos ():
    with open("primer_parcial_labo\productos.json", "w", encoding="utf-8") as file:
            # copie el insumos.csv a un .json
            # abro "insumos.csv" modo lectura para obtener los insumos
            with open("primer_parcial_labo\insumos.csv", "r", encoding="utf-8") as file:
                lista = []
                lista_elementos0 = []
                lista_elementos_js = []
                diccionario = {}

                for linea in file:
                    linea = linea.lower()
                    # filtrando los que tienen la palabra "alimento"
                    if "alimento" in str(linea).lower():
                        # abro "productos.js" modo "a" para appendearles las lineas
                        with open("primer_parcial_labo\productos.json", "a", encoding="utf-8") as file:
                            file.write(linea)