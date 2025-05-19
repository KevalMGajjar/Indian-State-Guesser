import pandas
from turtle import Turtle, Screen

class StateManager(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv(r"C:\Users\KEVAL\Desktop\Coding\Python Udemy\games\indian_state_guess\indian_states_coordinates_updated.csv")
        self.user_input = ''
        self.correct_states_num = 0
        self.num_states = len(self.data["State"]) - 1
        self.correct_states = self.data["State"].to_list()
        self.lower_correct_states = [state.lower() for state in self.correct_states]
        self.ht()
        
    def input_screen(self):
        screen = Screen()
        self.user_input = screen.textinput(f"{self.correct_states_num}/{self.num_states} States Correct", "Guess a state: ")
        if self.user_input == "exit":
            screen.bye()
        else:    
            self.correct()
        
    def correct(self):
        if self.user_input in self.lower_correct_states:
            self.correct_states_num += 1
 
           
            
            
        