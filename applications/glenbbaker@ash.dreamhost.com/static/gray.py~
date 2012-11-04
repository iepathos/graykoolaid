from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui import KeyboardListener
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.HTML import HTML
from pyjamas.JSONService import JSONProxy

class graybox():
	def onModuleLoad(self):
		self.remote = DataService()
		panel = VerticalPanel()
	
		self.graybox = TextBox()
		self.graybox.addKeyboardListener(self)
	
		self.grayList = ListBox()
		self.grayList.setVisibleItemCount(20)
		self.grayList.setWidth("200px")
		self.grayList.addClickListener(self)
		self.Status = Label("Status Label")
	
		panel.add(Label("Add New Task:"))
		panel.add(self.graybox)
		panel.add(Label("Click to Remove:"))
		panel.add(self.grayList)
		panel.add(self.Status)
		self.remote.getTasks(self)
	
		RootPanel().add(panel)
	
def onKeyUp(self, sender, keyCode, modifiers):
	pass
	
def onKeyDown(self, sender, keyCode, modifiers):
	pass

def onKeyPress(self, sender, keyCode, modifiers):
	if keyCode == KeyboardListener.KEY_ENTER and \
		sender == self.graybox:
			id = self.remote.addTask(sender.getText(),self)
			sender.setText(" ")
			if id<0:
				RootPanel().add(HTML("Server Error or Invalid Response"))
				
def onClick(self, sender):
	id = self.remote.deleteTask(
				sender.getValue(sender.getSelectedIndex()),self)
	if id<0:
		RootPanel().add(
			HTML("Server Error or Invalid Response"))

def onRemoteResponse(self, response, request_info):
	self.grayList.clear()
	for task in response:
		self.grayList.addItem(task[0])
		self.grayList.setValue(self.grayList.getItemCount()-1,
													task[1])

def onRemoteError(self, code, message, request_info):
	self.Status.setText("Server Error or Invalid Response: " \
										 + "ERROR " + code + " - " + message)

class DataService(JSONProxy):
	def __init__(self):
		JSONProxy.__init__(self, "../../default/call/jsonrpc",
												["getTasks", "addTask", "deleteTask"])

if __name__ == '__main__':
	app = graybox()
	app.onModuleLoad()