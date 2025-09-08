# Implementation of commands, using functions in the core module
def add(details, filename, tasks):
    with open(filename, 'a') as f:
        task = add(tasks, details)
        f.write(task)
    print(f"Succesfully added task {task[0]} ({task[1]})")


def get_ids(file):
    with open(file, 'r') as f:
        items = f.readlines()
        return items[1::2]


def get_descriptions(file):
    with open(file, 'r') as f:
        items = f.readlines()
        return items[0::2]


def rm(id, file, tasks):
    try:
        if id in get_ids(file):
            with open(file, 'r') as f:
                lines = f.readlines()
            with open(file, 'w') as f:
                for line in lines:
                    if not line.startswith(id):
                        f.write(line)
        else:
            raise ValueError(f"ID {id} not found in {file}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file} not found")
    except PermissionError:
        raise PermissionError(f"Permission denied for {file}")
