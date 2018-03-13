from tkinter import *
import sys
sys.path.append("/path/to/script/file/directory/")

class App(Frame):
    def run_script(self):
        sys.stdout = self
        ## sys.stderr = self
        try:
            del(sys.modules["test_script"])
        except:
            ## Yeah, it's a real ugly solution...
            pass
        import test_script
        test_script.HelloWorld()
        sys.stdout = sys.__stdout__
        ## sys.stderr = __stderr__


    def run_cls(self):
        sys.stdout=self

        ''''try:
            del(sys.modules["test_script"])
        except:
            pass
        '''
        import test_script
        test_script.cmd1()
        sys.stdout=sys.__stdout__

    def cmd2 (self):
        cmd1()



    def build_widgets(self):
        self.text1 = Text(self)
        self.text1.pack(side=TOP)
        self.button = Button(self)
        self.button["text"] = "Trigger script"
        self.button["command"] = self.run_script
        self.button.pack(side=TOP)

        self.buttoncls = Button(self)
        self.buttoncls["text"] = "Trigger script"
        self.buttoncls["command"] = self.cmd2
        self.buttoncls.pack(side=RIGHT)

    def write(self, txt):
        self.text1.insert(INSERT, txt)

    def cmd1():
        #command_line = self.text1.get()
        args = shlex.split(self.text1.get())
        p = subprocess.Popen(args) # Success!


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.build_widgets()

root = Tk()
app = App(master = root)
app.mainloop()