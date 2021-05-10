from subprocess import run
from pyautogui import press, typewrite
from time import sleep
from settings import get_user, get_database, get_password


def main():
    user = get_user()
    database = get_database()
    password = get_password()

    command = f"psql -U {user} -d {database}"

    run(['start'], shell=True)
    sleep(0.2)

    typewrite(command)
    press("enter")
    sleep(0.5)

    typewrite(password)
    press("enter")


if __name__ == '__main__':
    main()
