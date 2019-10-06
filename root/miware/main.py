from root.miware.terminal import handle
from root.miware.terminal.commands.resource import format_path, get_memory, get_path
from root.miware.login import *
from root.miware.bootup_sequence import *

def get_info(full, init_data):
    data = {
        "args": full.split(' '),
        "terminal_prefix": init_data['terminal_prefix'],
        "path": os.getcwd()
    }

    return data

def get_json_init_data(file):
    json = JsonShort(file)
    data = json.openJson()
    return json, data


def main():
    while True:
        path = get_path()
        json, init_data = get_json_init_data('{}\\root\\miware\\terminal\\json\\main.json'.format(path))
        formatString = (Style.BRIGHT + Fore.LIGHTBLUE_EX + get_memory()['loggedin'] + Style.RESET_ALL, Style.DIM + Fore.LIGHTGREEN_EX + format_path(get_memory()['path']) + Style.RESET_ALL, init_data['terminal_prefix'])
        full = input('{0[0]}@{0[1]}{0[2]}'.format(formatString))
        data = get_info(full, init_data)
        handle(data)


if __name__ == '__main__':
    bootup_main()
    main()
