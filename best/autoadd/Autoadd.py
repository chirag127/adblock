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

    with open("Custom/url.txt", "r") as file:
        urls = file.read()
    urlslist = urls.split("\n")

    print(len(urlslist))

    for url in urlslist:

        pyautogui.press("end")

        Click_Add_custom_filter()

        sleep(0.1)

        Type_url(url)

        sleep(0.1)

        Click_next()

        pyautogui.moveTo(100, 500)

        sleep(1)

        try:

            x_subscribe, y_subscribe = pyautogui.locateCenterOnScreen(
                "assests/images/subscribe.png"
            )

            x_trust = x_subscribe - 307

            y_trust = y_subscribe - 120

            pyautogui.click(x_trust, y_trust)

            sleep(0.1)

            pyautogui.click(x_subscribe, y_subscribe)

            sleep(0.5)

        except Exception as e:
            print(e)

            pyautogui.hotkey("ctrl", "r")

            sleep(1)

    print("Done")


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed("ctrl + q"):

            main()

        else:
            sleep(0.01)
