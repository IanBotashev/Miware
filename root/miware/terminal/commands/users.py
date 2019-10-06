from root.miware.jsonCommon import *
from colorama import *
from root.miware.terminal.commands.resource import get_path

def main():
    users_json = JsonShort('{}\\root\\miware\\terminal\\json\\users.json'.format(get_path()))
    users_data = users_json.openJson()

    for user in users_data:
        print('{0}; admin: {1}'.format(user, users_data[user]['admin']))
    print(Fore.GREEN + 'Total # of Users: {}'.format(len(users_data)) + Fore.RESET)


if __name__ == "__main__":
    pass
else:
    main()
