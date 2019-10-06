import os
import json

def main():
    """
    Compiler used for compiling new versions.
    :return:
    """
    result = {'dirs': [], 'files': []}

    for item in os.walk('.\\root'):
        path = item[0]

        result['dirs'].append(path)

        for file in item[2]:
            with open('{}\\{}'.format(path, file), 'r', encoding="latin1") as f:
                if file == 'users.json':
                    contents = "{}"
                else:
                    contents = f.read()
            result['files'].append({"name": file, "location": path, "contents": contents})

    with open('config.json', 'w') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main()
