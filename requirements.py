import os
import subprocess


def create_requirements_file():
    os.system('cmd /c "pip3 freeze > requirements.txt"')


def install_requirements():
    subprocess.check_call('pip3 install -r requirements.txt'.split())


if __name__ == '__main__':
    create_requirements_file()
    install_requirements()
