# Miware
A sort of "os" on windows.

## Information
* Python Version: Python 3.7
* Miware Version: Miware 1.1

### Installation
If you would like to install miware,
1. download miware-installer.py 
2. grab the most recent config.json
3. download all dependecies required.  
Then, put miware-installer, and config both into the directory you want to install miware at, run miware-installer, and you're good to go!

### Dependecies

The dependecies which Miware uses on a normal runtime:
* Colorama
* Winsound
* Os

The dependecies which the miware installer uses on a normal runtime is:
* pywin32

### Normal Runtime

#### main
This is what runs miware itself, if you would like to run miware, you should start this file, as it the "root" of all miware.

The way it works is, it's a while true loop, which gathers info for the handler, information such as:
* Path to .root
* The command which the user inputs

It then passes this info onto handler.

#### Handler
Handler is what handles all inputs made by the user, it checks if the command pinged exists, and if it does, it commits some information onto memory.json, and then runs the file the command is in.

#### Memory.json
Memory.json is where all the important data is stored per command inputed. The data which memory holds is:
* args, full command split into words, and the command itself being deleted from the beginning.
* full, contains the full command which the user inputed, unedited.
* path, the path from where the command was executed.
* loggedin, the current person loggedin
* admin, True if the current person loggedin is an admin, else it is False.

#### main.json
Contains data, which is not used like memory.json, but instead should not be edited, and contains most important data.
* terminal_prefix, probably to be removed, the ">" after "user@path/to/somewhere"
* main_admin, the main admin on a system, this admin has more power over the others, and cannot be normally removed.
* path, the path beyond "./root"
* version, current miware version.

#### users.json
Contains the data of all users, this data will soon to be all encrypted.
* {username}, the username of a user. This object contains all other data held with user.
* {password}, the password of a user.
* admin, either set to True or False

### Startup
All startup sequences are held in bootup_sequence.py
All it does is, make the user log in, print out the current version, and prints out the changelogs, which can be found at changelogs.json.

### Commands
All commands are held in /root/miware/terminal/commands
Each command is a .py file, and what miware does it runs the files.

#### resource.py
Resource.py is not a command, and is excluded from the command map by miware, it contains resources which the commands can use, such as:
* get_path, gets the path from where a command was executed
* get_memory, gets the data from memory.json
* get_args, gets the args of which the user executed with the command.
* format_path, formats the path to only start from root
* check_admin, checks if the current logged in person is an admin, returns True if yes, else returns False
* prompt_admin_password, if the user is not admin, you can ask the user for the main admins password, returns True if it was correct
* ask_true_or_false, asks the user if they are sure. returns True if 'y' else returns False.
* check_if_user_exists, check if a user exists
* check_locked_dir, check if a directory is locked only for a user.
* Colors, mostly unused. Most likely to be deleted by 1.5
