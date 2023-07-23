from tkinter import Button,Label
import random
import settings
import sys
class Cell:
    all = []
    cell_count = settings.gridSize **2 
    cellCountLabel = None 

    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.isOpened = False 
        self.isMineCandidate = False 
        self.x = x
        self.y = y
        self.cellButtonObject = None
        Cell.all.append(self)

    def createButtonObject(self, location):
        btn = Button(location, width=12, height=4)
        btn.bind("<Button-1>", self.leftClickAction)
        btn.bind("<Button-3>", self.rightClickAction)
        self.cellButtonObject = btn
    @staticmethod
    def createCellCountLabel(location):
        lbl = Label(
            location, 
            text = f"Cells left {Cell.cell_count}" , 
            bg="black", 
            fg="white",
            font=("" , 30)
        )
        Cell.cellCountLabel = lbl  
    def leftClickAction(self, event):
        if self.isMine:
            self.showMine()
        else:
            if self.countingMinesInSurrounedCells == 0 :
                for cell in self.surroundedCell : 
                    cell.showCell
            self.showCell()
        if Cell.cell_count == settings.minescount :
            #when i open the pc 
            pass    
        self.cellButtonObject.unbind('<Button-1>')  
        self.cellButtonObject.unbind('<Button-3>')  


    @property        
    def surroundedCell(self):
        surCells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y ),
            self.get_cell_by_axis(self.x - 1, self.y +1),
            self.get_cell_by_axis(self.x , self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x +1, self.y ),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        surCells= [x for x in surCells if x!= None]   
        return surCells     
    @property
    def countingMinesInSurrounedCells (self):
        counter =0 
        for cell in self.surroundedCell:
            if cell.isMine:
                counter +=1
        return counter     

    def showCell(self):
        if not self.isOpened :
            Cell.cell_count -= 1 
            self.cellButtonObject.configure(text=self.countingMinesInSurrounedCells)
            if Cell.cellCountLabel:
                Cell.cellCountLabel.configure(
                    text=f"Cell left :{Cell.cell_count}"
                )
        self.isOpened = True        

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def showMine(self):
        self.cellButtonObject.configure(bg="red")
        sys.exit()


    def rightClickAction(self, event):
        if not self.isMineCandidate : 
            self.cellButtonObject.configure(
                bg="orange" , 

            )
            self.isMineCandidate = True
        else :
            self.isMineCandidate = False 
            self.cellButtonObject.configure(
                bg = 'SystemButtonFace'
            )    

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(Cell.all, settings.minescount)
        for cell in pickedCells:
            cell.isMine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
