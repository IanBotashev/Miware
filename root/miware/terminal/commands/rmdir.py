import os
from root.miware.terminal.commands.resource import *
from colorama import *
import shutil

def main():
    if ask_true_or_false() is False:
        return

    memory = get_memory()
    folder_name = get_args(memory['full'])

    if check_admin(memory) is False:
        if prompt_admin_password() is False:
            return

    if folder_name is False:
        return print(Style.BRIGHT + Fore.RED + 'No Folder name has been given.' + Style.RESET_ALL)

    try:
        os.rmdir('{0}\\{1}'.format(memory['path'], folder_name[0]))
    except FileNotFoundError:
        return print(Fore.RED + "Directory '{0}' does not exist.".format(folder_name[0]) + Style.RESET_ALL)

    except OSError:
        try:
            if folder_name[1] == 'tree':
                shutil.rmtree('{0}\\{1}'.format(memory['path'], folder_name[0]))
        except IndexError:
            return print(Fore.RED + "Directory '{0}' is not empty.\nIf you want to delete it anyway, do 'rmdir {0} tree'".format(folder_name[0]) + Style.RESET_ALL)

    print('Directory ' + Fore.GREEN + folder_name[0] + Style.RESET_ALL + " removed at\n" + Fore.GREEN + '{0}\\{1}'.format(format_path(memory['path']), folder_name[0]) + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
