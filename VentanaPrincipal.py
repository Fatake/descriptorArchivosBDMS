import wx
import wx.xrc
import ConsultasGui as cg
import empleado as em

###########################################################################
## Class GeneradorConsulta
###########################################################################

class GeneradorConsulta ( wx.Frame ):
    def __init__( self, parent,tablaEmpleados):
        self.tablaEmpleados = tablaEmpleados
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'Bases de datos', pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        Separador = wx.BoxSizer( wx.VERTICAL )
        self.BotonConsulta1 = wx.Button( self, wx.ID_ANY, u"Consulta between", wx.DefaultPosition, wx.DefaultSize, 0 )
        Separador.Add( self.BotonConsulta1, 0, wx.ALL, 5 )
        self.SetSizer( Separador )
        self.Layout()
        self.Centre( wx.BOTH )

        # Conectando Evento onClick
        self.BotonConsulta1.Bind( wx.EVT_BUTTON, self.GenerarConsulta1 )
    def __del__( self ):
        pass

    # Evento al dar click al boton consulta
    def GenerarConsulta1( self, event ):
        #Tabla completa
        fm = cg.Tabla(None)
        fm.Mostrar(self.tablaEmpleados, 'Employees')


        #Seleccion
        fmS = cg.Tabla(None)
        listaSeleccion = []
        relacion = self.tablaEmpleados[0]
        self.tablaEmpleados.pop(0)#Elimina el nombre de la relacion
        listaSeleccion.append(relacion)
        
        #Para cara empleado en la tab la Empleados
        for empleado in self.tablaEmpleados:
            if empleado.salary >= 10000 and empleado.salary <= 15000:
                listaSeleccion.append(empleado)
        fmS.Mostrar(listaSeleccion, 'Seleccion')


        #Proyeccion
        fmP = cg.Tabla(None)
        fmP.MostrarProyeccion(listaSeleccion, 'Proyeccion')

        #Se muestran los resultados en ventanas diferentes
        fm.Show()
        fmS.Show()
        fmP.Show()