import os
from root.miware.jsonCommon import *
import colorama
import runpy
import traceback
from colorama import *
from root.miware.terminal.commands.resource import *
import winsound

def handle(data):
    path = get_path()
    command_map = make_map()
    if check_if_command_exists(data) is True:
        update_memory(data)
        try:
            run_command('{0}\\root\\miware\\terminal\\commands\\{1[args][0]}.py'.format(path, data))
        except Exception:
            print(Style.BRIGHT + Fore.RED + "An Exception occurred while running '{}'.\nError Log can be found at root\\miware\\error_log.txt".format(data['args'][0]) + Style.RESET_ALL)
            winsound.PlaySound('{}\\root\\miware\\sounds\\error.wav'.format(path), winsound.SND_ASYNC)
            exc = traceback.format_exc()

            with open('{}\\root\\miware\\error_log.txt'.format(path), 'w') as f:
                f.write(exc)

            return
    else:
        return print(colorama.Fore.RED + 'Unknown command! ' + colorama.Fore.RESET + 'Type \'help\' for help.')

def make_map():
    path = get_path()
    files = os.listdir('{}\\root\\miware\\terminal\\commands'.format(path))
    command_map = []
    for file in files:
        if file != 'resource.py' and file != '__init__.py':
            command_map.append(file.split('.')[0])


    return command_map

def check_if_command_exists(data):
    command_map = make_map()
    for cmd in command_map:
        if data['args'][0] == cmd:
            return True

    # Else
    return False

def update_memory(data):
    path = get_path()
    json = JsonShort('{}\\root\\miware\\terminal\\json\\memory.json'.format(path))
    memory = json.openJson()
    memory['args'] = data['args']
    memory['full'] = ' '.join(data['args'])
    memory['path'] = data['path']

    json.closeJson(memory)

def run_command(file):
    runpy.run_path(file)