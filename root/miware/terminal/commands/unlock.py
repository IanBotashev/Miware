from root.miware.terminal.commands.resource import *

def main():
    memory = get_memory()
    args = get_args(memory['full'])

    if args is False:
        return print("usage:\nunlock [dir/path]")

    path = "{}\\{}".format(memory['path'], args[0])
    if os.path.isdir(path) is False:
        return print(Style.BRIGHT + Fore.RED + "The directory given does not exist, or is not a directory." + Style.RESET_ALL)

    if check_locked_dir(args[0].split('\\')[0]) is False:
        return print(Style.BRIGHT + Fore.RED + "The directory you're trying to unlock, is not locked." + Style.RESET_ALL)
    user = check_locked_dir(args[0])

    if user != memory['loggedin']:
        return print(
            Style.BRIGHT + Fore.RED + "You cannot unlock this directory, as you're not the owner of it." + Style.RESET_ALL)

    os.remove("{}\\lock.txt".format(path))

    print(Style.BRIGHT + Fore.GREEN + "Successfully unlocked directory." + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
