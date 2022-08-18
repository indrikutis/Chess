from tkinter import Button, PhotoImage

class CoolButton:
    def __init__(self):
        self.cell_btn_object = None

    def createButton(self, text, location):
        img = PhotoImage(file="chess/circle.png")
        btn = Button(
            location,
            text = text,
            height=32,
            width=32,
            image=img
        )
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click
        self.cell_btn_object = btn
        print(btn)

    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")
