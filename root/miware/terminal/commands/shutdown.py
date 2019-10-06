import winsound
from root.miware.terminal.commands.resource import *
import time

def play_sound():
    winsound.PlaySound('{}\\root\\miware\\sounds\\shutdown.wav'.format(get_path()), winsound.SND_ASYNC)



def main():
    play_sound()
    time.sleep(1.5)
    exit()


if __name__ == "__main__":
    pass
else:
    main()