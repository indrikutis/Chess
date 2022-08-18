# import everything from tkinter module
from tkinter import *  
from CoolButton import CoolButton 
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
#root.attributes('-fullscreen',True)
root.title("Chess I guess")
 
center_frame = Frame(
    root,
    bg='black',
    width = 100,
    height = 100
)
center_frame.place(
    x = 400,
    y = 400,
)


#Board creation, which every tile like a button
def boardCreation():
    for x in range(1,8,2):
        for f in range(2,9,2):
            buttonBlack = CoolButton()
            buttonBlack.createButton("black", center_frame)
            buttonBlack.cell_btn_object.grid(column=f, row=x)
        for i in range(1,8,2):
            buttonWhite = CoolButton()
            buttonWhite.createButton("white", center_frame)
            buttonWhite.cell_btn_object.grid(column=i, row=x)
    for x in range(2,9,2):
        for i in range(1,8,2):
            buttonBlack = CoolButton()
            buttonBlack.createButton("black", center_frame)
            buttonBlack.cell_btn_object.grid(column=i, row=x)
        for f in range(2,9,2):
            buttonWhite = CoolButton()
            buttonWhite.createButton("white", center_frame)
            buttonWhite.cell_btn_object.grid(column=f, row=x)

#boardCreation()

buttonBlack = CoolButton()
buttonBlack.createButton("", center_frame)
buttonBlack.cell_btn_object.grid(column=1, row=0)

root.mainloop()