from re import S
import pyautogui
import keyboard
from time import sleep
import webbrowser
# Physical: {X=802,Y=822}
# Physical: {X=914,Y=725}
# Physical: {X=916,Y=900}
# Physical: {X=644,Y=798}


def Click_Add_custom_filter():
    pyautogui.click(x=802, y=822)

# define a function to type the url


def Type_url(url):
    pyautogui.typewrite(url)

# define a function to click the next button


def Click_next():
    pyautogui.click(x=914, y=725)


def main():

    # file = open("Custom/url.txt", "r")
    # urls = file.read()
    # file.close()

    urls = """https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/EkstraBladetEroticContentRemover.txt"""

    urlslist = urls.split('\n')

    print(len(urlslist))

    sleep(0.5)

    for url in urlslist:

        pyautogui.press('end')

        Click_Add_custom_filter()

        sleep(0.1)

        Type_url(url)

        sleep(0.1)

        Click_next()

        pyautogui.moveTo(100, 500)

        sleep(1)

        try:

            x_subscribe, y_subscribe = pyautogui.locateCenterOnScreen(
                'snew.png')

            x_trust = x_subscribe - 272

            y_trust = y_subscribe - 102

            pyautogui.click(x_trust, y_trust)

            sleep(0.1)

            pyautogui.click(x_subscribe, y_subscribe)

            sleep(0.5)

        except Exception as e:
            print(e)

            pyautogui.hotkey('ctrl', 'r')

            sleep(1)

    print('Done')


if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('ctrl + q'):

            main()

        else:
            sleep(0.01)
