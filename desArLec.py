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

    # La variable lineaDescriptor guardará todos los elementos de la linea 1 
    # del descriptor separadas por comas
    lineaDescriptor = lineas[0].split(",")
    nombreRelacion = lineaDescriptor[0] # Nombre de la Relacion
    lineas.pop(0)#Elimina la linea 0 dejando solo la tabla

    atributosIndice = []
    # Va atributo por atributo leyendo inico y fin del atributo
    for i in range(1,len(lineaDescriptor),3):
        nombreAtributo,inicio,fin = lineaDescriptor[i:i+3]
        atributosIndice.append((nombreAtributo,int(inicio)-1,int(fin)))
        #print(nombreAtributo+" I:"+inicio+" F:"+fin)

    # Procesa Entidad
    # Va linea por linea
    listaEmpleados = []
    for linea in lineas:
        nuevoEmpleado = em.empleado("","","","","","","","","","","")
        # Para cada atributo
        for i in range(0,len(atributosIndice)):
            nombreAtributo,inicio, fin = atributosIndice[i]
            if nombreAtributo == "employees_id" :
                nuevoEmpleado.employees_id = linea[inicio:fin].strip()
            elif nombreAtributo == "first_name" :
                nuevoEmpleado.first_name = linea[inicio:fin].strip()
            elif nombreAtributo == "last_name" :
                nuevoEmpleado.last_name = linea[inicio:fin].strip()
            elif nombreAtributo == "email" :
                nuevoEmpleado.email = linea[inicio:fin].strip()
            elif nombreAtributo == "phone_number" :
                nuevoEmpleado.phone_number = linea[inicio:fin].strip()
            elif nombreAtributo == "hire_date" :
                nuevoEmpleado.hire_date = linea[inicio:fin].strip()
            elif nombreAtributo == "job_id" :
                nuevoEmpleado.job_id = linea[inicio:fin].strip()
            elif nombreAtributo == "salary" :
                nuevoEmpleado.salary = linea[inicio:fin].strip()
            elif nombreAtributo == "commission_pct" :
                nuevoEmpleado.commission_pct = linea[inicio:fin].strip()
            elif nombreAtributo == "manager_id" :
                nuevoEmpleado.manager_id = linea[inicio:fin].strip()
            elif nombreAtributo == "department_id" :
                nuevoEmpleado.department_id = linea[inicio:fin].strip()

        listaEmpleados.append(nuevoEmpleado)

    # Cierra el archivo
    archivoDescriptor.close()

    #Retorna La lista de empleados
    return listaEmpleados