from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk,Image 

def open():
    fileTypes = [
        ('JPG(*.jpg)','*.jpg'),
        ('PNG(*.png)','*.png')
    ]
    fileName = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=fileTypes
    ) 
    img = ImageTk.PhotoImage(Image.open(fileName))
    canvas.create_image(20,20,anchor=NW,image=img)

def createMenu():
    menubar = Menu(ui)
    file = Menu(menubar,tearoff=0)
    file.add_command(label="Open",command=open)
    file.add_command(label="Save")
    file.add_separator()
    file.add_command(label="Exit",command=ui.quit)

    menubar.add_cascade(label="File",menu=file)

    edit = Menu(menubar,tearoff=0)
    edit.add_command(label="Undo")
    edit.add_command(label="Redo")

    menubar.add_cascade(label="Edit",menu=edit)

    view = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="View",menu=view)

    transform = Menu(menubar,tearoff=0)

    transformSubMenu = Menu(transform,tearoff=0)
    transformSubMenu.add_command(label="Min")
    transformSubMenu.add_command(label="Max")
    transformSubMenu.add_command(label="Average")
    transformSubMenu.add_command(label="Luminosity")

    transform.add_cascade(label="GrayScale",menu=transformSubMenu)


    menubar.add_cascade(label="Transform",menu=transform)

    ui.config(menu=menubar)
    

ui = Tk()
ui.title("Img Processing")
screen_width = ui.winfo_screenwidth()
screen_height = ui.winfo_screenheight()
#print(screen_height)
#print(screen_width)
ui.geometry("{}x{}+{}+{}".format(int(screen_width)-500,
              int(screen_height)-500, 0, 0))

createMenu()

canvas = Canvas(ui,width=500,height=500)
canvas.pack()


ui.mainloop()






ui.mainloop()
