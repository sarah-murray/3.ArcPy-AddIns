import arcpy
import pythonaddins

class ComboBoxClass7(object):
	"""Implementation for addin_addin.combobox (ComboBox)"""
	def __init__(self):
		self.items = ["item1", "item2"]
		self.editable = True
		self.enabled = True
		self.dropdownWidth = 'WWWWWW'
		self.width = 'WWWWWW'
	def onSelChange(self, selection):
		pass
	def onEditChange(self, text):
		pass
	def onFocus(self, focused):
		pass
	def onEnter(self):
		pass
	def refresh(self):
		pass

class ExplosionButtonClass(object):
	"""Implementation for addin_addin.button (Button)"""
	def __init__(self):
		self.enabled = True
		self.checked = False
	def onClick(self):
		object = pythonaddins.GPToolDialog("M:/All_GIS_work/Programming2/Prac1/Models.tbx", "Prac2ExplosionScript")
		combobox.items()