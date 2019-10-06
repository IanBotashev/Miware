from root.miware.jsonCommon import *
from colorama import *
import os
from root.miware.terminal.commands.resource import *
import winsound


def login_main():
    """
    Used for logining in.
    :return:
    """
    attempts = 0
    while True:
        if attempts >= 5:
            print(Style.BRIGHT + Back.RED + "Too many attempts. Exiting." + Style.RESET_ALL)
            exit()
        path = get_path()
        username, password = get_credentials()
        data, json = open_users()

        if check_credentials(data, username, password):
            print(Style.BRIGHT + Fore.GREEN + 'Successfully Logged in.' + Style.RESET_ALL)

            try:
                os.chdir('{0}\\root\\{1}'.format(path, username))
            except FileNotFoundError:
                os.mkdir('{0}\\root\\{1}'.format(path, username))
                os.chdir('{0}\\root\\{1}'.format(path, username))
                print(Style.BRIGHT + Fore.RED + "A new directory has been created for you, as no other directory under your name has been found." + Style.RESET_ALL)

            commit_to_memory(username, '{0}\\root\\{1}'.format(path, username))
            return

        else:
            attempts += 1
            winsound.PlaySound('{}\\root\\miware\\sounds\\error.wav'.format(get_path()), winsound.SND_ASYNC)
            print(Style.BRIGHT + Fore.RED + "Invalid Password or Username. Try again.\n{} attempt(s) left.".format(5-attempts) + Style.RESET_ALL)


def open_users():
    path = get_path()
    json = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(path))
    data = json.openJson()
    return data, json


def get_credentials():
    username = input('Username: ')
    password = input('Password: ')

    return username, password


def check_credentials(data, username, password):
    try:

        if data[username] and data[username]['password'] == password:
            return True

    except KeyError:
        return False


def commit_to_memory(username, path):
    cwdpath = get_path()
    memory = JsonShort('{}\\root\\miware\\terminal\\json\\memory.json'.format(cwdpath))
    users = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(cwdpath))

    usersData = users.openJson()
    memoryData = memory.openJson()

    memoryData['loggedin'] = username
    memoryData['admin'] = usersData[username]['admin']
    memoryData['path'] = path

    memory.closeJson(memoryData)
