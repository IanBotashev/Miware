import requests
from root.miware.terminal.commands.resource import *

def main():
    memory = get_memory()
    args = get_args(memory['full'])

    if args is False:
        return print('usage:\nweb [web-address] [opt: file name]\nOutcome: Downloads a file from the website specified')

    print('Starting download process...')
    r = requests.get(args[0])
    try:
        filename = args[1]
    except IndexError:
        filename = args[0].split('/')[-1]

    with open(filename, 'wb') as f:
        f.write(r.content)

    print('Successfully downloaded: "{}"'.format(filename))


if __name__ == "__main__":
    pass
else:
    print("Web has been put off limits, as it is incredibly unstable.")
    # main()
    pass
