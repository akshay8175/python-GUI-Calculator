import sys
import tkinter as tk
import tkinter.ttk as ttk
from math import *
import sci_calci_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Sci_Calc (root)
    sci_calci_support.init(root, top)
    root.mainloop()

class Sci_Calc:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
       
        
        top.geometry("510x279+503+280")
        
        top.resizable(False,False)
        top.title("Calculator")
        top.configure(background="#e0e4ff")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                hidemargin=1,
                label="View")
        self.sub_menu.add_radiobutton(
                value="NewRadio",
                
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                command=self.calc,
                font="TkMenuFont",
                foreground="#000000",
                label="Standard")
        self.sub_menu.add_radiobutton(
                value="NewRadio",
                
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Scientific")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Edit")
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Help")

        self.equation = tk.StringVar()

        self.e = tk.Entry(top)
        self.e.place(relx=0.02, rely=0.036,height=60, relwidth=0.949)
        self.e.configure(background="#ebfffe")
        self.e.configure(disabledforeground="#a3a3a3")
        self.e.configure(exportselection="0")
        self.e.configure(font="TkFixedFont")
        self.e.configure(foreground="#000000")
        self.e.configure(highlightbackground="#b5b5b5")
        self.e.configure(highlightthickness="1")
        self.e.configure(insertbackground="black")
        self.e.configure(readonlybackground="#efefef")
        self.e.configure(justify='right')
        self.e.configure(relief="flat")
        self.e.configure(textvariable=self.equation)
        self.e.configure(width=484)

        self.TButton = ttk.Button(top)
        self.TButton.place(relx=0.02, rely=0.287, height=35, width=36)
        self.TButton.configure(takefocus="")
        self.TButton.configure(command=lambda: self.press(","))
        self.TButton.configure(text=''' , ''')
        self.TButton.configure(width=36)
        self.TButton.configure(compound='center')

        self.TButtonInt = ttk.Button(top)
        self.TButtonInt.place(relx=0.02, rely=0.43, height=35, width=36)
        self.TButtonInt.configure(takefocus="")
        self.TButtonInt.configure(text='''Int''')

        self.TButtondms = ttk.Button(top)
        self.TButtondms.place(relx=0.02, rely=0.573, height=35, width=36)
        self.TButtondms.configure(takefocus="")
        self.TButtondms.configure(text='''dms''')

        self.TButtonPi = ttk.Button(top)
        self.TButtonPi.place(relx=0.02, rely=0.717, height=35, width=36)
        self.TButtonPi.configure(takefocus="")
        self.TButtonPi.configure(command=lambda: self.press("3.14"))
        self.TButtonPi.configure(text='''Pi''')

        self.TButtonFE = ttk.Button(top)
        self.TButtonFE.place(relx=0.02, rely=0.86, height=35, width=36)
        self.TButtonFE.configure(takefocus="")
        self.TButtonFE.configure(text='''F-E''')

        self.TButtonInv = ttk.Button(top)
        self.TButtonInv.place(relx=0.098, rely=0.287, height=35, width=36)
        self.TButtonInv.configure(takefocus="")
        self.TButtonInv.configure(text='''Inv''')
        self.TButtonInv.configure(compound='center')

        self.TButtonIn = ttk.Button(top)
        self.TButtonIn.place(relx=0.176, rely=0.287, height=35, width=36)
        self.TButtonIn.configure(takefocus="")
        self.TButtonIn.configure(command=lambda: self.press("log10("))
        self.TButtonIn.configure(text='''log10''')
        self.TButtonIn.configure(compound='center')

        self.TButtonbrac = ttk.Button(top)
        self.TButtonbrac.place(relx=0.255, rely=0.287, height=35, width=36)
        self.TButtonbrac.configure(takefocus="")
        self.TButtonbrac.configure(command=lambda: self.press("("))
        self.TButtonbrac.configure(text='''(''')
        self.TButtonbrac.configure(compound='center')

        self.TButton1brac = ttk.Button(top)
        self.TButton1brac.place(relx=0.333, rely=0.287, height=35, width=46)
        self.TButton1brac.configure(takefocus="")
        self.TButton1brac.configure(command=lambda: self.press(")"))
        self.TButton1brac.configure(text=''')''')
        self.TButton1brac.configure(width=46)
        self.TButton1brac.configure(compound='center')

        self.TButtonMC = ttk.Button(top)
        self.TButtonMC.place(relx=0.431, rely=0.287, height=35, width=36)
        self.TButtonMC.configure(takefocus="")
        self.TButtonMC.configure(text='''MC''')
        self.TButtonMC.configure(compound='center')

        self.TButtonROOT = ttk.Button(top)
        self.TButtonROOT.place(relx=0.902, rely=0.287, height=35, width=36)
        self.TButtonROOT.configure(takefocus="")
        self.TButtonROOT.configure(command=lambda: self.press("sqrt()"))
        self.TButtonROOT.configure(text='''Sqrt''')
        self.TButtonROOT.configure(compound='center')

        self.TButtonps = ttk.Button(top)
        self.TButtonps.place(relx=0.824, rely=0.287, height=35, width=36)
        self.TButtonps.configure(takefocus="")
        self.TButtonps.configure(command=lambda: self.press("+/-"))
        self.TButtonps.configure(text='''+/-''')
        self.TButtonps.configure(compound='center')

        self.TButtonsinh = ttk.Button(top)
        self.TButtonsinh.place(relx=0.098, rely=0.43, height=35, width=36)
        self.TButtonsinh.configure(takefocus="")
        self.TButtonsinh.configure(command=lambda: self.press("sinh("))
        self.TButtonsinh.configure(text='''sinh''')
        self.TButtonsinh.configure(compound='center')

        self.TButtonC = ttk.Button(top)
        self.TButtonC.place(relx=0.745, rely=0.287, height=35, width=36)
        self.TButtonC.configure(takefocus="")
        self.TButtonC.configure(command=self.clear)
        self.TButtonC.configure(text='''C''')
        self.TButtonC.configure(compound='center')

        self.TButtonD = ttk.Button(top)
        self.TButtonD.place(relx=0.588, rely=0.287, height=35, width=76)
        self.TButtonD.configure(takefocus="")
        self.TButtonD.configure(text='''Delete''')
        self.TButtonD.configure(width=76)
        self.TButtonD.configure(compound='center')

        self.TButtonMR = ttk.Button(top)
        self.TButtonMR.place(relx=0.431, rely=0.43, height=35, width=36)
        self.TButtonMR.configure(takefocus="")
        self.TButtonMR.configure(text='''MR''')
        self.TButtonMR.configure(compound='center')

        self.TButtonn = ttk.Button(top)
        self.TButtonn.place(relx=0.333, rely=0.43, height=35, width=46)
        self.TButtonn.configure(takefocus="")
        self.TButtonn.configure(command=lambda: self.press("factorial("))
        self.TButtonn.configure(text='''n!''')
        self.TButtonn.configure(width=46)
        self.TButtonn.configure(compound='center')

        self.TButtonx2 = ttk.Button(top)
        self.TButtonx2.place(relx=0.255, rely=0.43, height=35, width=36)
        self.TButtonx2.configure(takefocus="")
        self.TButtonx2.configure(command=lambda: self.press("**"))
        self.TButtonx2.configure(text='''x^2''')
        self.TButtonx2.configure(compound='center')

        self.TButtonsin = ttk.Button(top)
        self.TButtonsin.place(relx=0.176, rely=0.43, height=35, width=36)
        self.TButtonsin.configure(takefocus="")
        self.TButtonsin.configure(command=lambda: self.press("sin("))
        self.TButtonsin.configure(text='''sin''')
        self.TButtonsin.configure(compound='center')

        self.TButtonMS = ttk.Button(top)
        self.TButtonMS.place(relx=0.431, rely=0.573, height=35, width=36)
        self.TButtonMS.configure(takefocus="")
        self.TButtonMS.configure(text='''MS''')
        self.TButtonMS.configure(compound='center')

        self.TButtonx1y = ttk.Button(top)
        self.TButtonx1y.place(relx=0.333, rely=0.573, height=35, width=46)
        self.TButtonx1y.configure(takefocus="")
        self.TButtonx1y.configure(command=lambda: self.press("pow("))
        self.TButtonx1y.configure(text='''x^1/y''')
        self.TButtonx1y.configure(width=46)
        self.TButtonx1y.configure(compound='center')

        self.TButtonxy = ttk.Button(top)
        self.TButtonxy.place(relx=0.255, rely=0.573, height=35, width=36)
        self.TButtonxy.configure(takefocus="")
        self.TButtonxy.configure(command=lambda: self.press("pow("))
        self.TButtonxy.configure(text='''x^y''')
        self.TButtonxy.configure(compound='center')

        self.TButtoncos = ttk.Button(top)
        self.TButtoncos.place(relx=0.176, rely=0.573, height=35, width=36)
        self.TButtoncos.configure(takefocus="")
        self.TButtoncos.configure(command=lambda: self.press("cos("))
        self.TButtoncos.configure(text='''cos''')
        self.TButtoncos.configure(compound='center')

        self.TButtoncosh = ttk.Button(top)
        self.TButtoncosh.place(relx=0.098, rely=0.573, height=35, width=36)
        self.TButtoncosh.configure(takefocus="")
        self.TButtoncosh.configure(command=lambda: self.press("cosh("))
        self.TButtoncosh.configure(text='''cosh''')
        self.TButtoncosh.configure(compound='center')

        self.TButtonmp = ttk.Button(top)
        self.TButtonmp.place(relx=0.431, rely=0.717, height=35, width=36)
        self.TButtonmp.configure(takefocus="")
        self.TButtonmp.configure(text='''M+''')
        self.TButtonmp.configure(compound='center')

        self.TButtonx13 = ttk.Button(top)
        self.TButtonx13.place(relx=0.333, rely=0.717, height=35, width=46)
        self.TButtonx13.configure(takefocus="")
        self.TButtonx13.configure(command=lambda: self.press("pow("))
        self.TButtonx13.configure(text='''x^1/3''')
        self.TButtonx13.configure(width=46)
        self.TButtonx13.configure(compound='center')

        self.TButtonx3 = ttk.Button(top)
        self.TButtonx3.place(relx=0.255, rely=0.717, height=35, width=36)
        self.TButtonx3.configure(takefocus="")
        self.TButtonx3.configure(command=lambda: self.press("**3"))
        self.TButtonx3.configure(text='''x^3''')
        self.TButtonx3.configure(compound='center')

        self.TButtontan = ttk.Button(top)
        self.TButtontan.place(relx=0.176, rely=0.717, height=35, width=36)
        self.TButtontan.configure(takefocus="")
        self.TButtontan.configure(command=lambda: self.press("tan("))
        self.TButtontan.configure(text='''tan''')
        self.TButtontan.configure(compound='center')

        self.TButtontanh = ttk.Button(top)
        self.TButtontanh.place(relx=0.098, rely=0.717, height=35, width=36)
        self.TButtontanh.configure(takefocus="")
        self.TButtontanh.configure(command=lambda: self.press("tanh("))
        self.TButtontanh.configure(text='''tanh''')
        self.TButtontanh.configure(compound='center')

        self.TButton7 = ttk.Button(top)
        self.TButton7.place(relx=0.588, rely=0.43, height=35, width=36)
        self.TButton7.configure(takefocus="")
        self.TButton7.configure(command=lambda: self.press(7))
        self.TButton7.configure(text='''7''')
        self.TButton7.configure(compound='center')

        self.TButton8 = ttk.Button(top)
        self.TButton8.place(relx=0.667, rely=0.43, height=35, width=36)
        self.TButton8.configure(takefocus="")
        self.TButton8.configure(command=lambda: self.press(8))
        self.TButton8.configure(text='''8''')
        self.TButton8.configure(compound='center')

        self.TButton9 = ttk.Button(top)
        self.TButton9.place(relx=0.745, rely=0.43, height=35, width=36)
        self.TButton9.configure(takefocus="")
        self.TButton9.configure(command=lambda: self.press(9))
        self.TButton9.configure(text='''9''')
        self.TButton9.configure(compound='center')

        self.TButtondiv = ttk.Button(top)
        self.TButtondiv.place(relx=0.824, rely=0.43, height=35, width=36)
        self.TButtondiv.configure(takefocus="")
        self.TButtondiv.configure(command=lambda: self.press("/"))
        self.TButtondiv.configure(text='''/''')
        self.TButtondiv.configure(compound='center')

        self.TButtonper = ttk.Button(top)
        self.TButtonper.place(relx=0.902, rely=0.43, height=35, width=36)
        self.TButtonper.configure(takefocus="")
        self.TButtonper.configure(command=lambda: self.press("%"))
        self.TButtonper.configure(text='''%''')
        self.TButtonper.configure(compound='center')

        self.TButtonms = ttk.Button(top)
        self.TButtonms.place(relx=0.431, rely=0.86, height=35, width=36)
        self.TButtonms.configure(takefocus="")
        self.TButtonms.configure(text='''M-''')
        self.TButtonms.configure(compound='center')

        self.TButton1_16 = ttk.Button(top)
        self.TButton1_16.place(relx=0.333, rely=0.86, height=35, width=46)
        self.TButton1_16.configure(takefocus="")
        self.TButton1_16.configure(command=lambda: self.press("pow(10,"))
        self.TButton1_16.configure(text='''10^x''')
        self.TButton1_16.configure(width=46)
        self.TButton1_16.configure(compound='center')

        self.TButtonlog = ttk.Button(top)
        self.TButtonlog.place(relx=0.255, rely=0.86, height=35, width=36)
        self.TButtonlog.configure(takefocus="")
        self.TButtonlog.configure(command=lambda: self.press("log("))
        self.TButtonlog.configure(text='''log''')
        self.TButtonlog.configure(compound='center')

        self.TButtonmod = ttk.Button(top)
        self.TButtonmod.place(relx=0.176, rely=0.86, height=35, width=36)
        self.TButtonmod.configure(takefocus="")
        self.TButtonmod.configure(command=lambda: self.press("fmod("))
        self.TButtonmod.configure(text='''Mod''')
        self.TButtonmod.configure(compound='center')

        self.TButtonexp = ttk.Button(top)
        self.TButtonexp.place(relx=0.098, rely=0.86, height=35, width=36)
        self.TButtonexp.configure(takefocus="")
        self.TButtonexp.configure(command=lambda: self.press("exp("))
        self.TButtonexp.configure(text='''Exp''')
        self.TButtonexp.configure(compound='center')

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.745, rely=0.717, height=35, width=36)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(command=lambda: self.press(3))
        self.TButton3.configure(text='''3''')
        self.TButton3.configure(compound='center')

        self.TButtonm = ttk.Button(top)
        self.TButtonm.place(relx=0.824, rely=0.573, height=35, width=36)
        self.TButtonm.configure(takefocus="")
        self.TButtonm.configure(command=lambda: self.press("*"))
        self.TButtonm.configure(text='''*''')
        self.TButtonm.configure(compound='center')

        self.TButtons = ttk.Button(top)
        self.TButtons.place(relx=0.824, rely=0.717, height=35, width=36)
        self.TButtons.configure(takefocus="")
        self.TButtons.configure(command=lambda: self.press("-"))
        self.TButtons.configure(text='''-''')
        self.TButtons.configure(compound='center')

        self.TButton6 = ttk.Button(top)
        self.TButton6.place(relx=0.745, rely=0.573, height=35, width=36)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(command=lambda: self.press(6))
        self.TButton6.configure(text='''6''')
        self.TButton6.configure(compound='center')

        self.TButton0 = ttk.Button(top)
        self.TButton0.place(relx=0.588, rely=0.86, height=35, width=76)
        self.TButton0.configure(takefocus="")
        self.TButton0.configure(command=lambda: self.press(0))
        self.TButton0.configure(text='''0''')
        self.TButton0.configure(width=76)
        self.TButton0.configure(compound='center')

        self.TButtondot = ttk.Button(top)
        self.TButtondot.place(relx=0.745, rely=0.86, height=35, width=36)
        self.TButtondot.configure(takefocus="")
        self.TButtondot.configure(command=lambda: self.press("."))
        self.TButtondot.configure(text='''.''')
        self.TButtondot.configure(compound='center')

        self.TButtonp = ttk.Button(top)
        self.TButtonp.place(relx=0.824, rely=0.86, height=35, width=36)
        self.TButtonp.configure(takefocus="")
        self.TButtonp.configure(command=lambda: self.press("+"))
        self.TButtonp.configure(text='''+''')
        self.TButtonp.configure(compound='center')

        self.TButton5 = ttk.Button(top)
        self.TButton5.place(relx=0.667, rely=0.573, height=35, width=36)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(command=lambda: self.press(5))
        self.TButton5.configure(text='''5''')
        self.TButton5.configure(compound='center')

        self.TButtoneq = ttk.Button(top)
        self.TButtoneq.place(relx=0.902, rely=0.717, height=75, width=36)
        self.TButtoneq.configure(takefocus="")
        self.TButtoneq.configure(command=self.equalpress)
        self.TButtoneq.configure(text='''=''')
        self.TButtoneq.configure(width=36)
        self.TButtoneq.configure(compound='center')

        self.TButton1_17 = ttk.Button(top)
        self.TButton1_17.place(relx=0.902, rely=0.573, height=35, width=36)
        self.TButton1_17.configure(takefocus="")
        self.TButton1_17.configure(command=lambda: self.press('1/'))
        self.TButton1_17.configure(text='''1/x''')
        self.TButton1_17.configure(compound='center')

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.588, rely=0.573, height=35, width=36)
        self.TButton4.configure(command=lambda: self.press(4))
        self.TButton4.configure(text='''4''')
        self.TButton4.configure(compound='center')

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.588, rely=0.717, height=35, width=36)
        self.TButton1.configure(command=lambda: self.press(1))
        self.TButton1.configure(text='''1''')
        self.TButton1.configure(compound='center')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.667, rely=0.717, height=35, width=36)
        self.TButton2.configure(command=lambda: self.press(2))       
        self.TButton2.configure(text='''2''')
        self.TButton2.configure(compound='center')

        #  declare the expression variable 
        self.expression = ""
    



    
     


    # Function to update expressiom 
    # in the text entry box 
    def press(self,num): 
        # point out the global expression variable 
        
            
        # concatenation of string 
        self.expression = self.expression + str(num) 

        # update the expression by using set method 
        self.equation.set(self.expression)


    # Function to evaluate the final expression 
    def equalpress(self): 
        # Try and except statement is used 
        # for handling the errors like zero 
        # division error etc. 

        # Put that code inside the try block 
        # which may generate the error 
        try: 

             

            # eval function evaluate the expression 
            # and str function convert the result 
            # into string 
            total = str(eval(self.expression)) 

            self.equation.set(total) 

            # initialze the expression variable 
            # by empty string 
            self.expression = "" 

        # if error is generate then handle 
        # by the except block 
        except: 

            self.equation.set(" error ") 
            self.expression = "" 


    # Function to clear the contents 
    # of text entry box 
    def clear(self): 
         
        self.expression = "" 
        self.equation.set("")        

    def backspace(self):
        pass

    def calc(self):
        sci_calci_support.destroy_window()
        import calculator
        calculator.vp_start_gui() 

if __name__ == '__main__':
    vp_start_gui()        