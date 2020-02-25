import wx

class Tabla(wx.Frame):

    def __init__(self, *args, **kw):
        super(Tabla, self).__init__(*args, **kw)
        #self.InitUI()
    def __del__(self): pass
    
    def Mostrar(self, listaSeleccion, title):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)
        self.tablaEmpleados = listaSeleccion
        self.list = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT)
        i = 0
        for columna in self.tablaEmpleados[0]:
            self.list.InsertColumn(i, columna, wx.LIST_FORMAT_CENTER, 100)
            i += 1

        listaDeTuplas = []
        filas = self.tablaEmpleados.copy()
        filas.pop(0)
        for empleado in filas:
            listaEmpleado = empleado.empleadoToList()
            tupla = tuple(listaEmpleado)
            listaDeTuplas.append(tupla)
        
        idx = 0
        for tup in listaDeTuplas:
            index = self.list.InsertItem(idx, tup[0])
            self.list.SetItem(index, 1, tup[1])
            self.list.SetItem(index, 2, tup[2])
            self.list.SetItem(index, 3, tup[3])
            self.list.SetItem(index, 4, tup[4])
            self.list.SetItem(index, 5, tup[5])
            self.list.SetItem(index, 6, tup[6])
            self.list.SetItem(index, 7, tup[7])
            self.list.SetItem(index, 8, tup[8])
            self.list.SetItem(index, 9, tup[9])
            self.list.SetItem(index, 10, tup[10])
            idx += 1

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.SetTitle(title)
        if title == 'Employees':
            self.MoveXY(90, 120)
        else:
            self.CentreOnScreen()
        

    def MostrarProyeccion(self, listaSeleccion, title):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)
        self.tablaEmpleados = listaSeleccion
        self.list = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'first_name', wx.LIST_FORMAT_CENTER, 100)
        self.list.InsertColumn(1, 'salary', wx.LIST_FORMAT_CENTER, 100)

        listaDeTuplas = []
        filas = self.tablaEmpleados.copy()
        filas.pop(0)
        for empleado in filas:
            listaEmpleado = empleado.empleadoToList()
            tupla = tuple(listaEmpleado)
            listaDeTuplas.append(tupla)
        idx = 0
        for tup in listaDeTuplas:
            index = self.list.InsertItem(idx, tup[1])
            self.list.SetItem(index, 1, tup[7])
            idx +=1

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.SetTitle(title)
        self.MoveXY(875, 120)