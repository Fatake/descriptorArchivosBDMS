import wx
import wx.xrc
import empleado as em

###########################################################################
## Class VentanaPrincipal
###########################################################################

class VentanaPrincipal ( wx.Frame ):
    

    def __init__( self, parent , tablaEmpleados):
        self.__rutaImgagen__ = "D:\Documentos\Computacion\Programacion\BasesDatos\descriptorArchivosBDMS\consulta.jpg"
        self.tablaEmpleados = tablaEmpleados

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "GeneradorConsultas", pos = wx.DefaultPosition, size = wx.Size( 950,670 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.STAY_ON_TOP|wx.HSCROLL|wx.NO_BORDER|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        separadorPrincipal = wx.BoxSizer( wx.VERTICAL )

        self.separadorPaginas = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH|wx.NB_NOPAGETHEME )
        self.panelPrincipal = wx.Panel( self.separadorPaginas, wx.ID_ANY, wx.DefaultPosition, wx.Size( 950,670 ), wx.TAB_TRAVERSAL )
        self.panelPrincipal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

        separadorPanelPrincipal = wx.BoxSizer( wx.VERTICAL )

        self.labelInformacion = wx.StaticText( self.panelPrincipal, wx.ID_ANY, "Programa que dado un descriptor de archivo\nGenera una relacion Empleados\nGenera una consulta", wx.Point( 450,-1 ), wx.DefaultSize, wx.ALIGN_CENTRE )
        self.labelInformacion.Wrap( -1 )
        separadorPanelPrincipal.Add( self.labelInformacion, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.botonGeneralConsulta = wx.BitmapButton( self.panelPrincipal, wx.ID_ANY, wx.Bitmap( self.__rutaImgagen__, wx.BITMAP_TYPE_ANY ), wx.Point( 15,30 ), wx.Size( 750,410 ), wx.BU_AUTODRAW )

        separadorPanelPrincipal.Add( self.botonGeneralConsulta, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.panelPrincipal.SetSizer( separadorPanelPrincipal )
        self.panelPrincipal.Layout()
        self.separadorPaginas.AddPage( self.panelPrincipal, "Consulta", False )

        self.tabla = wx.Panel( self.separadorPaginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.tabla.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

        self.separadorTabla = wx.BoxSizer( wx.VERTICAL )

        self.labelNoConsultado = wx.StaticText( self.panelPrincipal, wx.ID_ANY, "De Clic en el boton generar consulta", wx.Point( 450,-1 ), wx.DefaultSize, wx.ALIGN_CENTRE )
        self.labelInformacion.Wrap( -1 )
        

        self.tabla.SetSizer( self.separadorTabla )
        self.tabla.Layout()
        self.separadorTabla.Fit( self.tabla )
        self.separadorTabla.Add( self.labelNoConsultado, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.separadorPaginas.AddPage( self.tabla, "Tabla", False )

    
        self.seleccion = wx.Panel( self.separadorPaginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.seleccion.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

        self.separadorSeleccion = wx.BoxSizer( wx.VERTICAL )


        self.seleccion.SetSizer( self.separadorSeleccion )
        self.seleccion.Layout()
        self.separadorSeleccion.Fit( self.seleccion )
        self.separadorSeleccion.Add( self.labelNoConsultado, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.separadorPaginas.AddPage( self.seleccion, "Seleccion", False )



        self.proyeccion = wx.Panel( self.separadorPaginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.proyeccion.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

        self.separadorProyeccion = wx.BoxSizer( wx.VERTICAL )


        self.proyeccion.SetSizer( self.separadorProyeccion )
        self.proyeccion.Layout()
        self.separadorProyeccion.Fit( self.proyeccion )
        self.separadorProyeccion.Add( self.labelNoConsultado, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.separadorPaginas.AddPage( self.proyeccion, "Proyeccion", False )

        separadorPrincipal.Add( self.separadorPaginas, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( separadorPrincipal )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.botonGeneralConsulta.Bind( wx.EVT_BUTTON, self.botonGeneralConsultaOnButtonClick )

    def __del__( self ):
        pass


    # Eventos escuchadores
    def botonGeneralConsultaOnButtonClick( self, event ):
        event.Skip()
        # Tabla Completa
        self.Mostrar(self.tablaEmpleados, "Tabla")

        # Seleccion
        listaSeleccion = []
        relacion = self.tablaEmpleados[0]
        self.tablaEmpleados.pop(0)#Elimina el nombre de la relacion
        listaSeleccion.append(relacion)
        
        # Para cara empleado en la tab la Empleados
        for empleado in self.tablaEmpleados:
            if empleado.salary >= 10000 and empleado.salary <= 15000:
                listaSeleccion.append(empleado)
        self.Mostrar(listaSeleccion, "Seleccion")


        # Proyeccion
        self.MostrarProyeccion(listaSeleccion)


    def Mostrar(self, listaSeleccion, title):
        if title == "Tabla":
            separador = self.separadorTabla
            panel = self.tabla
        elif title == "Seleccion":
            separador = self.separadorSeleccion
            panel = self.seleccion

        self.labelNoConsultado.SetLabelText(""+title)

        listaProyectada = wx.ListCtrl(panel, wx.ID_ANY,size=wx.Size( 940,660 ), style=wx.LC_REPORT)
        i = 0
        for columna in listaSeleccion[0]:
            listaProyectada.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1

        listaDeTuplas = []
        filas = listaSeleccion.copy()
        filas.pop(0)
        for empleado in filas:
            listaEmpleado = empleado.empleadoToList()
            tupla = tuple(listaEmpleado)
            listaDeTuplas.append(tupla)

        idx = 0
        for tup in listaDeTuplas:
            index = listaProyectada.InsertItem(idx, tup[0])
            listaProyectada.SetItem(index, 1, tup[1])
            listaProyectada.SetItem(index, 2, tup[2])
            listaProyectada.SetItem(index, 3, tup[3])
            listaProyectada.SetItem(index, 4, tup[4])
            listaProyectada.SetItem(index, 5, tup[5])
            listaProyectada.SetItem(index, 6, tup[6])
            listaProyectada.SetItem(index, 7, tup[7])
            listaProyectada.SetItem(index, 8, tup[8])
            listaProyectada.SetItem(index, 9, tup[9])
            listaProyectada.SetItem(index, 10, tup[10])
            idx += 1

        listaProyectada.SetVirtualSize(940,660)
        separador.Add(listaProyectada, 1, wx.EXPAND)
        panel.SetSizer(separador)


    # Funcion que muestra la proyeccion
    def MostrarProyeccion(self, listaSeleccion):
        self.labelNoConsultado.SetLabelText("Proyeccion")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = self.proyeccion
        listaProyectada = wx.ListCtrl(panel, wx.ID_ANY,size=wx.Size( 940,660 ), style=wx.LC_REPORT)

        listaProyectada.InsertColumn(0, 'first_name', wx.LIST_FORMAT_CENTER, 100)
        listaProyectada.InsertColumn(1, 'salary', wx.LIST_FORMAT_CENTER, 100)

        listaDeTuplas = []
        filas = listaSeleccion.copy()
        filas.pop(0)
        for empleado in filas:
            listaEmpleado = empleado.empleadoToList()
            tupla = tuple(listaEmpleado)
            listaDeTuplas.append(tupla)

        idx = 0
        for tup in listaDeTuplas:
            index = listaProyectada.InsertItem(idx, tup[1])
            listaProyectada.SetItem(index, 1, tup[7])
            idx +=1

        listaProyectada.SetVirtualSize(940,660)
        hbox.Add(listaProyectada, 1, wx.EXPAND)
        panel.SetSizer(hbox)


