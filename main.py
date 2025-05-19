from turtle import Screen
import time
from state_manager import StateManager
from state_locator import StateLocator

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgpic(r"C:\Users\KEVAL\Desktop\Coding\Python Udemy\games\indian_state_guess\indian_states.gif")
state_manager = StateManager()
state_locator = StateLocator()
screen.listen()


while state_locator.choice == True:
    time.sleep(0.1)
    screen.update()
    state_manager.input_screen()
    state_locator.draw(state_manager.user_input)
    
screen.exitonclick()    
    