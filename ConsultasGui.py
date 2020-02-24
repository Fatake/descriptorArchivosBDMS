import wx
import wx.xrc

#################
## Class Tabla ##
#################

class Tabla ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Tabla", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.ICONIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		separador = wx.FlexGridSizer( 0, 0, 0, 0 )
		separador.SetFlexibleDirection( wx.BOTH )
		separador.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		separador.SetMinSize( wx.Size( 150,150 ) ) 
		self.textArea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		self.textArea.SetMinSize( wx.Size( 475,250 ) )
		
		separador.Add( self.textArea, 0, wx.ALL, 5 )
		
		
		self.SetSizer( separador )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

