import os

try:
    import wx
except ImportError:
    print("Instalando la libreria wx...\n")
    os.system('pip install -U wxPython')
    try:
        import wx
    except ImportError:
        print("Se tiene que instalar la libreria wxpython\n")
        os._exit(-1)

#import VentanaPrincipal as p
from VentanaPrincipal import VentanaPrincipal
# Importa al descriptor
#import desArLec as desc
from DescritorArchivo import Descriptor
#import empleado as em

###########################################################################
## Main Program
###########################################################################
def main():
    # Obtiene la tabla Departments del descriptor
    descDepartments = Descriptor("Departments.txt")
    tablaDepartments = descDepartments.leerDescriptor()
    # Obtiene la tabla Employees del descriptor
    descEmployees = Descriptor("Employees.txt")
    tablaEmployees = descEmployees.leerDescriptor()
    # Genera Aplicación
    app = wx.App()

    # Genera un el Frame principal y le pasa la tabla de empleados
    ex = VentanaPrincipal(None,tablaEmployees,tablaDepartments)
    # Muestra el frame principal
    ex.Show()

    # Pone la aplicacion en loop
    app.MainLoop()
    
if __name__ == '__main__':
    main()