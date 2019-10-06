from root.miware.terminal.commands.resource import *
import webbrowser
import os

def main():
    memory = get_memory()
    args = get_args(memory['full'])

    if args is False:
        return print(Style.BRIGHT + Fore.RED + "No file specified!" + Style.RESET_ALL)

    file = "{}\\{}".format(memory['path'], args[0])
    if os.path.isdir(file):
        return print(Style.BRIGHT + Fore.RED + "File specified does not exist, or is a directory." + Style.RESET_ALL)

    if os.path.exists(file) is False:
        with open(file, 'w'):
            pass

    os.system('notepad.exe {}'.format(file))


if __name__ == "__main__":
    pass
else:
    main()
