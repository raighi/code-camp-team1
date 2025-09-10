def get_tasks(file):
    """
    Reads tasks from a file and returns a list of dictionnaries.
    """
    tasks = []
    try:
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split("\t", 1)
                if len(parts) == 2:
                    id, description = parts
                    tasks.append({'id': id, 'description': description})
    except (FileNotFoundError, PermissionError) as e:
        print("WARNING:", e)
        pass  # So that the file can be created
    return tasks


def add(details, file):
    tasks = get_tasks(file)
    new_id = 0
    if tasks:
        new_id = int(tasks[-1]['id'])+1
    entry = f"{new_id}\t{details}\n"
    with open(file, 'a') as f:
        f.write(entry)
    print(f"Succesfully added task {details} (ID: {new_id})")


def modify(id, file, new_details):
    try:
        tasks = get_tasks(file)
        task_found = False
        with open(file, 'w') as f:
            for task in tasks:
                if task['id'] == id:
                    f.write(f"{id}\t{new_details}\n")
                    task_found = True
                else:
                    f.write(f"{task['id']}\t{task['description']}\n")

        if task_found:
            print(f"Successfully modified task {id}.")
        else:
            raise ValueError(f"ID {id} not found in {file}")

    except (FileNotFoundError, PermissionError) as e:
        raise e


def rm(id, file):
    try:
        tasks = get_tasks(file)
        task_found = False
        with open(file, 'w') as f:
            for task in tasks:
                if task['id'] == id:
                    task_found = True
                else:
                    f.write(f"{task['id']}\t{task['description']}\n")

        if task_found:
            print(f"Successfully removed task {id}.")
        else:
            raise ValueError(f"ID {id} not found in {file}")

    except (FileNotFoundError, PermissionError) as e:
        raise e


def show(file):
    try:
        tasks = get_tasks(file)
        if not tasks:
            print("No tasks found.")
            return

        tasks.sort(key=lambda x: x['id'])

        id_width = max(len(task['id']) for task in tasks)
        max_desc_len = max(len("description"), *(len(task['description']) for task in tasks))

        header = f"| {'id':<{id_width}} | {'description':<{max_desc_len}} |"
        divider = "+" + "-" * (id_width + 2) + "+" + "-" * (max_desc_len + 2) + "+"

        print(divider)
        print(header)
        print(divider)

        for task in tasks:
            print(f"| {task['id']:<{id_width}} | {task['description']:<{max_desc_len}} |")

        print(divider)

    except (FileNotFoundError, PermissionError) as e:
        raise e
