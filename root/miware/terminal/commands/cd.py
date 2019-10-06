import os
from root.miware.terminal.commands.resource import *
from colorama import *
from root.miware import jsonCommon

def main():
    cwdpath = get_path()
    memory = get_memory()
    args = get_args(memory['full'])

    if args is False:
        return print('usage:\ncd [path]')

    path = "{}\\{}".format(memory['path'], args[0])

    # check if the user wants to go back a directory
    if args[0] == '..':
        placeholder = memory['path'].split('\\')
        placeholder.pop(-1)
        path = "\\".join(placeholder)

        if format_path(memory['path']) == 'root':
            return print(Style.BRIGHT + Fore.RED + "Cannot CD beyond Root" + Style.RESET_ALL)

        if format_path(memory['path']) == "root\\{}".format(memory['loggedin']):
            if check_admin(memory) is False:
                if prompt_admin_password() is False:
                    return print(Style.BRIGHT + Fore.RED + "Cannot CD beyond one owns directory." + Style.RESET_ALL)


    if os.path.isdir(path) and os.path.exists(path) and args[0] != '.': # Check if user is trying to cd into a file, and if yes, if the directory exists
        pass
    else:
        return print(Style.BRIGHT + Fore.RED + "No such Directory exists, or you're trying to CD into a File." + Style.RESET_ALL)

    if check_locked_dir("{}\\{}".format(memory['path'], args[0].split('\\')[0])) is not False:
        if check_locked_dir("{}\\{}".format(memory['path'], args[0].split('\\')[0])) != memory['loggedin']:
            return print(Style.BRIGHT + Fore.RED + "A Directory you're trying to cd to, is locked by {0}.".format(check_locked_dir("{}\\{}".format(memory['path'], args[0].split('\\')[0]))) + Style.RESET_ALL)

    os.chdir(path)
    memory['path'] = path

    json = JsonShort('{}\\root\\miware\\terminal\\json\\memory.json'.format(cwdpath))
    json.closeJson(memory)

if __name__ == "__main__":
    pass
else:
    main()