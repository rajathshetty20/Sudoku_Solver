#GUI Version of Sudoku using kivy
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
import sudoku
import time
import threading

#Game Page
class Game(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.buttons = [None]*81
        for x in range(0,9):
            subgrid = GridLayout()
            subgrid.cols=3
            subgrid.padding=[5,5,5,5]
            for y in range(0,9):
                button = Button(font_size="20")
                button.background_color = (1,1,1,1)
                subgrid.add_widget(button)
                rownumber = 3*(x//3)+(y//3)
                colnumber = 3*(x%3)+(y%3)
                self.buttons[9*rownumber+colnumber] = button
            self.add_widget(subgrid)

class MyApp(App):
    def build(self):
        self.title = "Sudoku"
        self.layout = BoxLayout(orientation='vertical')
        self.game = Game()
        
        self.options = BoxLayout(orientation='horizontal', size_hint=(1,0.1))
        self.solve = Button(text="Solve")
        self.solve.bind(on_press=self.solve_press)
        self.reset = Button(text="Reset")
        self.reset.bind(on_press=self.reset_press)
        self.options.add_widget(self.solve)
        self.options.add_widget(self.reset)

        self.layout.add_widget(self.game)
        self.layout.add_widget(self.options)
        return self.layout

    
    
    def update(self,reset=False,latest=[]):
        for i in range(0,81):
            row_number = i//9
            column_number = i%9
            self.game.buttons[i].text = str(sudoku.board[row_number][column_number])
            if self.game.buttons[i].text == "0":
                self.game.buttons[i].text = ""
                self.game.buttons[i].background_color = (1,1,1,1)
            elif reset:
                self.game.buttons[i].background_color = (0.5,0.5,0.5,0.5)
        if len(latest)==2:
            row,column = latest
            self.game.buttons[row*9+column].background_color = (0.8,0.8,0.8,1)
            
    def solve_press(self, button):
        x = threading.Thread(target=sudoku.solver, args=(self,))
        x.start()

    def reset_press(self, button):
        sudoku.init_board()
        self.update(reset=True)

if __name__ == "__main__":
    my_app = MyApp()
    my_app.run()
