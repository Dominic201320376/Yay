from Tkinter import *
import tkMessageBox
import time
import tkFileDialog

class GUI(Tk):
    def __init__(self, parent):
        Tk.__init__(self,parent)
        self.parent=parent
    def main(self):
        self.geometry('1200x700-50-50')
        self.resizable(False, False)
        self.title('Yay')

        self.image=PhotoImage(file='RoadMap.pbm')
        self.bgimage=Label(image=self.image)
        self.bgimage.place(x=0, y=0, relwidth=1, relheight=1)

        self.setedge()
    def setedge(self):
        self.headerphoto=PhotoImage(file='Logo.pbm')
        self.header=Label(self, image=self.headerphoto, bd=0)
        self.header.place(relx=0.02, rely=0.01)

        self.start=Label(self, text='Start:', font=('Helvetica', '10'), fg='#d92d33', bg='#c6c6c4')
        self.start.place(relx=0.05, rely=0.18)
        self.startinput=Label(self, text='Text', font=('Helvetica', '10'), fg='#443266')
        self.startinput.place(relx=0.1, rely=0.18)
        self.startbutton=Button(self, text='Clear', command=self.main)
        self.startbutton.place(relx=0.15, rely=0.18)

        self.end=Label(self, text='End:', font=('Helvetica', '10'), fg='#d92d33', bg='#c6c6c4')
        self.end.place(relx=0.05, rely=0.22)
        self.endinput=Label(self, text='Text', font=('Helvetica', '10'), fg='#443266')
        self.endinput.place(relx=0.1, rely=0.22)
        self.endbutton=Button(self, text='Clear', command=self.main)
        self.endbutton.place(relx=0.15, rely=0.22)

        self.quick=Label(self, text='Quickest Path:', font=('Helvetica', '10'), fg='#d92d33', bg='#c6c6c4')
        self.quick.place(relx=0.05, rely=0.32)
        self.quickoutput=Label(self, text='Insert some text here.', font=('Helvetica', '10'), fg='#443266')
        self.quickoutput.place(relx=0.15, rely=0.32)

        self.quicktime=Label(self, text='Time:', font=('Helvetica', '10'), fg='#d92d33', bg='#c6c6c4')
        self.quicktime.place(relx=0.05, rely=0.36)
        self.quicktimeoutput=Label(self, text='Insert some text here.', font=('Helvetica', '10'), fg='#443266')
        self.quicktimeoutput.place(relx=0.15, rely=0.36)

        self.cheapest=Label(self, text='Cheapest Path:', font=('Helvetica', '10'), fg='#d92d33', bg='#c6c6c4')
        self.cheapest.place(relx=0.05, rely=0.46)
        self.cheapestoutput=Label(self, text='Insert some text here.', font=('Helvetica', '10'), fg='#443266')
        self.cheapestoutput.place(relx=0.15, rely=0.46)

        self.cheapcost=Label(self, text='Cost:', font=('Helvetica', '10'), fg='#d92d33', bg='#c6c6c4')
        self.cheapcost.place(relx=0.05, rely=0.50)
        self.cheapcostoutput=Label(self, text='Insert some text here.', font=('Helvetica', '10'), fg='#443266')
        self.cheapcostoutput.place(relx=0.15, rely=0.50)

        # Nodes 1-48.

        self.photo1=PhotoImage(file='E1.pbm')
        self.pic1=Label(self, image=self.photo1, bd=0)
        self.pic1.place(rely=0.1465, relx=0.3937)

        self.photo2=PhotoImage(file='E2.pbm')
        self.pic2=Label(self, image=self.photo2, bd=0)
        self.pic2.place(rely=0.206, relx=0.427)

        self.photo3=PhotoImage(file='E3.pbm')
        self.pic3=Label(self, image=self.photo3, bd=0)
        self.pic3.place(rely=0.1675, relx=0.4523)

        self.photo4=PhotoImage(file='E4.pbm')
        self.pic4=Label(self, image=self.photo4, bd=0)
        self.pic4.place(rely=0.205, relx=0.463)

        self.photo5=PhotoImage(file='E5.pbm')
        self.pic5=Label(self, image=self.photo5, bd=0)
        self.pic5.place(rely=0.135, relx=0.487)

        self.photo6=PhotoImage(file='E6.pbm')
        self.pic6=Label(self, image=self.photo6, bd=0)
        self.pic6.place(rely=0.081, relx=0.52)

        self.photo7=PhotoImage(file='E7.pbm')
        self.pic7=Label(self, image=self.photo7, bd=0)
        self.pic7.place(rely=0.23, relx=0.421)

        self.photo8=PhotoImage(file='E8.pbm')
        self.pic8=Label(self, image=self.photo8, bd=0)
        self.pic8.place(rely=0.231, relx=0.45799)

        self.photo9=PhotoImage(file='E9.pbm')
        self.pic9=Label(self, image=self.photo9, bd=0)
        self.pic9.place(rely=0.2349, relx=0.4671)

        self.photo10=PhotoImage(file='E10.pbm')
        self.pic10=Label(self, image=self.photo10, bd=0)
        self.pic10.place(rely=0.273, relx=0.484)

        self.photo11=PhotoImage(file='E11.pbm')
        self.pic11=Label(self, image=self.photo11, bd=0)
        self.pic11.place(rely=0.235, relx=0.495)

        self.photo12=PhotoImage(file='E12.pbm')
        self.pic12=Label(self, image=self.photo12, bd=0)
        self.pic12.place(rely=0.249, relx=0.505)

        self.photo13a=PhotoImage(file='E13a.pbm')
        self.pic13a=Label(self, image=self.photo13a, bd=0)
        self.pic13a.place(rely=0.15, relx=0.517)

        self.photo13b=PhotoImage(file='E13b.pbm')
        self.pic13b=Label(self, image=self.photo13b, bd=0)
        self.pic13b.place(rely=0.22, relx=0.548)

        self.photo14=PhotoImage(file='E14.pbm')
        self.pic14=Label(self, image=self.photo14, bd=0)
        self.pic14.place(rely=0.2799, relx=0.4479)

        self.photo15=PhotoImage(file='E15.pbm')
        self.pic15=Label(self, image=self.photo15, bd=0)
        self.pic15.place(rely=0.29, relx=0.4)

        self.photo16=PhotoImage(file='E16.pbm')
        self.pic16=Label(self, image=self.photo16, bd=0)
        self.pic16.place(rely=0.3, relx=0.4419)

        self.photo17=PhotoImage(file='E17.pbm')
        self.pic17=Label(self, image=self.photo17, bd=0)
        self.pic17.place(rely=0.3092, relx=0.431)

        self.photo18=PhotoImage(file='E18.pbm')
        self.pic18=Label(self, image=self.photo18, bd=0)
        self.pic18.place(rely=0.299, relx=0.458)

        self.photo19=PhotoImage(file='E19.pbm')
        self.pic19=Label(self, image=self.photo19, bd=0)
        self.pic19.place(rely=0.2995, relx=0.4886)

        self.photo20=PhotoImage(file='E20.pbm')
        self.pic20=Label(self, image=self.photo20, bd=0)
        self.pic20.place(rely=0.289, relx=0.506)

        self.photo21=PhotoImage(file='E21.pbm')
        self.pic21=Label(self, image=self.photo21, bd=0)
        self.pic21.place(rely=0.291, relx=0.543)

        self.photo22a=PhotoImage(file='E22a.pbm')
        self.pic22a=Label(self, image=self.photo22a, bd=0)
        self.pic22a.place(rely=0.291, relx=0.543)
g=GUI(None)
g.main()
g.mainloop()
