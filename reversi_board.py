import argparse
import tkinter as tk
 
class Board(tk.Tk):
    def __init__(self):
        super(Board, self).__init__()                     
        self.title("reversi")
        self.geometry("600x700")
        self.drow_board()
 
    def drow_board(self):
        self.board = tk.Canvas(self, bg="#8a2be2", width=600, height=600)
        self.board.place(x=0, y=0)
        for y in range(20, 570,70):
            for x in range(20, 570, 70):
                pos = x, y, x+70, y+70
                self.board.create_rectangle(*pos, fill="#7fffd4")
 
    def run(self):
        self.mainloop()        
 
if __name__ == "__main__":
    app = Board()
    app.run()