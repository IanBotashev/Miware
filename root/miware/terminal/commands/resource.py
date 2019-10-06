from root.miware.jsonCommon  import *
import random
from colorama import *

def get_memory():
    """Gets everything saved in memory.json"""
    json = JsonShort('{}\\root\\miware\\terminal\\json\\memory.json'.format(get_path()))
    return json.openJson()

def get_args(full_command):
    """
    Gets the args given to a command
    For example:
        cd /path/to/somewhere/
    returns:
        /path/to/somewhere/
    :return:
    """
    placeholderArgs = full_command.split(' ')
    placeholderArgs.pop(0)
    result = placeholderArgs
    if result == []:
        return False
    return result

def format_path(path):
    """
    Returns a formatted path, starting from \root
    :return:
    """
    return path.replace('{}\\'.format(get_path()), '')


def check_admin(memory):
    """
    Check if the logged in user is an admin
    :return:
    """
    if memory['admin'] is True:
        return True
    else:
        return False

def prompt_admin_password():
    """
    Prompt for admin password
    :return:
    """
    json = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(get_path()))
    data = json.openJson()

    main = JsonShort('{}\\root\\miware\\terminal\\json\\main.json'.format(get_path()))
    main_data = main.openJson()

    admin = main_data['main_admin']
    admin_password = data[admin]['password']

    password = input('Admins Password: ')

    if admin_password == password:
        return True
    else:
        print(Style.BRIGHT + Fore.RED + "Incorrect password." + Style.RESET_ALL)
        return False

def ask_true_or_false():
    """
    Ask if a user is sure about an action
    :return:
    """
    while True:
        ask = input(Fore.GREEN + 'Are you sure you want to continue? [Y/N] ' + Fore.RESET)
        if ask.lower() == 'y':
            return True
        else:
            return False

def check_if_user_exists(username):
    """
    Checks if a given user exists.
    :return:
    """
    users = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(get_path()))
    users_data = users.openJson()

    for user in users_data:
        if user == username:
            return True

    # Else
    return False

def check_locked_dir(path):
    """
    Check if a directory is locked.
    :param path:
    :return:
    """
    files = os.listdir(path)

    for file in files:
        if file == 'lock.txt':
            with open("{}\\lock.txt".format(path), 'r') as f:
                return f.read()

    return False

class Colors:
    """
    A class for colors. Pretty self-explanatory.
    """
    def error(self, message):
        print(Style.BRIGHT + Fore.RED + message + Style.RESET_ALL)

    def succeed(self, message):
        print(Style.BRIGHT + Fore.GREEN + message + Style.RESET_ALL)

    def warn(self, message):
        print(Style.BRIGHT + Fore.YELLOW + message + Style.RESET_ALL)

def get_path():
    """
    Get the path where root is contained.
    :return:
    """
    path = os.getcwd().split('\\root')[0]
    return path
