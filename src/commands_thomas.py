# Implementation of commands, using functions in the core module
def add(details, filename, tasks):
    if len(tasks) == 0:
        new_id = 1
    else:
        last = tasks[-1]
        last_id = int(last.split(' ')[0])
        new_id = last_id + 1
    with open(filename, 'a') as f:
        task = details
        f.write(str(new_id)+' '+task+'\n')
    print(f"Succesfully added task {new_id} ({task})")
    return new_id

def modify(id, details, filename, tasks):
    new_tasks = []
    for i in range(len (tasks)):
        task_id = int(tasks[i].split(' ')[0])
        if task_id == id:
            line = str(id) + ' ' + details + '\n'
        else :
            line = tasks[i]
        new_tasks.append(line)
    with open(filename, 'w') as f:
        f.writelines(new_tasks)
    print(f"Succesfully modified task {id} ({details})")
            