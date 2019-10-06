import os
from root.miware.terminal.commands.resource import *
from colorama import *

def main():
    memory = get_memory()
    folder_name = get_args(memory['full'])

    if folder_name is False:
        return print(Style.BRIGHT + Fore.RED + 'No Folder name has been given.' + Style.RESET_ALL)
    try:
        os.mkdir('{0}\\{1}'.format(memory['path'], folder_name[0]))
    except FileExistsError:
        return print(Fore.RED + "Directory '{0}' already exists".format(folder_name[0]) + Style.RESET_ALL)

    print('Directory ' + Fore.GREEN + folder_name[0] + Style.RESET_ALL + " created at\n" + Fore.GREEN + '{0}\\{1}'.format(format_path(memory['path']), folder_name[0]) + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
