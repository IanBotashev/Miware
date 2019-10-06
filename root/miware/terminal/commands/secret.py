from root.miware.terminal.commands.resource import *

def main():
    print('You found a secret!\nHere\'s some cookies!')
    print("""
                 _    _           
                | |  (_)          
  ___ ___   ___ | | ___  ___  ___ 
 / __/ _ \ / _ \| |/ / |/ _ \/ __|
| (_| (_) | (_) |   <| |  __/\__ \\
 \___\___/ \___/|_|\_\_|\___||___/""")
    print(Back.RED + 'I mean, what were you expecting really?' + Style.RESET_ALL)


if __name__ == "__main__":
    pass
else:
    main()
