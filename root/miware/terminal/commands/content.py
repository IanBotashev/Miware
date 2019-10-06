from root.miware.terminal.commands.resource import *
from colorama import *
import os

def main():
    memory = get_memory()
    file = get_args(memory['full'])
    if file is False:
        return print("usage:\ncontent [file/path]")
    pathtofile = "{0}\\{1}".format(memory['path'], file[0])

    if os.path.isdir(pathtofile) or os.path.exists(pathtofile) is False:
        return print(Style.BRIGHT + Fore.RED + "File given is a directory, or the file does not exist." + Style.RESET_ALL)

    with open(pathtofile, 'r') as f:
        print(Fore.RED + "{-------\n" + Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + f.read() + Style.RESET_ALL)
        print(Fore.RED + "}-------" + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
