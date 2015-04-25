from Tkinter import *
import tkMessageBox
import time
import tkFileDialog
from transport import *

class GUI(Tk):
    def __init__(self, parent):
        Tk.__init__(self,parent)
        self.parent=parent
    def main(self):
        self.geometry('1200x700-50-50')
        self.resizable(False, False)
        self.title('HIGHWAYS')

        self.image=PhotoImage(file='RoadMap.pbm')
        self.bgimage=Label(image=self.image)
        self.bgimage.place(x=0, y=0, relwidth=1, relheight=1)

        self.logo=PhotoImage(file='BasicLogo.pbm')
        self.tk.call('wm', 'iconphoto', self._w, self.logo)

        self.setedge()
    def setedge(self):
        self.headerphoto=PhotoImage(file='Logo.pbm')
        self.header=Label(self, image=self.headerphoto, bd=0)
        self.header.place(relx=0.02, rely=0.01)

        self.start=Label(self, text='Start:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.start.place(relx=0.1, rely=0.25)

        self.startVar = StringVar()        
        self.startinput=Label(self, text=self.startVar.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.startinput.place(relx=0.15, rely=0.25)
        self.startbutton=Button(self, text='Clear', command=self.clearStart, font=('Helvetica', "12"), bg='#d92d33', fg='#c6c6c4')
        self.startbutton.place(relx=0.2, rely=0.25)

        self.end=Label(self, text='End:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.end.place(relx=0.1, rely=0.3)

        self.endVar = StringVar()
        self.endinput=Label(self, text=self.endVar.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.endinput.place(relx=0.15, rely=0.3)
        self.endbutton=Button(self, text='Clear', command=self.clearEnd, font=('Helvetica', "12"), bg='#d92d33', fg='#c6c6c4')
        self.endbutton.place(relx=0.2, rely=0.3)

        self.submit = Button(self, text="     Submit     ", command=self.submit, font=('Helvetica', "18"), bg='#d92d33', fg='#c6c6c4')
        self.submit.place(relx=0.102, rely=0.355)

        self.quick=Label(self, text='Quickest Path:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.quick.place(relx=0.1, rely=0.45)
        self.quickest = StringVar()
        self.quickoutput=Label(self, text=self.quickest.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.quickoutput.place(relx=0.2, rely=0.45)

        self.quicktime=Label(self, text='Time:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.quicktime.place(relx=0.1, rely=0.5)

        self.quickestTime = StringVar()
        self.quicktimeoutput=Label(self, text=self.quickestTime.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.quicktimeoutput.place(relx=0.2, rely=0.5)

        self.cheapest=Label(self, text='Fittest Path:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.cheapest.place(relx=0.1, rely=0.6)

        self.cheap = StringVar()
        self.cheapestoutput=Label(self, text=self.cheap.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.cheapestoutput.place(relx=0.2, rely=0.6)

        self.cheapcost=Label(self, text='Cost:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.cheapcost.place(relx=0.1, rely=0.65)
        self.cheapOutput = StringVar()
        self.cheapcostoutput=Label(self, text=self.cheapOutput.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.cheapcostoutput.place(relx=0.2, rely=0.65)

        self.middlest=Label(self, text='Average Path:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.middlest.place(relx=0.1, rely=0.75)

        self.middle=StringVar()
        self.middlestOutput=Label(self, text=self.middle.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.middlestOutput.place(relx=0.2, rely=0.75)

        self.middleCost=Label(self, text='Cost:', font=('Helvetica', "12"), fg='#d92d33', bg='#c6c6c4')
        self.middleCost.place(relx=0.1, rely=0.8)
        self.middleOutputCost=StringVar()
        self.middleOutput=Label(self, text=self.middleOutputCost.get(), font=('Helvetica', "12"), fg='#443266', bg='#c6c6c4')
        self.middleOutput.place(relx=0.2, rely=0.8)

        self.frame=Frame(self, width=340, height=260, bg="#d92d33")
        self.frame.place(relx=0.665, rely=0.35)

        self.legendHead=Label(self.frame, text="Legend:", font=("Helvetica", "12"), bg="#d92d33", fg="#c6c6c4")
        self.legendHead.place(relx=0.05, rely=0.05)

        temp=Label(self.frame, text="Time", font=("Helvetica", "12"), bg="#d92d33", fg="#c6c6c4")
        temp.place(relx=0.4, rely=0.2)

        temp=Label(self.frame, text="Cost", font=("Helvetica", "12"), bg="#d92d33", fg="#c6c6c4")
        temp.place(relx=0.75, rely=0.2)

        temp=Label(self.frame, text="Bike", font=("Helvetica", "12"), bg="#d92d33", fg="#c6c6c4")
        temp.place(relx=0.1, rely=0.35)

        temp=Label(self.frame, text="100", font=("Helvetica", "12"), bg="#d92d33")
        temp.place(relx=0.4, rely=0.35)

        temp=Label(self.frame, text="0", font=("Helvetica", "12"), bg="#d92d33")
        temp.place(relx=0.75, rely=0.35)

        temp=Label(self.frame, text="Taxi", font=("Helvetica", "12"), bg="#d92d33", fg="#c6c6c4")
        temp.place(relx=0.1, rely=0.5)

        temp=Label(self.frame, text="30", font=("Helvetica", "12"), bg="#d92d33")
        temp.place(relx=0.4, rely=0.5)

        temp=Label(self.frame, text="40", font=("Helvetica", "12"), bg="#d92d33")
        temp.place(relx=0.75, rely=0.5)

        temp=Label(self.frame, text="Train", font=("Helvetica", "12"), bg="#d92d33", fg="#c6c6c4")
        temp.place(relx=0.1, rely=0.65)

        temp=Label(self.frame, text="20", font=("Helvetica", "12"), bg="#d92d33")
        temp.place(relx=0.4, rely=0.65)

        temp=Label(self.frame, text="20", font=("Helvetica", "12"), bg="#d92d33")
        temp.place(relx=0.75, rely=0.65)

        temp=Label(self.frame, text="Note: trains are only available on certain segments,", font=("Helvetica", "10"), bg="#d92d33")
        temp.place(relx=0.05, rely=0.8)

        temp=Label(self.frame, text="those in the map not colored red.", font=("Helvetica", "10"), bg="#d92d33")
        temp.place(relx=0.05, rely=0.87)

        self.photo1=PhotoImage(file='E1.pbm')
        self.pic1=Label(self, image=self.photo1, bd=0)
        self.pic1.bind("<1>", lambda event:self.set(1))
        self.pic1.place(rely=0.1465, relx=0.3937)

        self.photo2=PhotoImage(file='E2.pbm')
        self.pic2=Label(self, image=self.photo2, bd=0)
        self.pic2.bind("<1>", lambda event:self.set(2))
        self.pic2.place(rely=0.206, relx=0.427)

        self.photo3=PhotoImage(file='E3.pbm')
        self.pic3=Label(self, image=self.photo3, bd=0)
        self.pic3.bind("<1>", lambda event:self.set(3))
        self.pic3.place(rely=0.1675, relx=0.4523)

        self.photo4=PhotoImage(file='E4.pbm')
        self.pic4=Label(self, image=self.photo4, bd=0)
        self.pic4.bind("<1>", lambda event:self.set(4))
        self.pic4.place(rely=0.205, relx=0.463)

        self.photo5=PhotoImage(file='E5.pbm')
        self.pic5=Label(self, image=self.photo5, bd=0)
        self.pic5.bind("<1>", lambda event:self.set(5))
        self.pic5.place(rely=0.135, relx=0.487)

        self.photo6=PhotoImage(file='E6.pbm')
        self.pic6=Label(self, image=self.photo6, bd=0)
        self.pic6.bind("<1>", lambda event:self.set(6))
        self.pic6.place(rely=0.081, relx=0.52)

        self.photo7=PhotoImage(file='E7.pbm')
        self.pic7=Label(self, image=self.photo7, bd=0)
        self.pic7.bind("<1>", lambda event:self.set(7))
        self.pic7.place(rely=0.23, relx=0.421)

        self.photo8=PhotoImage(file='E8.pbm')
        self.pic8=Label(self, image=self.photo8, bd=0)
        self.pic8.bind("<1>", lambda event:self.set(8))
        self.pic8.place(rely=0.231, relx=0.45799)

        self.photo9=PhotoImage(file='E9.pbm')
        self.pic9=Label(self, image=self.photo9, bd=0)
        self.pic9.bind("<1>", lambda event:self.set(9))
        self.pic9.place(rely=0.2349, relx=0.4671)

        self.photo10=PhotoImage(file='E10.pbm')
        self.pic10=Label(self, image=self.photo10, bd=0)
        self.pic10.bind("<1>", lambda event:self.set(10))
        self.pic10.place(rely=0.273, relx=0.484)

        self.photo11=PhotoImage(file='E11.pbm')
        self.pic11=Label(self, image=self.photo11, bd=0)
        self.pic11.bind("<1>", lambda event:self.set(11))
        self.pic11.place(rely=0.235, relx=0.495)

        self.photo12=PhotoImage(file='E12.pbm')
        self.pic12=Label(self, image=self.photo12, bd=0)
        self.pic12.bind("<1>", lambda event:self.set(12))
        self.pic12.place(rely=0.249, relx=0.505)

        self.photo13a=PhotoImage(file='E13a.pbm')
        self.pic13a=Label(self, image=self.photo13a, bd=0)
        self.pic13a.bind("<1>", lambda event:self.set(13))
        self.pic13a.place(rely=0.15, relx=0.517)

        self.photo13b=PhotoImage(file='E13b.pbm')
        self.pic13b=Label(self, image=self.photo13b, bd=0)
        self.pic13b.bind("<1>", lambda event:self.set(13))
        self.pic13b.place(rely=0.22, relx=0.548)

        self.photo14=PhotoImage(file='E14.pbm')
        self.pic14=Label(self, image=self.photo14, bd=0)
        self.pic14.bind("<1>", lambda event:self.set(14))
        self.pic14.place(rely=0.2799, relx=0.4479)

        self.photo15=PhotoImage(file='E15.pbm')
        self.pic15=Label(self, image=self.photo15, bd=0)
        self.pic15.bind("<1>", lambda event:self.set(15))
        self.pic15.place(rely=0.29, relx=0.4)

        self.photo16=PhotoImage(file='E16.pbm')
        self.pic16=Label(self, image=self.photo16, bd=0)
        self.pic16.bind("<1>", lambda event:self.set(16))
        self.pic16.place(rely=0.3, relx=0.4419)

        self.photo17=PhotoImage(file='E17.pbm')
        self.pic17=Label(self, image=self.photo17, bd=0)
        self.pic17.bind("<1>", lambda event:self.set(17))
        self.pic17.place(rely=0.3092, relx=0.431)

        self.photo18=PhotoImage(file='E18.pbm')
        self.pic18=Label(self, image=self.photo18, bd=0)
        self.pic18.bind("<1>", lambda event:self.set(18))
        self.pic18.place(rely=0.299, relx=0.458)

        self.photo19=PhotoImage(file='E19.pbm')
        self.pic19=Label(self, image=self.photo19, bd=0)
        self.pic19.bind("<1>", lambda event:self.set(19))
        self.pic19.place(rely=0.2995, relx=0.4886)

        self.photo20=PhotoImage(file='E20.pbm')
        self.pic20=Label(self, image=self.photo20, bd=0)
        self.pic20.bind("<1>", lambda event:self.set(20))
        self.pic20.place(rely=0.289, relx=0.506)

        self.photo21=PhotoImage(file='E21.pbm')
        self.pic21=Label(self, image=self.photo21, bd=0)
        self.pic21.bind("<1>", lambda event:self.set(21))
        self.pic21.place(rely=0.291, relx=0.543)

        self.photo22a=PhotoImage(file='E22a.pbm')
        self.pic22a=Label(self, image=self.photo22a, bd=0)
        self.pic22a.bind("<1>", lambda event:self.set(22))
        self.pic22a.place(rely=0.333, relx=0.465)

        self.photo22b=PhotoImage(file='E22b.pbm')
        self.pic22b=Label(self, image=self.photo22b, bd=0)
        self.pic22b.bind("<1>", lambda event:self.set(22))
        self.pic22b.place(rely=0.3648, relx=0.445)

        self.photo22c=PhotoImage(file='E22c.pbm')
        self.pic22c=Label(self, image=self.photo22c, bd=0)
        self.pic22c.bind("<1>", lambda event:self.set(22))
        self.pic22c.place(rely=0.392, relx=0.443)

        self.photo23=PhotoImage(file='E23.pbm')
        self.pic23=Label(self, image=self.photo23, bd=0)
        self.pic23.bind("<1>", lambda event:self.set(23))
        self.pic23.place(rely=0.38, relx=0.552)

        self.photo24=PhotoImage(file='E24.pbm')
        self.pic24=Label(self, image=self.photo24, bd=0)
        self.pic24.bind("<1>", lambda event:self.set(24))
        self.pic24.place(rely=0.37, relx=0.503)

        self.photo25=PhotoImage(file='E25.pbm')
        self.pic25=Label(self, image=self.photo25, bd=0)
        self.pic25.bind("<1>", lambda event:self.set(25))
        self.pic25.place(rely=0.337, relx=0.506)

        self.photo26=PhotoImage(file='E26.pbm')
        self.pic26=Label(self, image=self.photo26, bd=0)
        self.pic26.bind("<1>", lambda event:self.set(26))
        self.pic26.place(rely=0.337, relx=0.522)

        self.photo27=PhotoImage(file='E27.pbm')
        self.pic27=Label(self, image=self.photo27, bd=0)
        self.pic27.bind("<1>", lambda event:self.set(27))
        self.pic27.place(rely=0.346, relx=0.553)

        self.photo28=PhotoImage(file='E28.pbm')
        self.pic28=Label(self, image=self.photo28, bd=0)
        self.pic28.bind("<1>", lambda event:self.set(28))
        self.pic28.place(rely=0.357, relx=0.538)

        self.photo29=PhotoImage(file='E29.pbm')
        self.pic29=Label(self, image=self.photo29, bd=0)
        self.pic29.bind("<1>", lambda event:self.set(29))
        self.pic29.place(rely=0.3637, relx=0.56788)

        self.photo30a=PhotoImage(file='E30a.pbm')
        self.pic30a=Label(self, image=self.photo30a, bd=0)
        self.pic30a.bind("<1>", lambda event:self.set(30))
        self.pic30a.place(rely=0.4148, relx=0.446)
        
        self.photo30b=PhotoImage(file='E30b.pbm')
        self.pic30b=Label(self, image=self.photo30b, bd=0)
        self.pic30b.bind("<1>", lambda event:self.set(30))
        self.pic30b.place(rely=0.393, relx=0.466)

        self.photo31=PhotoImage(file='E31.pbm')
        self.pic31=Label(self, image=self.photo31, bd=0)
        self.pic31.bind("<1>", lambda event:self.set(31))
        self.pic31.place(rely=0.3995, relx=0.5)

        self.photo32=PhotoImage(file='E32.pbm')
        self.pic32=Label(self, image=self.photo32, bd=0)
        self.pic32.bind("<1>", lambda event:self.set(32))
        self.pic32.place(rely=0.385, relx=0.521)

        self.photo33=PhotoImage(file='E33.pbm')
        self.pic33=Label(self, image=self.photo33, bd=0)
        self.pic33.bind("<1>", lambda event:self.set(33))
        self.pic33.place(rely=0.424, relx=0.4325)

        self.photo34=PhotoImage(file='E34.pbm')
        self.pic34=Label(self, image=self.photo34, bd=0)
        self.pic34.bind("<1>", lambda event:self.set(34))
        self.pic34.place(rely=0.403, relx=0.546)

        self.photo35=PhotoImage(file='E35.pbm')
        self.pic35=Label(self, image=self.photo35, bd=0)
        self.pic35.bind("<1>", lambda event:self.set(35))
        self.pic35.place(rely=0.4394, relx=0.5342)

        self.photo36=PhotoImage(file='E36.pbm')
        self.pic36=Label(self, image=self.photo36, bd=0)
        self.pic36.bind("<1>", lambda event:self.set(36))
        self.pic36.place(rely=0.43, relx=0.559)

        self.photo37=PhotoImage(file='E37.pbm')
        self.pic37=Label(self, image=self.photo37, bd=0)
        self.pic37.bind("<1>", lambda event:self.set(37))
        self.pic37.place(rely=0.52, relx=0.444)

        self.photo38a=PhotoImage(file='E38a.pbm')
        self.pic38a=Label(self, image=self.photo38a, bd=0)
        self.pic38a.bind("<1>", lambda event:self.set(38))
        self.pic38a.place(rely=0.445, relx=0.515)

        self.photo38b=PhotoImage(file='E38b.pbm')
        self.pic38b=Label(self, image=self.photo38b, bd=0)
        self.pic38b.bind("<1>", lambda event:self.set(38))
        self.pic38b.place(rely=0.474, relx=0.483)

        self.photo38c=PhotoImage(file='E38c.pbm')
        self.pic38c=Label(self, image=self.photo38c, bd=0)
        self.pic38c.bind("<1>", lambda event:self.set(38))
        self.pic38c.place(rely=0.5491, relx=0.4723)

        self.photo39=PhotoImage(file='E39.pbm')
        self.pic39=Label(self, image=self.photo39, bd=0)
        self.pic39.bind("<1>", lambda event:self.set(39))
        self.pic39.place(rely=0.51, relx=0.461)

        self.photo40=PhotoImage(file='E40.pbm')
        self.pic40=Label(self, image=self.photo40, bd=0)
        self.pic40.bind("<1>", lambda event:self.set(40))
        self.pic40.place(rely=0.555, relx=0.435)

        self.photo41=PhotoImage(file='E41.pbm')
        self.pic41=Label(self, image=self.photo41, bd=0)
        self.pic41.bind("<1>", lambda event:self.set(41))
        self.pic41.place(rely=0.566, relx=0.459)

        self.photo42=PhotoImage(file='E42.pbm')
        self.pic42=Label(self, image=self.photo42, bd=0)
        self.pic42.bind("<1>", lambda event:self.set(42))
        self.pic42.place(rely=0.571, relx=0.471)

        self.photo43a=PhotoImage(file='E43a.pbm')
        self.pic43a=Label(self, image=self.photo43a, bd=0)
        self.pic43a.bind("<1>", lambda event:self.set(43))
        self.pic43a.place(rely=0.58, relx=0.494)

        self.photo43b=PhotoImage(file='E43b.pbm')
        self.pic43b=Label(self, image=self.photo43b, bd=0)
        self.pic43b.bind("<1>", lambda event:self.set(43))
        self.pic43b.place(rely=0.53, relx=0.516)

        self.photo44=PhotoImage(file='E44.pbm')
        self.pic44=Label(self, image=self.photo44, bd=0)
        self.pic44.bind("<1>", lambda event:self.set(44))
        self.pic44.place(rely=0.592, relx=0.433)

        self.photo45a=PhotoImage(file='E45a.pbm')
        self.pic45a=Label(self, image=self.photo45a, bd=0)
        self.pic45a.bind("<1>", lambda event:self.set(45))
        self.pic45a.place(rely=0.63, relx=0.457)

        self.photo45b=PhotoImage(file='E45b.pbm')
        self.pic45b=Label(self, image=self.photo45b, bd=0)
        self.pic45b.bind("<1>", lambda event:self.set(45))
        self.pic45b.place(rely=0.674, relx=0.4195)

        self.photo46=PhotoImage(file='E46.pbm')
        self.pic46=Label(self, image=self.photo46, bd=0)
        self.pic46.bind("<1>", lambda event:self.set(46))
        self.pic46.place(rely=0.642, relx=0.492)
        
        self.photo47=PhotoImage(file='E47.pbm')
        self.pic47=Label(self, image=self.photo47, bd=0)
        self.pic47.bind("<1>", lambda event:self.set(47))
        self.pic47.place(rely=0.81, relx=0.483)
        
        self.photo48=PhotoImage(file='E48.pbm')
        self.pic48=Label(self, image=self.photo48, bd=0)
        self.pic48.bind("<1>", lambda event:self.set(48))
        self.pic48.place(rely=0.801, relx=0.504)

    def set(self, temp):
        if self.startVar.get() == "":
            self.startVar.set(temp)
            self.startinput.configure(text=self.startVar.get())
        else:
            self.endVar.set(temp)
            self.endinput.configure(text=self.endVar.get())

    def clearStart(self):
        self.startVar.set("")
        self.startinput.configure(text=self.startVar.get())

    def clearEnd(self):
        self.endVar.set("")
        self.endinput.configure(text=self.endVar.get())

    def submit(self):
        a = A_star()
        b = code()
        b.set_start(self.startVar.get())
        b.set_end(self.endVar.get())

        x, y = a.algorithm(b.get_start(), b.get_end(), b, 0, None)
        self.cheap.set(y)
        self.cheapestoutput.configure(text=self.cheap.get())
        self.cheapOutput.set(str(x) + " minutes")
        self.cheapcostoutput.configure(text=self.cheapOutput.get())

        a = A_star()
        x, y = a.algorithm(b.get_start(), b.get_end(), b, 1, None)
        self.quickest.set(y)
        self.quickoutput.configure(text=self.quickest.get())
        self.quickestTime.set(str(x) + " minutes")
        self.quicktimeoutput.configure(text=self.quickestTime.get())

        a = A_star()
        x, y = a.algorithm(b.get_start(), b.get_end(), b, 2, None)
        self.middle.set(y)
        self.middlestOutput.configure(text=self.middle.get())
        self.middleOutputCost.set(str(x) + " pesos per minute")
        self.middleOutput.configure(text=self.middleOutputCost.get())

g=GUI(None)
g.main()
g.mainloop()
