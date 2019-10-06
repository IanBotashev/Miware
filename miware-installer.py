import json
import os
import shutil
import traceback
import win32com.client
import pythoncom

def main():
    """
    turns config.json (which compiler.py compiled) back into folders and files.
    :return:
    """
    try:
        input('Welcome to MiWare Installer!\n\nWhen you press Enter, the installation will begin.\nDependecies: Colorama, Python\nDependecies are things which are required for miware to run. Which you will have to install.\n>')
        install_all_items()
        create_new_user()
        create_shortcut()
        print('Fully done with installation!')
    except Exception:
        traceback.print_exc()
        print('An error happened! Please tell the developer about this!')

def create_new_user():
    print("\nLet's create an account.")
    path = os.getcwd()
    username = input('Username: ')
    password = input('Password: ')

    users = open("{}\\root\\miware\\terminal\\json\\users.json".format(path), 'r')
    users_data = users.read()
    data = json.loads(users_data)

    data.update({username: {"password": password, "admin": True}})
    os.mkdir('{0}\\root\\{1}'.format(path, username))

    with open("{}\\root\\miware\\terminal\\json\\users.json".format(path), 'w') as f_users:
        json.dump(data, f_users)

    json_file = open("{}\\root\\miware\\terminal\\json\\main.json".format(path), 'r')
    json_data = json_file.read()
    main_data = json.loads(json_data)

    main_data['main_admin'] = username
    main_data['path'] = path

    with open("{}\\root\\miware\\terminal\\json\\main.json".format(path), 'w') as f_main:
        json.dump(main_data, f_main)

def install_all_items():
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        shutil.rmtree(".\\root")
        print('An error occurred!\nNo config.json found. Put it in the SAME directory as this installer.')
        exit()
    try:
        print('Creating all directories needed...')
        for dir in data['dirs']:
            os.mkdir(dir)

        print('Done!\nCreating all files needed...')
        for file in data['files']:
            with open('{0}\\{1}'.format(file['location'], file['name']), 'w', encoding='latin1') as f:
                f.write(file['contents'])

        print('Done!')
    except FileExistsError:
        print('Please fully delete all previous miware files before downloading a new one.')
        exit()

def create_shortcut():
    pathcwd = os.getcwd()
    path = os.path.join(pathcwd, 'Miware.lnk')
    target =os.path.join(pathcwd, 'root\\miware\\main.py')

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WindowStyle = 7  # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()

if __name__ == '__main__':
    main()
