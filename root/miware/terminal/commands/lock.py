from root.miware.terminal.commands.resource import *
import os

def main():
    memory = get_memory()
    args = get_args(memory['full'])

    if args is False:
        return print("usage:\nlock [path/dir]")

    path = "{}\\{}".format(memory['path'], args[0])

    if os.path.isdir(path) is False:
        return print(Style.BRIGHT + Fore.RED + "The directory given does not exist, or is not a directory." + Style.RESET_ALL)

    with open("{}\\lock.txt".format(path), 'w') as f:
        f.write(memory['loggedin'])

    print(Style.BRIGHT + Fore.GREEN + "Directory has been locked." + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
