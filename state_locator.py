import pandas
from turtle import Turtle

ALLIGNMENT = "center"
FONT = ('Courier', 8, 'normal')

state_dict = {
    'Jammu And Kashmir': 0,
    'Himachal Pradesh': 1,
    'Punjab': 2,
    'Uttarakhand': 3,
    'Haryana': 4,
    'Rajasthan': 5,
    'Uttar Pradesh': 6,
    'Bihar': 7,
    'Sikkim': 8,
    'Arunachal Pradesh': 9,
    'Assam': 10,
    'Meghalaya': 11,
    'Nagaland': 12,
    'Manipur': 13,
    'Mizoram': 14,
    'Tripura': 15,
    'West Bengal': 16,
    'Jharkhand': 17,
    'Odisha': 18,
    'Chhattisgarh': 19,
    'Madhya Pradesh': 20,
    'Gujarat': 21,
    'Maharashtra': 22,
    'Goa': 23,
    'Karnataka': 24,
    'Kerala': 25,
    'Tamil Nadu': 26,
    'Andhra Pradesh': 27,
    'Telangana': 28
}

inputs = []

class StateLocator(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("indian_states_coordinates_updated.csv")
        self.states = self.data["State"].to_list()
        self.lower_states = [state.lower() for state in self.states]
        self.color("black")
        self.xcord = 0
        self.ycord = 0
        self.ht()
        self.penup()
        self.choice = True 

    def draw(self, input):    
        if input != "exit":
            if input in self.lower_states:
                capital_input = input.title()
                state_data = self.data[self.data.State == capital_input]
                self.xcord = state_data['X_Coordinate'][state_dict[capital_input]]
                self.ycord = state_data['Y_Coordinate'][state_dict[capital_input]]
                self.goto(self.xcord, self.ycord)
                self.write(f"{capital_input}", align=ALLIGNMENT, font=FONT)
                inputs.append(capital_input)
            else:
                print("Invalid Answer, Please start over")
                self.choice = False 
            return self.choice     
        else:
            left_states = [state for state in self.states if state not in inputs]
            data = pandas.DataFrame(left_states)
            data.to_csv(r"games\indian_state_guess\left_out_states")
