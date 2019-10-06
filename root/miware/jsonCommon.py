import json, os

class JsonShort:
    """A class for making it easier opening json files, and dumping data on json files."""
    def __init__(self, file):
        self.file = file
        if os.path.exists(file) is not True:
            raise FileNotFoundError('File Not found: {}'.format(file))

    def openJson(self):
        """Open a json file."""
        json_file = open(self.file, 'r')
        json_data = json_file.read()
        result = json.loads(json_data)
        return result

    def closeJson(self, data):
        """Close a json file, and dump data in it."""
        with open(self.file, 'w') as f:
            json.dump(data, f)
