from parse import parse
import re
import tkinter as tk

def display():
    out.delete(1.0, "end-1c")   # clear up the text box
    regex = parse(e.get())
    out.insert("end-1c", "Regex in python: {0}\n".format(regex))
    out.insert("end-1c", 'starting the test: ...\n')
    for case, status in suite:
        x = re.search(regex, case) is not None
        if x != status:
            out.insert("end-1c", "error: case: {0}, expected: {1}\n".format(case, status))
    out.insert("end-1c", 'done!\n')

# read the test suite file
suite = []
with open('test-suite', 'r') as f:
    for line in f:
        word, status = line.strip().split()
        status = status == 'True'
        suite.append((word, status))

master = tk.Tk()
master.title("CSCB36 TT3 Q11 Auto Marker")

tk.Label(master, 
         text="Enter regex").grid(row=0, column=0)
e = tk.Entry(master, width=50)
e.grid(row=0, column=1)

tk.Button(master, 
          text='Show', command=display).grid(row=1, 
                                            column=0, 
                                            sticky=tk.W, 
                                            pady=4)
          
out = tk.Text(master)
out.grid(row=2, column = 0, columnspan = 2)

master.mainloop()
