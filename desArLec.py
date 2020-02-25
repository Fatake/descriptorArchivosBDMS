import sys
import empleado as em

def leerDescriptor(nombreArchivo = 'Employees.txt'):
    # intenta Abrir el Archivo
    try:
        archivoDescriptor = open(nombreArchivo,"r")
    except:
        sys.exit("Error al abrir el archivo "+nombreArchivo)

    # Lee Archivo
    lineas = archivoDescriptor.readlines()
    # La variable lineaDescriptor guardará todos los elementos de la linea 1, la cual corresponde al descriptor
    lineaDescriptor = lineas[0].split(",")
    lineas.pop(0)#Elimina la linea 0 dejando solo la tabla

    descriptor = []
    atributosIndice = []
    # Va atributo por atributo leyendo inico y fin del atributo
    for i in range(1,len(lineaDescriptor),3):
        nombreAtributo,inicio,fin = lineaDescriptor[i:i+3]
        atributosIndice.append((nombreAtributo,int(inicio)-1,int(fin)))
        descriptor.append(lineaDescriptor[i])

    tabla = []
    tabla.append(descriptor)

    # Procesa Entidad
    # Va linea por linea
    listaEmpleados = []
    for linea in lineas:
        nuevoEmpleado = em.empleado("","","","","","","","","","","")
        # Para cada atributo
        for i in range(0,len(atributosIndice)):
            nombreAtributo,inicio, fin = atributosIndice[i]
            if nombreAtributo == "employees_id" :
                nuevoEmpleado.employees_id = int(linea[inicio:fin].strip())
            elif nombreAtributo == "first_name" :
                nuevoEmpleado.first_name = linea[inicio:fin].strip()
            elif nombreAtributo == "last_name" :
                nuevoEmpleado.last_name = linea[inicio:fin].strip()
            elif nombreAtributo == "email" :
                nuevoEmpleado.email = linea[inicio:fin].strip()
            elif nombreAtributo == "phone_number" :
                nuevoEmpleado.phone_number = linea[inicio:fin].strip()
            elif nombreAtributo == "hire_date" :
                txt = linea[inicio:fin].strip()
                nuevoEmpleado.hire_date = txt[0:2] + "/" + txt[2:4] + "/" + txt[4:6]
            elif nombreAtributo == "job_id" :
                nuevoEmpleado.job_id = linea[inicio:fin].strip()
            elif nombreAtributo == "salary" :
                nuevoEmpleado.salary = int(linea[inicio:fin].strip())
            elif nombreAtributo == "commission_pct" :
                if linea[inicio:fin].strip() == "nul":
                    nuevoEmpleado.commission_pct = 0
                else:
                    nuevoEmpleado.commission_pct = float(linea[inicio:fin].strip())
            elif nombreAtributo == "manager_id" :
                if linea[inicio:fin].strip() == "null":
                    nuevoEmpleado.manager_id = " "
                else:
                    nuevoEmpleado.manager_id = int(linea[inicio:fin].strip())
            elif nombreAtributo == "department_id" :
                if linea[inicio:fin].strip() == "null":
                    nuevoEmpleado.department_id = " "
                else:
                    nuevoEmpleado.department_id = int(linea[inicio:fin].strip())

        tabla.append(nuevoEmpleado)

    # Cierra el archivo
    archivoDescriptor.close()

    #Retorna La lista de empleados
    return tabla