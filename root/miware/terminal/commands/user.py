from root.miware.terminal.commands.resource import *
import shutil


def delete_user(path, memory):

    username = input('Username: ')

    if memory['loggedin'] != username:
        if check_admin(memory) is False:
            if prompt_admin_password() is False:
                return
    else:
        return print(Fore.RED + "Cannot delete the user you're currently logged in." + Style.RESET_ALL)

    users = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(path))
    users_data = users.openJson()

    main_json = JsonShort('{}\\root\\miware\\terminal\\json\\main.json'.format(path))
    main_data = main_json.openJson()


    if main_data['main_admin'] == username:
        return print(Style.BRIGHT + Fore.RED + "Cannot delete main admin." + Style.RESET_ALL)

    if check_if_user_exists(username) is False:
        return print(Style.BRIGHT + Fore.RED + "User '{0}' does not exist.".format(username) + Style.RESET_ALL)

    shutil.rmtree('{0}\\root\\{1}'.format(path, username))

    del users_data[username]
    users.closeJson(users_data)
    print(Style.BRIGHT + Fore.GREEN + 'Successfully deleted user "{0}"'.format(username) + Style.RESET_ALL)


def create_user(path):
    username = input('Username: ')
    password = input('Password: ')
    admin_input = input('Admin: ')

    if admin_input.lower() == 'false':
        admin = False
    elif admin_input.lower() == 'true':
        admin = True
    else:
        return print(Style.BRIGHT + Fore.RED + 'Please do False/True.'.format(username) + Style.RESET_ALL)

    users = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(path))
    users_data = users.openJson()

    for user in users_data:
        if user == username:
            return print(Style.BRIGHT + Fore.RED + "There's already a user named that." + Style.RESET_ALL)

    users_data.update({username: {"password": password, "admin": admin}})
    os.mkdir('{0}\\root\\{1}'.format(path, username))

    users.closeJson(users_data)

    print(Style.BRIGHT + Fore.GREEN + 'Successfully created user "{0}"'.format(username) + Style.RESET_ALL)


def main():
    memory = get_memory()
    args = get_args(memory['full'])
    path = get_path()

    if args is False:
        return print('usage: user\nuser delete - delete a user.\nuser create - create a user')

    if check_admin(memory) is False:
        if prompt_admin_password() is False:
            return

    if ask_true_or_false() is False:
        return

    if args[0] == 'delete':
        delete_user(path, memory)

    elif args[0] == 'create':
        create_user(path)

if __name__ == '__main__':
    pass
else:
    main()
