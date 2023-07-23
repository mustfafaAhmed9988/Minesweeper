import settings
from cell import Cell
import utils
from tkinter import * 
root = Tk()
root.geometry(f'{settings.Width}x{settings.Height}')
root.configure(bg="black")
root.title("Minessweeper Game")
root.resizable(False,False)
topFrame = Frame(
    root,
    bg='black',  
    width=settings.Width,
    height=utils.heightPercentage(25)
)
topFrame.place(x= 0 , y=0)
game_title = Label(
    topFrame, 
    bg='black' , 
    fg='white' , 
    text="MinesSweeper Game" , 
    font = ('' , 48)
)
game_title.place(
    x= utils.widthPercentage(25), y = 0 
)
leftFrame= Frame(
    root,
    bg="black" ,
        width=utils.widthPercentage(25),
    height=utils.heightPercentage(75), 
)
centerFrame = Frame(
    root,
    bg="black" , 
    width=utils.widthPercentage(75) , 
    height=utils.heightPercentage(75) ,
)
centerFrame.place(x = utils.widthPercentage(25), y = utils.heightPercentage(25))
leftFrame.place(x =0 , y = utils.heightPercentage(25))
for x in range(settings.gridSize):
    for y in range(settings.gridSize):
        c1 = Cell(x,y) 
        c1.createButtonObject(centerFrame)
        c1.cellButtonObject.grid(
            row=y, column=x
        )
Cell.createCellCountLabel(leftFrame)
Cell.cellCountLabel.place(x = 0 , y =0 )        
Cell.randomizeMines()       
root.mainloop()
