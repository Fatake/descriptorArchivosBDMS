try:
    import wx
except ImportError:
    print("Instala la libreria wx\n")
    os.system('pip install -U wxPython')
    try:
        import wx
    except ImportError:
        print("Se tiene que instalar la libreria wxpython\n")
        os._exit(-1)
import os
import VentanaPrincipal as vp

# Importa al descriptor
import desArLec as desc
import empleado as em


###########################################################################
## Main Program
###########################################################################
def main():
    # Obtiene la tabla Empleados del descriptor
    tablaEmpleados = desc.leerDescriptor()

    # Genera Aplicación
    app = wx.App()

    # Genera un el Frame principal y le pasa la tabla de empleados
    ex = vp.GeneradorConsulta(None, tablaEmpleados)

    # Muestra el frame principal
    ex.Show()

    # Pone la aplicacion en loop
    app.MainLoop()
    
if __name__ == '__main__':
    main()
