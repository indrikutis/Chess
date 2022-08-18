from tkinter import *  
from PIL import Image, ImageTk

class CoolButton():
    def __init__(self, root, imagePath):
        self.createButton(root, imagePath)

    def createButton(self, root, imagePath):

        width = 50
        height = 50

        self.img = Image.open(imagePath)
        self.img = self.img.resize((width, height))
        self.img=ImageTk.PhotoImage(self.img)

        self.btn = Button(root, image = self.img, width = width, height = height)
        self.btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        self.btn.bind('<Button-3>', self.right_click_actions ) # Right Click
        
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    
