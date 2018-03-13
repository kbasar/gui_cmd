import tkinter as tk
from tkinter import ttk

class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default = "")
        tk.Tk.wm_title(self, "")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Add, BlankPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Add)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class Add(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        innerFrame = tk.Frame(self)
        innerFrame.place(relx=.5, rely=.5, anchor="c", relwidth=1.0, relheight=1.0)

        innerFrame.grid_rowconfigure(1, weight=1)
        innerFrame.grid_columnconfigure(0, weight=1)

        name = tk.Label(innerFrame, text = "User")
        name.grid(row=0, sticky="NE")

        pagename = tk.Label(innerFrame, text = "Label")
        pagename.grid(row=0, sticky="N")

        next = ttk.Button(innerFrame, text = "Next", command = self.changePage)
        next.grid(row=2, sticky="E")

        back = ttk.Button(innerFrame, text = "Back", command = self.changePage)
        back.grid(row=2, sticky="W")

###########################################################################################################

        self.pageThree = tk.Frame(innerFrame)
        self.pageThree.grid(row=1)

        self.pageThree.grid_rowconfigure(0, weight=1)
        self.pageThree.grid_columnconfigure(0, weight=1)

        pagename = tk.Label(self.pageThree, text = "Page 3")
        pagename.grid(row=0, sticky="N")

###########################################################################################################

        self.pageTwo = tk.Frame(innerFrame)
        self.pageTwo.grid(row=1)

        self.pageTwo.grid_rowconfigure(0, weight=1)
        self.pageTwo.grid_columnconfigure(0, weight=1)

        pagename = tk.Label(self.pageTwo, text = "Page 2")
        pagename.grid(row=0, sticky="N")

###########################################################################################################

        self.pageOne = tk.Frame(innerFrame)
        self.pageOne.grid(row=1)

        self.pageOne.grid_rowconfigure(0, weight=1)
        self.pageOne.grid_columnconfigure(0, weight=1)

        pagename = tk.Label(self.pageOne, text = "Page 1")
        pagename.grid(row=0, sticky="N")

###########################################################################################################

    def changePage(self,buttonBool):
        pages = [self.pageOne,self.pageTwo,self.pageThree]
        #find current raised page and set to variable 'current'
        position = pages.index(current)
        if (postion==0 and buttonBool==False) or (postion==len(pages)-1 and buttonBool==True):
            show_frame(BlankPage)
        elif buttonBool==True:
            pages[position+1].tkraise()
        else:
            pages[position-1].tkraise()


class BlankPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)


app = Program()
app.state('zoomed')
app.mainloop()