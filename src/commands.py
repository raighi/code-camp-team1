import core


# Implementation of commands, using functions in the core module
def add(details, filename, tasks):
    with open(filename, 'a') as f:
        task = core.add(tasks, details)
        f.write(task)
    print(f"Succesfully added task {task[0]} ({task[1]})")
