import os
from root.miware.terminal.commands.resource import *

def main():
    if ask_true_or_false() is False:
        return

    memory = get_memory()
    args = get_args(memory['full'])

    if args is False:
        return print('usage:\nrm [file/path]')

    if check_admin(memory) is False:
        if prompt_admin_password() is False:
            return

    file = "{}\\{}".format(memory['path'], args[0])
    if os.path.isdir(file):
        return print(Style.BRIGHT + Fore.RED + "File Specified is a Directory." + Style.RESET_ALL)
    if os.path.exists(file) is False:
        return print(Style.BRIGHT + Fore.RED + "File Specified does not exist." + Style.RESET_ALL)

    os.remove(file)

    print('File ' + Fore.GREEN + args[0] + Style.RESET_ALL + " deleted at\n" + Fore.GREEN + '{0}\\{1}'.format(format_path(memory['path']), args[0]) + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
