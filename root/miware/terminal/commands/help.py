
def main():
    command_map = ['help - Returns this message',
                   'ls - Get all files and directories in current directory',
                   'cd [path] - Change current directory. Do \'..\' to go back a directory',
                   'mkdir [path/name] - Create a directory, accepts a path, and a name.',
                   'rmdir [path/name] [tree] - Delete a directory/tree, accepts a path, and a name.',
                   'content [path/name] - Print out the contents of a file. Accepts a path, and a name.',
                   'logout',
                   'shutdown',
                   'createuser - Create a user',
                   'deleteuser - Delete a user',
                   'rm [path/name] - removes a file. Accepts a path, and a name.',
                   'edit [path/name] - allows you to edit a file.',
                   'exec [path/name] get the output of a file after running it.',
                   'lock [path/name] - lock a folder to only allow access for you.',
                   'web [website] - Download a file from the internet',]

    for command in command_map:
        print(command)

if __name__ == "__main__":
    pass
else:
    main()