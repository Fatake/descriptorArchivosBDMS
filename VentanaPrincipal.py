import wx
import wx.xrc
import tkinter as tk
import ConsultasGui as cg
import empleado as em

#############################
## Class GeneradorConsulta ##
#############################

class GeneradorConsulta ( wx.Frame ):

    def __init__( self, parent,tablaEmpleados):
        self.tablaEmpleados = tablaEmpleados
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Proyecto Final: BD", pos = wx.DefaultPosition, size = wx.Size( 400,225 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        Separador = wx.BoxSizer( wx.VERTICAL )

        self.BotonConsulta1 = wx.Button( self, wx.ID_ANY, u"Tabla completa", wx.DefaultPosition, wx.DefaultSize, 0 )
        Separador.Add( self.BotonConsulta1, 0, wx.ALL, 10 )
        
        self.BotonConsulta2 = wx.Button( self, wx.ID_ANY, u"Consulta between", wx.DefaultPosition, wx.DefaultSize, 0 )
        Separador.Add( self.BotonConsulta2, 0, wx.ALL, 10 )

        self.BotonConsulta3 = wx.Button( self, wx.ID_ANY, u"Tabla consulta final", wx.DefaultPosition, wx.DefaultSize, 0 )
        Separador.Add( self.BotonConsulta3, 0, wx.ALL, 10 )

        self.BotonConsultaTODO = wx.Button( self, wx.ID_ANY, u"Muestra todas las tablas", wx.DefaultPosition, wx.DefaultSize, 0 )
        Separador.Add( self.BotonConsultaTODO, 0, wx.ALL, 10 )
        
        self.SetSizer( Separador )
        self.Layout()

        self.Centre( wx.BOTH )

        # Conectando Evento onClick
        self.BotonConsulta1.Bind( wx.EVT_BUTTON, self.GenerarConsulta1 )
        self.BotonConsulta2.Bind( wx.EVT_BUTTON, self.GenerarConsulta2 )
        self.BotonConsulta3.Bind( wx.EVT_BUTTON, self.GenerarConsulta3 )
        self.BotonConsultaTODO.Bind( wx.EVT_BUTTON, self.GenerarConsultaTODO )


    def __del__( self ):
        pass


    # Evento al dar click al boton consulta
    def GenerarConsulta1( self, event ):
        # Por agregar consulta
        print("\n\n\\\\\\\\\\Tabla Completa//////////")
        #Tabla Completa
        #fm = cg.Tabla(None)
        root = tk.Tk()
        root.title("Tabla Completa")
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=100)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        for empleado in self.tablaEmpleados:
            T.insert(tk.END, str(empleado)+"\n")
        
        tk.mainloop()    
    # Evento al dar click al boton consulta
    def GenerarConsulta2( self, event ):
        #Tabla Seleccion between
        listaSeleccion = []
        root = tk.Tk()
        root.title("Tabla Seleccion")
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=100)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)

        for empleado in self.tablaEmpleados:
            if int(empleado.salary) >= 10000 and int(empleado.salary) <= 15000:
                listaSeleccion.append(empleado)
                T.insert(tk.END, str(empleado.first_name)+" "+str(empleado.salary)+"\n")
        tk.mainloop()        
    # Evento al dar click al boton consulta
    def GenerarConsulta3( self, event ):
        #Tabla Consulta Final
        listaSeleccion = []
        root = tk.Tk()
        root.title("Tabla Consulta Final")
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=100)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        for empleado in self.tablaEmpleados:
        #for empleado in listaSeleccion:
            T.insert(tk.END, str(empleado.first_name)+" "+str(empleado.salary)+"\n")
        tk.mainloop() 
    # Evento al dar click al boton consulta
    def GenerarConsultaTODO( self, event ):
        # Por agregar consulta
        #Tabla Completa
        root = tk.Tk()
        root.title("Tabla Completa")
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=100)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        for empleado in self.tablaEmpleados:
            T.insert(tk.END, str(empleado)+"\n")
        tk.mainloop() 
        #Tabla Seleccion between
        listaSeleccion = []
        root2 = tk.Tk()
        root2.title("Tabla Seleccion")
        S2 = tk.Scrollbar(root2)
        T2 = tk.Text(root2, height=20, width=100)
        S2.pack(side=tk.RIGHT, fill=tk.Y)
        T2.pack(side=tk.LEFT, fill=tk.Y)
        S2.config(command=T2.yview)
        T2.config(yscrollcommand=S2.set)
        for empleado in self.tablaEmpleados:
            if int(empleado.salary) >= 10000 and int(empleado.salary) <= 15000:
                T2.insert(tk.END, str(empleado.first_name)+" "+str(empleado.salary)+"\n")
                listaSeleccion.append(empleado)
        tk.mainloop() 
        #TablaConsultaFinal
        listaSeleccion = []
        root3 = tk.Tk()
        root3.title("Tabla Consulta Final")
        S3 = tk.Scrollbar(root3)
        T3 = tk.Text(root3, height=20, width=100)
        S3.pack(side=tk.RIGHT, fill=tk.Y)
        T3.pack(side=tk.LEFT, fill=tk.Y)
        S3.config(command=T3.yview)
        T3.config(yscrollcommand=S3.set)
        #fm3 = cg.Tabla(None)
        for empleado in self.tablaEmpleados:
            T3.insert(tk.END, str(empleado.first_name)+" "+str(empleado.salary)+"\n")
        tk.mainloop() 
        #Muestra las pantallas
