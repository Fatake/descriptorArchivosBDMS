import wx

class VentanaPrincipal(wx.Frame):
    def __init__(self, parent, tablaEmployees, tablaDepartments):
        super().__init__(parent, wx.ID_ANY, "Bases de datos para Ingeniería", style=wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.STAY_ON_TOP|wx.NO_BORDER|wx.TAB_TRAVERSAL)
        self.tablaEmployees = tablaEmployees
        self.tablaDepartments = tablaDepartments
        self.consulta = ""
        # Estructura para mostrar páginas
        notebook = wx.Notebook(self)
        self.panelInicio = wx.Panel(notebook)
        self.panelTabla = wx.Panel(notebook)
        self.panelSeleccion = wx.Panel(notebook)
        self.panelProyeccion = wx.Panel(notebook)
        # Agregando los paneles a las páginas    
        notebook.AddPage(self.panelInicio, "Gestor de consultas")
        notebook.AddPage(self.panelTabla, "Tablas completas")
        notebook.AddPage(self.panelSeleccion, u"Selección")
        notebook.AddPage(self.panelProyeccion, u"Proyección")
        # Elementos para posicionamiento en el resto de las hojas
        # Contenedores
        self.contenedorTabla =  wx.StaticBox(self.panelTabla, wx.ID_ANY, label="Tablas completas", size=(1200, -1))
        self.contenedorSeleccion =  wx.StaticBox(self.panelSeleccion, wx.ID_ANY, label=u"Sólo Selección", size=(1200, -1))
        self.contenedorProyeccion =  wx.StaticBox(self.panelProyeccion, wx.ID_ANY, label=u"Sólo Proyección", size=(1200, -1))
        # Sizers
        self.szTablaPrincipal = wx.BoxSizer(wx.VERTICAL)
        self.szSeleccionPrincipal = wx.BoxSizer(wx.VERTICAL)
        self.szProyeccionPrincipal = wx.BoxSizer(wx.VERTICAL)
        # Inicializando cada pagina de la interfaz
        self.paginaInicio(self.panelInicio)
        self.inicializarPaginas(self.panelTabla, self.contenedorTabla, self.szTablaPrincipal, u"\tMuestra todas las tuplas y columnas de la tabla cargada, cuya información es la siguiente:")
        self.inicializarPaginas(self.panelSeleccion, self.contenedorSeleccion, self.szSeleccionPrincipal, u"\tMuestra todas las tuplas que cumplen la condición de consulta, cuya información es la siguiente:")
        self.inicializarPaginas(self.panelProyeccion, self.contenedorProyeccion, self.szProyeccionPrincipal, u"\tMuestra todas las columnas que se solicitan en la consulta, cuya información es la siguiente:")
        # Configurando sizer principal
        sizerPrincipal = wx.BoxSizer()
        sizerPrincipal.Add(notebook, 1, wx.EXPAND, 5)
        self.SetSizer(sizerPrincipal)


    def paginaInicio(self, panelInicio):
        # Paneles de pestaña inicio
        #self.panelInicio = panelInicio
        panelInicio.SetBackgroundColour("#74ccf0")
        # Contenedor 
        contenedorInferior = wx.StaticBox(panelInicio, wx.ID_ANY, label="Consultas disponibles", pos=(50, 100), size=(720, -1))
        contenedorInferior.SetBackgroundColour("#74ccf0")
        # Sizers
        szInicioPrincipal = wx.BoxSizer(wx.VERTICAL)
        # Elementos gráficos
        informacion = wx.StaticText(panelInicio, -1, u"Programa que dado un descriptor de archivos\ngenera la tabla correspondiente y realiza\nalgunas consultas ya definidas", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE) #self.panelInicioSuperior
        imagen = wx.StaticBitmap(panelInicio, wx.ID_ANY, wx.Bitmap('presentacion.jpg', wx.BITMAP_TYPE_ANY), size = (720,524))
        # Datos para los ComboBox
        consultas =  u"Between|Join".split("|")
        self.listaConsultas = wx.ComboBox(contenedorInferior, -1, choices=consultas,  pos = (165, 15), size = (238, 25))
        self.aceptarConsulta = wx.Button(contenedorInferior, label="Aceptar", pos=(430, 15), size=(100,25))
        self.aceptarConsulta.Show(False)
        # Agregando los elementos a los sizers
        szInicioPrincipal.Add(informacion, 1, wx.EXPAND|wx.ALL, 20)
        szInicioPrincipal.Add(imagen, 1, wx.EXPAND|wx.ALL)
        szInicioPrincipal.Add(contenedorInferior, 2,  wx.ALIGN_CENTRE|wx.ALL, 10)
        # Configurando Sizers
        panelInicio.SetSizer(szInicioPrincipal)   
        self.listaConsultas.Bind(wx.EVT_COMBOBOX, self.seleccionConsulta)
        self.aceptarConsulta.Bind(wx.EVT_BUTTON, self.realizaConsulta)


    def inicializarPaginas(self, panelActual, contenedorActual, sizerActual, informacion):
        # Paneles de pestaña inicio
        panel = panelActual
        contenedor = contenedorActual
        sizer = sizerActual
        panel.SetBackgroundColour("#74ccf0")
        contenedor.SetBackgroundColour("#74ccf0")
        # Elementos gráficos
        informacion = wx.StaticText(contenedor, wx.ID_ANY, informacion, pos=(25,25), size=(1000,50))#"\tMuestra todas las tuplas y columnas de la tabla cargada, cuya información es la siguiente:"
        # Agregando los elementos a los sizers
        sizer.Add(contenedor, 1, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTRE, 30)
        # Configurando Sizers
        panel.SetSizer(sizer)


    def seleccionConsulta(self,event):
        self.consulta = self.listaConsultas.GetValue()
        print("Consulta seleccionada: "+self.consulta)
        self.aceptarConsulta.Show(True)


    def realizaConsulta(self, event):
        self.aceptarConsulta.Show(False)
        event.Skip()
        if self.consulta == "Between":
            tablaEmpleados = self.tablaEmployees.copy()
            # Tabla Completa
            self.mostrarTablaBetween(tablaEmpleados, True)
            # Seleccion
            listaEmpleados = []
            atributosEmpleados = tablaEmpleados[0]
            tablaEmpleados.pop(0)
            listaEmpleados.append(atributosEmpleados)
            # Se realiza la consulta between solicitada
            for empleado in tablaEmpleados:
                if empleado.salary >= 10000 and empleado.salary <= 15000:
                    listaEmpleados.append(empleado)
            tuplasSeleccionadas = self.mostrarSeleccionBetween(listaEmpleados)
            # Proyeccion
            self.mostrarProyeccionBetween(tuplasSeleccionadas)
        else:
            tablaEmpleados = self.tablaEmployees.copy()
            tablaDepartamentos = self.tablaDepartments.copy()
            # Tabla Completa
            self.mostrarTablaJoin(tablaEmpleados, tablaDepartamentos)
            self.szTablaPrincipal.SetContainingWindow(self.panelTabla)
            self.panelTabla.SetSizer(self.szTablaPrincipal)
            # Empleados
            listaEmpleados = []
            atributosEmpleados = tablaEmpleados[0]
            tablaEmpleados.pop(0)
            listaEmpleados.append(atributosEmpleados)
            # Departamentos
            listaDepartamentos = []
            atributosDepartamentos = tablaDepartamentos[0]
            tablaDepartamentos.pop(0)
            listaDepartamentos.append(atributosDepartamentos)
            # Se realiza la consulta join solicitada
            for empleado in tablaEmpleados:
                if empleado.department_id != "null":
                    listaEmpleados.append(empleado)
                    for departamento in tablaDepartamentos:
                        if int(empleado.department_id) == int(departamento.department_id):
                            listaDepartamentos.append(departamento)
            tuplasSeleccionadas = self.mostrarSeleccionJoin(listaEmpleados, listaDepartamentos)
            # Proyección
            self.mostrarProyeccionJoin(tuplasSeleccionadas)


    def mostrarTablaBetween(self, tablaEmpleados, band):
        wx.StaticText(self.contenedorTabla, wx.ID_ANY, "Employees", pos=(20,40), size=(1000,50))
        if band:
            self.listaTablaCompletaB = wx.ListCtrl(self.contenedorTabla, wx.ID_ANY, pos=(35, 60), size=wx.Size(1120,500), style=wx.LC_REPORT) #self.contendorTabla, wx.ID_ANY,size=wx.Size(940,660), style=wx.LC_REPORT)
        else:
            self.listaTablaCompletaB = wx.ListCtrl(self.contenedorTabla, wx.ID_ANY, pos=(35, 60), size=wx.Size(1120,250), style=wx.LC_REPORT)
        i = 0
        for columna in tablaEmpleados[0]:
            self.listaTablaCompletaB.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1
        listaDeTuplas = []
        filas = tablaEmpleados.copy()
        filas.pop(0)
        for empleado in filas:
            listaEmpleado = empleado.employeeToList()
            tupla = tuple(listaEmpleado)
            listaDeTuplas.append(tupla)
        idx = 0
        for tup in listaDeTuplas:
            columna = 1
            index = self.listaTablaCompletaB.InsertItem(idx, tup[0])
            while columna < len(listaDeTuplas[0]):
                self.listaTablaCompletaB.SetItem(index, columna, tup[columna])
                columna += 1
            idx += 1
        self.szTablaPrincipal.SetContainingWindow(self.panelTabla)
        # Configurando Sizers
        self.panelTabla.SetSizer(self.szTablaPrincipal)
    

    def mostrarSeleccionBetween(self, listaSeleccion):
        self.listaTablaSeleccionB = wx.ListCtrl(self.contenedorSeleccion, wx.ID_ANY, pos=(35, 60), size=wx.Size(1120,500), style=wx.LC_REPORT) #self.contendorTabla, wx.ID_ANY,size=wx.Size(940,660), style=wx.LC_REPORT)
        i = 0
        for columna in listaSeleccion[0]:
            self.listaTablaSeleccionB.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1
        listaDeTuplas = []
        filas = listaSeleccion.copy()
        filas.pop(0)
        for empleado in filas:
            listaEmpleado = empleado.employeeToList()
            tupla = tuple(listaEmpleado)
            listaDeTuplas.append(tupla)
        idx = 0
        for tup in listaDeTuplas:
            columna = 1
            index = self.listaTablaSeleccionB.InsertItem(idx, tup[0])
            while columna < len(listaDeTuplas[0]):
                self.listaTablaSeleccionB.SetItem(index, columna, tup[columna])
                columna += 1
            idx += 1
        self.szSeleccionPrincipal.SetContainingWindow(self.panelSeleccion)
        # Configurando Sizers
        self.panelSeleccion.SetSizer(self.szSeleccionPrincipal)
        return listaDeTuplas


    def mostrarProyeccionBetween(self, tuplasSeleccionadas):
        self.listaTablaProyeccionB = wx.ListCtrl(self.contenedorProyeccion, wx.ID_ANY, pos=(200, 70), size=wx.Size(200,450), style=wx.LC_REPORT)
        self.listaTablaProyeccionB.InsertColumn(0, 'first_name', wx.LIST_FORMAT_CENTER, 100)
        self.listaTablaProyeccionB.InsertColumn(1, 'salary', wx.LIST_FORMAT_CENTER, 100)
        idx = 0
        for tup in tuplasSeleccionadas:
            index = self.listaTablaProyeccionB.InsertItem(idx, tup[1])
            self.listaTablaProyeccionB.SetItem(index, 1, tup[7])
            idx +=1
        # Agregando los elementos a los sizers
        self.szProyeccionPrincipal.SetContainingWindow(self.panelProyeccion)
        # Configurando Sizers
        self.panelProyeccion.SetSizer(self.szProyeccionPrincipal)


    def mostrarTablaJoin(self, tablaEmpleados, tablaDepartamentos):
        self.mostrarTablaBetween(tablaEmpleados, False)
        wx.StaticText(self.contenedorTabla, wx.ID_ANY, "Departments", pos=(20,320), size=(1000,50))
        self.listaTablaCompletaJ = wx.ListCtrl(self.contenedorTabla, wx.ID_ANY, pos=(35, 340), size=wx.Size(420,250), style=wx.LC_REPORT) #self.contendorTabla, wx.ID_ANY,size=wx.Size(940,660), style=wx.LC_REPORT)
        i = 0
        for columna in tablaDepartamentos[0]:
            self.listaTablaCompletaJ.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1
        listaDeTuplas = []
        filas = tablaDepartamentos.copy()
        filas.pop(0)
        for department in filas:
            listaDepartamento = department.departmentToList()
            tupla = tuple(listaDepartamento)
            listaDeTuplas.append(tupla)
        idx = 0
        for tup in listaDeTuplas:
            columna = 1
            index = self.listaTablaCompletaJ.InsertItem(idx, tup[0])
            while columna < len(listaDeTuplas[0]):
                self.listaTablaCompletaJ.SetItem(index, columna, tup[columna])
                columna += 1
            idx += 1
        self.szTablaPrincipal.SetContainingWindow(self.panelTabla)
        self.panelTabla.SetSizer(self.szTablaPrincipal)


    def mostrarSeleccionJoin(self, listaEmpleados, listaDepartamentos):
        self.listaTablaSeleccionJ = wx.ListCtrl(self.contenedorSeleccion, wx.ID_ANY, pos=(35, 60), size=wx.Size(1120,500), style=wx.LC_REPORT) #self.contendorTabla, wx.ID_ANY,size=wx.Size(940,660), style=wx.LC_REPORT)
        i = 0
        for columna in listaEmpleados[0]:
            self.listaTablaSeleccionJ.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1
        for columna in listaDepartamentos[0]:
            self.listaTablaSeleccionJ.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1
        filasEmpleados = listaEmpleados.copy()
        filasEmpleados.pop(0)
        filasDepartamentos = listaDepartamentos.copy()
        filasDepartamentos.pop(0)
        listaSeleccion = []
        for empleado in filasEmpleados:
            listaSeleccion.append(empleado.employeeToList())
        departamentos = []
        for departamento in filasDepartamentos:
            departamentos.append(departamento.departmentToList())
        # Uniendo ambas listas 
        i = 0
        for i in range(len(listaSeleccion)):
            listaSeleccion[i].extend(departamentos[i])
        listaDeTuplas = []
        for fila in listaSeleccion:
            tupla = tuple(fila)
            listaDeTuplas.append(tupla)
        idx = 0
        for tup in listaDeTuplas:
            columna = 1
            index = self.listaTablaSeleccionJ.InsertItem(idx, tup[0])
            while columna < len(listaDeTuplas[0]):
                self.listaTablaSeleccionJ.SetItem(index, columna, tup[columna])
                columna += 1
            idx += 1
        self.szSeleccionPrincipal.SetContainingWindow(self.panelSeleccion)
        # Configurando Sizers
        self.panelSeleccion.SetSizer(self.szSeleccionPrincipal)
        return listaDeTuplas


    # Funcion que muestra la proyeccion
    def mostrarProyeccionJoin(self, tuplasSeleccionadas):
        self.listaTablaProyeccionJ = wx.ListCtrl(self.contenedorProyeccion, wx.ID_ANY, pos=(200, 70), size=wx.Size(520,500), style=wx.LC_REPORT)
        self.listaTablaProyeccionJ.InsertColumn(0, 'employee_id', wx.LIST_FORMAT_CENTER, 100)
        self.listaTablaProyeccionJ.InsertColumn(1, 'first_name', wx.LIST_FORMAT_CENTER, 100)
        self.listaTablaProyeccionJ.InsertColumn(2, 'department_id', wx.LIST_FORMAT_CENTER, 100)
        self.listaTablaProyeccionJ.InsertColumn(3, 'department_id', wx.LIST_FORMAT_CENTER, 100)
        self.listaTablaProyeccionJ.InsertColumn(4, 'location_id', wx.LIST_FORMAT_CENTER, 100)
        idx = 0
        for tup in tuplasSeleccionadas:
            index = self.listaTablaProyeccionJ.InsertItem(idx, tup[0])
            self.listaTablaProyeccionJ.SetItem(index, 1, tup[1])
            self.listaTablaProyeccionJ.SetItem(index, 2, tup[10])
            self.listaTablaProyeccionJ.SetItem(index, 3, tup[11])
            self.listaTablaProyeccionJ.SetItem(index, 4, tup[14])
            idx +=1
        # Agregando los elementos a los sizers
        self.szProyeccionPrincipal.SetContainingWindow(self.panelProyeccion)
        # Configurando Sizers
        self.panelProyeccion.SetSizer(self.szProyeccionPrincipal)