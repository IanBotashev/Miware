from root.miware.login import *
from colorama import *
import winsound
from root.miware.terminal.commands.resource import get_path
from root.miware.jsonCommon import *
from root.miware.updater import *

def bootup_main():
    login_main()
    play_sound()
    bootup_message()


def play_sound():
    path = "{}\\root\\miware\\sounds\\startup.wav".format(get_path())
    winsound.PlaySound(path, winsound.SND_ASYNC)

def get_changelogs():
    changelogs = JsonShort('{}\\root\\miware\\terminal\\json\\changelogs.json'.format(get_path()))
    return changelogs.openJson()

def print_changelogs(changelogs, main):
    print('\nChangelogs for {0}:'.format(main['version']))
    for change in changelogs['changelogs']:
        print('    -{}'.format(change))


def bootup_message():
    print("\nWelcome to " + Style.BRIGHT + Fore.LIGHTBLUE_EX + "MiWare" + Style.RESET_ALL)
    main = JsonShort('{}\\root\\miware\\terminal\\json\\main.json'.format(get_path()))
    data = main.openJson()

    print('Github page: https://github.com/TheMiotaS/miware')
    print('Current version: ' + Fore.GREEN + str(data['version']) + Style.RESET_ALL)
    print_changelogs(get_changelogs(), data)
