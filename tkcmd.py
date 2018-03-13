#init the GUI elements and the Text widget
from tkinter import *
root = Tk()
top = Frame(root)
outputFrame = Frame(top)
outputFrame.pack(side='top', padx=20, pady=20)
outputTextArea = Text(outputFrame, yscrollcommand='', width=150, height=40)
outputTextArea.pack(side='left', expand=YES, fill='both')

#callback executed when the button is clicked
def callMe():

    #get parameters
    # .....

    #command line execution script execution
    process = subprocess.Popen(command_line, stdout=subprocess.PIPE, shell=True)

    #get script output
    matr = process.stdout.readlines()

    #from a list of strings to a single string
    output = "".join(matr)  # <<< now it is:  output = "".join(matr).replace('\r', '')

    #write output into the Text widget
    outputTextArea.insert(0.0, output)