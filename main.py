from subprocess import run
from pyautogui import press, typewrite
from time import sleep
from settings import get_postgres_password


def main():
    run(['start'], shell=True)
    sleep(0.2)

    # ユーザー名・データベース名はここ
    typewrite("psql -U YourUserName -d YourDataBase")
    press("enter")
    sleep(0.5)

    typewrite(get_postgres_password())
    press("enter")


if __name__ == '__main__':
    main()
