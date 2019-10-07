from github import Github
from root.miware.jsonCommon import *
from root.miware.terminal.commands.resource import get_path

# In-progress.

def updater_main():
    updater = Updater()
    updater.check_differences()

class Updater:
    def __init__(self):
        self.json = JsonShort('{0}\\root\\miware\\terminal\\json\\gitkey.json'.format(get_path()))
        self.data = self.json.openJson()
        self.github = Github(self.data['user'], self.data['password'])
        self.github_repo = self.github.get_repo('TheMiotaS/Miware')
        self.contents = self.github_repo.get_contents("root")

    def check_differences(self):
        while self.contents:
            file_content = self.contents.pop(0)
            if file_content.type == "dir":
                print(self.github_repo.get_contents(file_content.path))
            else:
                print(file_content)