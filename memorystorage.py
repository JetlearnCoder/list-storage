from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

window = Tk()
window.geometry("750x300")
window.config(bg = "white")

def openfile():
    file = askopenfile(title = "Open File")
    if file is not None:
        listbox.delete(0,END)
        items = file.readlines()
        for i in items:
            listbox.insert(END,i.strip())
            
def additem():
    x = addtext.get()
    listbox.insert(END,x.strip())

def deleteitem():
    y = listbox.curselection()
    listbox.delete(y)
    
def saveitem():
    f = asksaveasfile(defaultextension = ".txt")
    if f is not None:
        for i in listbox.get(0,END):
            print(i.strip(),file = f )
        listbox.delete(0,END)
        
        
openbutton = Button(window,text = "Open", command = openfile)
addbutton = Button(window,text = "Add", command = additem)
savebutton = Button(window,text = "Save", command = saveitem)
deletebutton = Button(window,text = "Delete", command = deleteitem)

frame = Frame(window)
frame.pack(side = BOTTOM)
listed = ["a","b","cde"]
scrlbar = Scrollbar(frame,orient = "vertical")
addtext = Entry(window)

listbox = Listbox(frame,width = 45, yscrollcommand = scrlbar.set, bg = "grey")
for i in range(500):
    listbox.insert(END,"LIST "+str(i))

openbutton.place(x = 20, y = 110)
addbutton.place(x = 300, y = 70)
savebutton.place(x = 300, y = 20)
deletebutton.place(x = 600, y = 110 )
addtext.place(x = 250, y = 90 )

listbox.pack(side = LEFT, padx = 5)
scrlbar.pack(side = RIGHT, pady = 5)
scrlbar.config(command = listbox.yview)


window.mainloop()