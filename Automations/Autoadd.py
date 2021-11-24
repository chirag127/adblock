from re import S
import pyautogui
import keyboard
from time import sleep
import webbrowser
# Physical: {X=791,Y=682}
# Physical: {X=921,Y=730}
# Physical: {X=641,Y=611}
# Physical: {X=958,Y=731}


def Click_Add_custom_filter():
    pyautogui.click(x=791, y=682)

# define a function to type the url


def Type_url(url):
    pyautogui.typewrite(url)

# define a function to click the next button


def Click_next():
    pyautogui.click(x=921, y=730)


def main():

    urls = """
https://raw.githubusercontent.com/chirag127/adblock/master/AD.txt
https://raw.githubusercontent.com/chirag127/adblock/master/AL.txt
https://raw.githubusercontent.com/chirag127/adblock/master/APWL.txt
https://raw.githubusercontent.com/chirag127/adblock/master/C.txt
https://raw.githubusercontent.com/chirag127/adblock/master/D.txt
https://raw.githubusercontent.com/chirag127/adblock/master/E.txt
https://raw.githubusercontent.com/chirag127/adblock/master/F.txt
https://raw.githubusercontent.com/chirag127/adblock/master/GD.txt
https://raw.githubusercontent.com/chirag127/adblock/master/H.txt
https://raw.githubusercontent.com/chirag127/adblock/master/N.txt
https://raw.githubusercontent.com/chirag127/adblock/master/NF.txt
https://raw.githubusercontent.com/chirag127/adblock/master/O.txt
https://raw.githubusercontent.com/chirag127/adblock/master/P.txt
https://raw.githubusercontent.com/chirag127/adblock/master/S.txt
https://raw.githubusercontent.com/chirag127/adblock/master/SR.txt
https://raw.githubusercontent.com/chirag127/adblock/master/T.txt
https://raw.githubusercontent.com/chirag127/adblock/master/W.txt
https://raw.githubusercontent.com/chirag127/adblock/master/YT.txt
"""

    urlslist = urls.split('\n')

    print(urlslist.count())

    for url in urlslist:

        pyautogui.press('end')

        Click_Add_custom_filter()

        sleep(0.1)

        Type_url(url)   # type the url

        Click_next()

        sleep(1)

        try:

            x_subscribe, y_subscribe = pyautogui.locateCenterOnScreen(
                'subscribe.png')

            x_trust = x_subscribe - 307

            y_trust = y_subscribe - 120

            pyautogui.click(x_trust, y_trust)

            pyautogui.click(x_subscribe, y_subscribe)

        except Exception as e:
            print(e)

        pyautogui.hotkey('ctrl', 'r')

        sleep(0.5)

    print('Done')


if __name__ == '__main__':
    
    while True:

        if keyboard.is_pressed('ctrl + q'):

            main()

        else:
            sleep(0.01)
