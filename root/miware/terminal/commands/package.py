from root.miware.terminal.commands.resource import *
from root.miware.terminal import make_map

def main():
    memory = get_memory()
    args = get_args(memory['full'])
    colors = Colors()

    if check_admin(memory) is False:
        if prompt_admin_password() is False:
            return

    if args is False:
        return colors.error('Usage:\ndel [package]\n')

    if args[0].lower() == 'del':
        remove_package(args[1])

def check_command_existance(command):
    command_map = make_map()
    for cmd in command_map:
        if cmd == command:
            return True

    return False

def check_if_builtin_command(command):
    builtin_cmd = [
        "cd",
        'content',
        'createuser',
        'deleteuser',
        'edit',
        'help',
        'lock',
        'logout',
        'ls',
        'mkdir',
        'package',
        'resource',
        'rm',
        'rmdir',
        'shutdown',
        'unlock',
        'users'
    ]

    for cmd in builtin_cmd:
        if cmd == command:
            return True

    return False

def remove_package(package):
    try:
        if check_command_existance(package) is True and check_if_builtin_command(package) is False:
            os.remove('{0}\\root\\miware\\terminal\\commands\\{1}.py'.format(get_path(), package))
            Colors.succeed(Colors(), "Successfully deleted package {}".format(package))

        else:
            Colors.error(Colors(), "No such package exists, or you're trying to remove a built-in package.")

    except IndexError:
        return Colors.error(Colors(), 'No package name given.')


if __name__ == "__main__":
    pass
else:
    main()
