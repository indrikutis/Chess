# import everything from tkinter module
from tkinter import *  
from CoolButton import CoolButton 
 
def boardCreation(imagePathBlack, imagePathWhite):
    for x in range(1,8,2):
        for f in range(2,9,2):
            buttonBlack = CoolButton(root, imagePathBlack)
            buttonBlack.btn.grid(column=f, row=x)
        for i in range(1,8,2):
            buttonWhite = CoolButton(root, imagePathWhite)
            buttonWhite.btn.grid(column=i, row=x)
    for x in range(2,9,2):
        for i in range(1,8,2):
            buttonBlack = CoolButton(root, imagePathBlack)
            buttonBlack.btn.grid(column=i, row=x)
        for f in range(2,9,2):
            buttonWhite = CoolButton(root, imagePathWhite)
            buttonWhite.btn.grid(column=f, row=x)



# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
#root.attributes('-fullscreen',True)
root.title("Chess I guess")
root.geometry("450x450")

#Board creation, which every tile like a button
imagePathBlack = "Images/black.png"
imagePathWhite = "Images/white.png"

boardCreation(imagePathBlack, imagePathWhite)

root.mainloop()