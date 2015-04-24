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
        self.pic22a.place(rely=0.333, relx=0.465)

        self.photo22b=PhotoImage(file='E22b.pbm')
        self.pic22b=Label(self, image=self.photo22b, bd=0)
        self.pic22b.place(rely=0.3648, relx=0.445)

        self.photo22c=PhotoImage(file='E22c.pbm')
        self.pic22c=Label(self, image=self.photo22c, bd=0)
        self.pic22c.place(rely=0.392, relx=0.443)

        self.photo23=PhotoImage(file='E23.pbm')
        self.pic23=Label(self, image=self.photo23, bd=0)
        self.pic23.place(rely=0.38, relx=0.552)

        self.photo24=PhotoImage(file='E24.pbm')
        self.pic24=Label(self, image=self.photo24, bd=0)
        self.pic24.place(rely=0.37, relx=0.503)

        self.photo25=PhotoImage(file='E25.pbm')
        self.pic25=Label(self, image=self.photo25, bd=0)
        self.pic25.place(rely=0.337, relx=0.506)

        self.photo26=PhotoImage(file='E26.pbm')
        self.pic26=Label(self, image=self.photo26, bd=0)
        self.pic26.place(rely=0.337, relx=0.522)

        self.photo27=PhotoImage(file='E27.pbm')
        self.pic27=Label(self, image=self.photo27, bd=0)
        self.pic27.place(rely=0.346, relx=0.553)

        self.photo28=PhotoImage(file='E28.pbm')
        self.pic28=Label(self, image=self.photo28, bd=0)
        self.pic28.place(rely=0.357, relx=0.538)

        self.photo29=PhotoImage(file='E29.pbm')
        self.pic29=Label(self, image=self.photo29, bd=0)
        self.pic29.place(rely=0.3637, relx=0.56788)

        self.photo30a=PhotoImage(file='E30a.pbm')
        self.pic30a=Label(self, image=self.photo30a, bd=0)
        self.pic30a.place(rely=0.4148, relx=0.446)
        
        self.photo30b=PhotoImage(file='E30b.pbm')
        self.pic30b=Label(self, image=self.photo30b, bd=0)
        self.pic30b.place(rely=0.393, relx=0.466)

        self.photo31=PhotoImage(file='E31.pbm')
        self.pic31=Label(self, image=self.photo31, bd=0)
        self.pic31.place(rely=0.3995, relx=0.5)

        self.photo32=PhotoImage(file='E32.pbm')
        self.pic32=Label(self, image=self.photo32, bd=0)
        self.pic32.place(rely=0.385, relx=0.521)

        self.photo33=PhotoImage(file='E33.pbm')
        self.pic33=Label(self, image=self.photo33, bd=0)
        self.pic33.place(rely=0.424, relx=0.4325)

        self.photo34=PhotoImage(file='E34.pbm')
        self.pic34=Label(self, image=self.photo34, bd=0)
        self.pic34.place(rely=0.403, relx=0.546)

        self.photo35=PhotoImage(file='E35.pbm')
        self.pic35=Label(self, image=self.photo35, bd=0)
        self.pic35.place(rely=0.4394, relx=0.5342)

        self.photo36=PhotoImage(file='E36.pbm')
        self.pic36=Label(self, image=self.photo36, bd=0)
        self.pic36.place(rely=0.43, relx=0.559)

        self.photo37=PhotoImage(file='E37.pbm')
        self.pic37=Label(self, image=self.photo37, bd=0)
        self.pic37.place(rely=0.52, relx=0.444)

        self.photo38a=PhotoImage(file='E38a.pbm')
        self.pic38a=Label(self, image=self.photo38a, bd=0)
        self.pic38a.place(rely=0.445, relx=0.515)

        self.photo38b=PhotoImage(file='E38b.pbm')
        self.pic38b=Label(self, image=self.photo38b, bd=0)
        self.pic38b.place(rely=0.474, relx=0.483)

        self.photo38c=PhotoImage(file='E38c.pbm')
        self.pic38c=Label(self, image=self.photo38c, bd=0)
        self.pic38c.place(rely=0.5491, relx=0.4723)

        self.photo39=PhotoImage(file='E39.pbm')
        self.pic39=Label(self, image=self.photo39, bd=0)
        self.pic39.place(rely=0.51, relx=0.461)

        self.photo40=PhotoImage(file='E40.pbm')
        self.pic40=Label(self, image=self.photo40, bd=0)
        self.pic40.place(rely=0.555, relx=0.435)

        self.photo41=PhotoImage(file='E41.pbm')
        self.pic41=Label(self, image=self.photo41, bd=0)
        self.pic41.place(rely=0.566, relx=0.459)

        self.photo42=PhotoImage(file='E42.pbm')
        self.pic42=Label(self, image=self.photo42, bd=0)
        self.pic42.place(rely=0.571, relx=0.471)

        self.photo43a=PhotoImage(file='E43a.pbm')
        self.pic43a=Label(self, image=self.photo43a, bd=0)
        self.pic43a.place(rely=0.58, relx=0.494)

        self.photo43b=PhotoImage(file='E43b.pbm')
        self.pic43b=Label(self, image=self.photo43b, bd=0)
        self.pic43b.place(rely=0.53, relx=0.516)

        self.photo44=PhotoImage(file='E44.pbm')
        self.pic44=Label(self, image=self.photo44, bd=0)
        self.pic44.place(rely=0.592, relx=0.433)

        self.photo45a=PhotoImage(file='E45a.pbm')
        self.pic45a=Label(self, image=self.photo45a, bd=0)
        self.pic45a.place(rely=0.63, relx=0.457)

        self.photo45b=PhotoImage(file='E45b.pbm')
        self.pic45b=Label(self, image=self.photo45b, bd=0)
        self.pic45b.place(rely=0.674, relx=0.4195)

        self.photo46=PhotoImage(file='E46.pbm')
        self.pic46=Label(self, image=self.photo46, bd=0)
        self.pic46.place(rely=0.642, relx=0.492)
        
        self.photo47=PhotoImage(file='E47.pbm')
        self.pic47=Label(self, image=self.photo47, bd=0)
        self.pic47.place(rely=0.81, relx=0.483)
        
        self.photo48=PhotoImage(file='E48.pbm')
        self.pic48=Label(self, image=self.photo48, bd=0)
        self.pic48.place(rely=0.801, relx=0.504)
g=GUI(None)
g.main()
g.mainloop()