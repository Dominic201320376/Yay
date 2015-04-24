from Tkinter import *

class Page(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)

		self.createWidgets()

	def createWidgets(self):
		self.master.title("Hello World")

Window = Tk()
Main = Page(Window)
Window.geometry('1000x600+170+80')
Window.resizable(0,0)
Window.mainloop()