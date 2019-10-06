from root.miware.terminal.commands.resource import get_memory
import os
from colorama import *

def main():
    memory = get_memory()
    for file in os.listdir(memory['path']):
        if file == '__pycache__':
            pass
        else:
            if os.path.isfile(file):
                print(file.split('\\')[-1])
            else:
                print(Style.BRIGHT + Fore.LIGHTBLUE_EX + file.split('\\')[-1] + Fore.RESET)


if __name__ == "__main__":
    pass
else:
    main()
