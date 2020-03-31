import sys
from Entidades import Employee, Department
#import empleado as em

class Descriptor():
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.tabla = []

    def leerDescriptor(self):
        # intenta Abrir el Archivo
        try:
            archivoDescriptor = open(self.nombreArchivo,"r")
        except:
            sys.exit("Error al abrir el archivo "+self.nombreArchivo)
        # Lee Archivo
        lineas = archivoDescriptor.readlines()
        # La variable lineaDescriptor guardará todos los elementos de la linea 1, la cual corresponde al descriptor de archivo
        lineaDescriptor = lineas[0].split(",")
        #Elimina la linea 0 dejando solo la tabla
        lineas.pop(0)
        atributos = []
        atributosIndice = []
        # Va atributo por atributo leyendo inico y fin del atributo
        for i in range(1,len(lineaDescriptor),3):
            nombreAtributo,inicio,fin = lineaDescriptor[i:i+3]
            atributosIndice.append((nombreAtributo,int(inicio)-1,int(fin)))
            atributos.append(lineaDescriptor[i])
        self.tabla.append(atributos)
        if len(atributos)==11:
            self.cargarEmployees(lineas,atributosIndice)
        elif len(atributos)==4:
            self.cargarDepartments(lineas,atributosIndice)
        # Cierra el archivo
        archivoDescriptor.close()
        return self.tabla
        

    def cargarEmployees(self, lineas, atributosIndice):
        # Procesa Entidad Employees leyendo el resto del archivo línea por línea
        for linea in lineas:
            nuevoEmpleado = Employee("","","","","","","","","","","")
            # Para cada atributo
            for i in range(0,len(atributosIndice)):
                atributo,inicio,fin = atributosIndice[i]
                if atributo == "employee_id" :
                    nuevoEmpleado.employees_id = int(linea[inicio:fin].strip())
                elif atributo == "first_name" :
                    nuevoEmpleado.first_name = linea[inicio:fin].strip()
                elif atributo == "last_name" :
                    nuevoEmpleado.last_name = linea[inicio:fin].strip()
                elif atributo == "email" :
                    nuevoEmpleado.email = linea[inicio:fin].strip()
                elif atributo == "phone_number" :
                    nuevoEmpleado.phone_number = linea[inicio:fin].strip()
                elif atributo == "hire_date" :
                    txt = linea[inicio:fin].strip()
                    nuevoEmpleado.hire_date = txt[0:2] + "/" + txt[2:4] + "/" + txt[4:6]
                elif atributo == "job_id" :
                    nuevoEmpleado.job_id = linea[inicio:fin].strip()
                elif atributo == "salary" :
                    nuevoEmpleado.salary = int(linea[inicio:fin].strip())
                elif atributo == "commission_pct" :
                    if linea[inicio:fin].strip() == "nul":
                        nuevoEmpleado.commission_pct = "null"#0
                    else:
                        nuevoEmpleado.commission_pct = float(linea[inicio:fin].strip())
                elif atributo == "manager_id" :
                    if linea[inicio:fin].strip() == "null":
                        nuevoEmpleado.manager_id = "null"
                    else:
                        nuevoEmpleado.manager_id = int(linea[inicio:fin].strip())
                elif atributo == "department_id" :
                    if linea[inicio:fin].strip() == "null":
                        nuevoEmpleado.department_id = "null"
                    else:
                        nuevoEmpleado.department_id = int(linea[inicio:fin].strip())
            self.tabla.append(nuevoEmpleado)


    def cargarDepartments(self, lineas, atributosIndice):
        # Procesa Entidad Employees leyendo el resto del archivo línea por línea
        for linea in lineas:
            nuevoDepartamento = Department("","","","")
            # Para cada atributo
            for i in range(0,len(atributosIndice)):
                atributo,inicio,fin = atributosIndice[i]
                if atributo == "department_id" :
                    nuevoDepartamento.department_id = int(linea[inicio:fin].strip())
                elif atributo == "department_name" :
                    nuevoDepartamento.department_name = linea[inicio:fin].strip()
                elif atributo == "manager_id" :
                    if linea[inicio:fin].strip() == "null":
                        nuevoDepartamento.manager_id = "null"
                    else:
                        nuevoDepartamento.manager_id = int(linea[inicio:fin].strip())
                elif atributo == "location_id" :
                    nuevoDepartamento.location_id = int(linea[inicio:fin].strip())
            self.tabla.append(nuevoDepartamento)