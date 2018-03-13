import shlex, subprocess

print ("Hello world!")

def HelloWorld():
    print ("HelloWorldFromDef!")

def Cleared():
    print ("cleared")

def cmd1():
    command_line = input()
    args = shlex.split(command_line)
    p = subprocess.Popen(args) # Success!

def run1():
    from tkinter import *
    import subprocess as sub
    p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()



