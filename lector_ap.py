# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#Funcion d eletras griegas
def letras_griegas():
    letras_griegas = [chr(code) for code in range(945,970)]
    print(letras_griegas)

#funcion para abrir archivo
def abrir_archivo(name):
    #determinamos le directorio donde se encuentra el archivo
    directory = "./"
    #abrimos el archivo y el contenido lo cargamos a una variable
    archivo = open(directory+name)
    #resultado de lectura
    #Si se quiere utilizar en mas d eun proceso el contenido debe volverse a abrir el archivo 8incluyendo print)
    #print(imprime.read())
    return (archivo)

def leer_documento(name):
    #determinamos le directorio donde se encuentra el archivo
    directory = "./"
    #abrimos el archivo y el contenido lo cargamos a una variable
    archivo = open(directory+name)
    imprime = open(directory + name)
    #resultado de lectura
    #Si se quiere utilizar en mas d eun proceso el contenido debe volverse a abrir el archivo 8incluyendo print)
    print("-----------------------------------------------")
    print("Contenido del documento '" + name + "'")
    print("-----------------------------------------------")
    print(imprime.read())
    print("----------------END DOC-----------------")


#funcion para abrir archivo y guardar las lineas en una lista
def abrir_archivo_lineas(name):
    #abrimos el archivo y cargamos el contenido a una variable
    archivo = abrir_archivo(name)
    #almacenamos las lineas en lista
    lineas = archivo.readlines()

    #dividir lineas en lista de lineas
    lista_lineas = []
    #limpieza de caracteres especiales por linea
    for linea in lineas:
        linea = linea.split()
        mensaje = linea[0]
        mensaje = mensaje.replace(",","")
        mensaje = mensaje.replace(";", "")
        mensaje = mensaje.replace("(", "")
        mensaje = mensaje.replace(")", "")
        #agrega a una lista los mensajes
        a = list(mensaje)
        lista_lineas.append(a)
    print("")
    #print("---------lista de lineas depuradas-------")
    #print(lista_lineas)
    return (lista_lineas)

def proceso_1(name):
    lineas = abrir_archivo_lineas(name)
    lamb = str(lineas[0][0])
    iota = str(lineas[0][-1])
    regla = []
    print("----------------------------------------")
    print("Paso 1")
    print("S  ->  <" +lamb+ ", "+chr(955)+", " +iota+ ">" )
    regla.extend([ lamb, "L", iota, "\n"])
    #crear el archivo por rimera vez en blanco
    escribir_archivo_linea("gram.cfg","w",["1\n"])

    #escribir el resultado en el archivo
    escribir_archivo_linea("gram.cfg", "a", regla)
    regla.clear()

def proceso_2(name):
    lineas = abrir_archivo_lineas(name)
    regla = []
    print("----------------------------------------")
    print("Paso 2")
    escribir_archivo_linea("gram.cfg", "a", ["2\n"])
    for linea in lineas[0]:
        for letra in linea:
            s_1 = str(letra)
        print("<" +s_1+ ", "+chr(955)+", " +s_1+ ">  ->  "+chr(955) )
        regla.extend([s_1, "L", s_1, "L\n"])
        # escribir el resultado en el archivo
        escribir_archivo_linea("gram.cfg", "a", regla)
        regla.clear()

def proceso_3(name):
    lineas_aceptada = []
    lineas = abrir_archivo_lineas(name)
    regla = []
    print("----------------------------------------")
    print("Paso 3")
    escribir_archivo_linea("gram.cfg", "a", ["3\n"])
    for linea in range(5,len(lineas)):
        #print(lineas[linea][2])
        #while linea > 4:
        if lineas[linea][2] != "L":
            print("cadena valida en la linea numero:" +str(linea))
            a0 = lineas[linea][0]
            a1 = lineas[linea][1]
            a2 = lineas[linea][2]
            a3 = lineas[linea][3]
            a4 = lineas[linea][4]
            print("(" +a0+ ", " +a1+ ", " +a2+ " ; " +a3+ " , " +a4+ " )" )
            lineas_aceptada.append([a0,a1,a2,a3,a4])
    for s in lineas[0]:
        for l in range(0,len(lineas_aceptada)):

            a0 = lineas_aceptada[l][0]
            a1 = lineas_aceptada[l][1]
            a2 = lineas_aceptada[l][2]
            a3 = lineas_aceptada[l][3]
            a4 = lineas_aceptada[l][4]

            print("s = "+s+ "   < "+a0+" , "+a2+" , "+s+ " >  -> "+a1+" < "+a3+ " , " +a4+" , " +s+ " >")
            regla.extend([s, a0, a2, s, a1, a3, a4, s,"\n"])
            escribir_archivo_linea("gram.cfg","a",regla)
            regla.clear()



def proceso_4(name):
    lineas_aceptada = []
    lineas = abrir_archivo_lineas(name)
    sim_pila = []
    regla = []
    unique_list = []
    print("----------------------------------------")
    print("Paso 4")
    escribir_archivo_linea("gram.cfg","a", ["4\n"])
    for linea in range(5,len(lineas)):
        #print(lineas[linea][2])
        #while linea > 4:
        if lineas[linea][2] == "L":
            print("cadena valida en la linea numero:" +str(linea))
            a0 = lineas[linea][0]
            a1 = lineas[linea][1]
            a2 = lineas[linea][2]
            a3 = lineas[linea][3]
            a4 = lineas[linea][4]
            print("(" +a0+ ", " +a1+ ", " +a2+ " ; " +a3+ " , " +a4+ " )" )
            lineas_aceptada.append([a0,a1,a2,a3,a4])
            sim_pila.append(a2)
            sim_pila.append(a4)
    unique_list = list(dict.fromkeys(sim_pila))
    #unique_list = sim_pila
    #print(unique_list)
    for l in range(0, len(lineas_aceptada)):
        print("")
        print("------------------------------")
        print("Linea con la que se trabajara: "+str(lineas_aceptada[l]))
        a0 = lineas_aceptada[l][0]
        a1 = lineas_aceptada[l][1]
        a2 = lineas_aceptada[l][2]
        a3 = lineas_aceptada[l][3]
        a4 = lineas_aceptada[l][4]

        for w in unique_list:
            print("w = "+w)
            for k in lineas[0]:
                print(" k = "+k)
                for r in lineas[0]:
                        print("  r = "+r+ "   <"+a0+", "+a1+", "+r+ ">  -> "+a1+" <"+a3+ ", " +a4+", " +k+ "> <"+k+ ", " +a1+ ", " +r+ ">")
                        regla.extend([a0,a1,r,a1,a3,a4,k,k,a1,r,"\n"])
                        escribir_archivo_linea("gram.cfg","a",regla)
                        regla.clear()
        #print("-----------------------")

#función para escribir un archivo de texto gram.cfg, estado w nuevo archivo, a sobreescribe
def escribir_archivo_linea(name,estado,texto):
    fichero = open(name,estado)
    fichero.writelines(texto)
    fichero.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doc = "simple_3.ap"
    #abrir_archivo_lineas(doc)
    #letras_griegas()
    leer_documento(doc)
    proceso_1(doc)
    proceso_2(doc)
    proceso_3(doc)
    proceso_4(doc)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
