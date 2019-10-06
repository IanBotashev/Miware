from root.miware.terminal.commands.resource import *
import os
import subprocess
import sys

def main():
    memory= get_memory()
    args= get_args(memory['full'])

    if args is False:
        return print('usage: exec [file]')
    path = os.path.join(memory['path'], args[0])

    if os.path.isfile(path) is False:
        return Colors.error(Colors(), 'File does not exist, or it is a Directory.')

    subprocess.call([sys.executable, path])


if __name__ == "__main__":
    pass
else:
    main()
