import pyautogui
from time import sleep
import keyboard
# Physical: {X=639,Y=759}


# define the function to click on the remove extension button
def remove_extension():
    pyautogui.click(x=639, y=759)

def main():
    # define the function to click on the remove extension button
    remove_extension()

    sleep(0.5)

    # define the function to click exter
    pyautogui.press('enter')

    sleep(0.5)

if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('ctrl+c'):

            while True:

                main()

        else:
            sleep(0.01)
    
