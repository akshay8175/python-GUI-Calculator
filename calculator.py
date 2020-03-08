# -*-coding: utf-8-*-

import sys
import tkinter as tk
import tkinter.ttk as ttk
import calulator_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = View(root)
    calulator_support.init(root, top)
    root.mainloop()



class View:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family Consolas -size 12 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"

        img = tk.PhotoImage(file="icon/icon1.png")
        top.iconphoto(top,img)
        top.geometry("252x312")        
        top.resizable(False,False)
        top.title("Calculator")
        top.configure(background="#e0e4ff")
        top.configure(highlightbackground="#efefef")
        top.configure(highlightcolor="#5c2163")

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
                label="View")
        self.sub_menu.add_radiobutton(
                value="NewRadio",
                
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Standard")
        self.sub_menu.add_radiobutton(
                value="NewRadio",
                
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                command=self.sci_c,
                font="TkMenuFont",
                foreground="#000000",
                label="Scientific")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Edit")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Help")

        self.equation = tk.StringVar()

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.04, rely=0.03,height=60, relwidth=0.929)
        self.Entry1.configure(background="#ebfffe")
        self.Entry1.configure(borderwidth="5")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font9)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#b5b5b5")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(highlightthickness="1")
        self.Entry1.configure(justify='right')
        self.Entry1.configure(relief="flat")
        self.Entry1.configure(width=234)
        self.Entry1.configure(textvariable=self.equation)
        self.Entry1.focus_set()


        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.04, rely=0.342, height=35, width=46)
        self.TButton1.configure(command=lambda: self.press(1))
        self.TButton1.configure(text='''1''')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.238, rely=0.342, height=35, width=46)
        self.TButton2.configure(command=lambda: self.press(2))
        self.TButton2.configure(text='''2''')

        self.TButton1_11 = ttk.Button(top)
        self.TButton1_11.place(relx=0.437, rely=0.342, height=35, width=46)
        self.TButton1_11.configure(command=lambda: self.press(3))
        self.TButton1_11.configure(text='''3''')

        self.TButton1_12 = ttk.Button(top)
        self.TButton1_12.place(relx=0.04, rely=0.479, height=35, width=46)
        self.TButton1_12.configure(command=lambda: self.press(4))
        self.TButton1_12.configure(text='''4''')

        self.TButton1_13 = ttk.Button(top)
        self.TButton1_13.place(relx=0.238, rely=0.479, height=35, width=46)
        self.TButton1_13.configure(command=lambda: self.press(5))
        self.TButton1_13.configure(text='''5''')

        self.TButton1_14 = ttk.Button(top)
        self.TButton1_14.place(relx=0.238, rely=0.616, height=35, width=46)
        self.TButton1_14.configure(command=lambda: self.press(8))
        self.TButton1_14.configure(text='''8''')

        self.TButton1_15 = ttk.Button(top)
        self.TButton1_15.place(relx=0.04, rely=0.616, height=35, width=46)
        self.TButton1_15.configure(command=lambda: self.press(7))
        self.TButton1_15.configure(text='''7''')

        self.TButton1_16 = ttk.Button(top)
        self.TButton1_16.place(relx=0.437, rely=0.479, height=35, width=46)
        self.TButton1_16.configure(command=lambda: self.press(6))
        self.TButton1_16.configure(text='''6''')

        self.TButton1_17 = ttk.Button(top)
        self.TButton1_17.place(relx=0.437, rely=0.616, height=35, width=46)
        self.TButton1_17.configure(command=lambda: self.press(9))
        self.TButton1_17.configure(text='''9''')

        self.TButton1_18 = ttk.Button(top)
        self.TButton1_18.place(relx=0.04, rely=0.753, height=35, width=96)
        self.TButton1_18.configure(command=lambda: self.press(0))
        self.TButton1_18.configure(text='''0''')

        self.TButton1_19 = ttk.Button(top)
        self.TButton1_19.place(relx=0.437, rely=0.753, height=35, width=46)
        self.TButton1_19.configure(command=lambda: self.press("."))
        self.TButton1_19.configure(text='''.''')

        self.TButton1_20 = ttk.Button(top)
        self.TButton1_20.place(relx=0.675, rely=0.342, height=35, width=66)
        self.TButton1_20.configure(command=lambda: self.press("/"))
        self.TButton1_20.configure(text='''/''')

        self.TButton1_21 = ttk.Button(top)
        self.TButton1_21.place(relx=0.675, rely=0.479, height=35, width=66)
        self.TButton1_21.configure(command=lambda: self.press("*"))
        self.TButton1_21.configure(text='''*''')

        self.TButton1_1 = ttk.Button(top)
        self.TButton1_1.place(relx=0.675, rely=0.616, height=35, width=66)
        self.TButton1_1.configure(command=lambda: self.press("-"))
        self.TButton1_1.configure(text='''-''')

        self.TButton1_2 = ttk.Button(top)
        self.TButton1_2.place(relx=0.675, rely=0.753, height=35, width=66)
        self.TButton1_2.configure(command=lambda: self.press("+"))
        self.TButton1_2.configure(text='''+''')

        self.TButton1_3 = ttk.Button(top)
        self.TButton1_3.place(relx=0.675, rely=0.89, height=35, width=66)
        self.TButton1_3.configure(command=self.equalpress)
        self.TButton1_3.configure(text='''=''')

        self.TButton1_4 = ttk.Button(top)
        self.TButton1_4.place(relx=0.437, rely=0.89, height=35, width=46)
        self.TButton1_4.configure(command=self.clear)
        self.TButton1_4.configure(text='''C''')

        self.TButton1_5 = ttk.Button(top)
        self.TButton1_5.place(relx=0.04, rely=0.89, height=35, width=96)
        self.TButton1_5.configure(command=self.backspace)
        self.TButton1_5.configure(text='''<-----''')

        self.expression = ""

    # globally declare the expression variable 
     


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

    def sci_c(self):
        calulator_support.destroy_window()
        import scicalc       
        scicalc.vp_start_gui()
    

if __name__ == '__main__':
    vp_start_gui()





