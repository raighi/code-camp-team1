def get_tasks(file):
    """
    Reads tasks from a file and returns a list of dictionnaries.
    """
    tasks = []
    try:
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 3:
                    id, description, est_time = parts
                    tasks.append({'id': id, 'description': description, 'est_time': est_time})
                if len(parts) == 4:
                    id, description, user, est_time = parts
                    tasks.append({'id': id, 'description': description, 'user': user, 'est_time': est_time})
    except (FileNotFoundError, PermissionError) as e:
        print("WARNING:", e)
        pass  # So that the file can be created
    return tasks


def add(details, file, user):
    tasks = get_tasks(file)
    new_id = 0
    while True:
        estimated_time = input("Please enter the estimated time of the task (in seconds): ")
        try:
            time_value = int(estimated_time)
            if time_value >= 0:
                break
            else:
                print("Error: Time must be a positive number or zero.")
        except ValueError:
            print("Error: Please enter a valid integer number.")
    if tasks:
        new_id = int(tasks[-1]['id'])+1
    if user:
        entry = f"{new_id}\t{details}\t{user}\t{estimated_time}\n"
    else:
        entry = f"{new_id}\t{details}\t \t{estimated_time}\n"
    with open(file, 'a') as f:
        f.write(entry)
    print(f"Succesfully added task {details} (ID: {new_id})")


def modify(id, file, new_details, new_user):
    try:
        tasks = get_tasks(file)
        task_found = False
        with open(file, 'w') as f:
            for task in tasks:
                if task['id'] == id:
                    # Use existing values if new ones are defaults
                    details_to_use = task['description'] if new_details == "no details" else new_details
                    user_to_use = task.get('user') if new_user == "unknown" else new_user

                    # Write entry based on whether user exists
                    if user_to_use:
                        entry = f"{id}\t{details_to_use}\t{user_to_use}\n"
                    else:
                        entry = f"{id}\t{details_to_use}\n"

                    f.write(entry)
                    task_found = True
                else:
                    # Preserve original task format
                    if 'user' in task:
                        f.write(f"{task['id']}\t{task['description']}\t{task['user']}\n")
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
        max_user_len = max(len("user"), *(len(task.get('user', '')) for task in tasks))
        max_est_time_len = max(len("estimated time"), *(len(task.get('est_time', '')) for task in tasks))

        header = f"| {'id':<{id_width}} | {'description':<{max_desc_len}} | {'user':<{max_user_len}} | {'estimated time':<{max_est_time_len}} |"
        divider = "+" + "-" * (id_width + 3) + "+" + "-" * (max_desc_len + 2) + "+" + "-" * (max_user_len + 2) + "+" + "-" * (max_est_time_len + 2) + "+"

        print(divider)
        print(header)
        print(divider)

        for task in tasks:
            if 'user' in task:
                print(f"| {task['id']:<{id_width}}  | {task['description']:<{max_desc_len}} | "
                      f"{task['user']:<{max_user_len}} | {task['est_time']:<{max_est_time_len}} |")
            else:
                print(f"| {task['id']:<{id_width}}  | {task['description']:<{max_desc_len}} | {'-':<{max_user_len}} |"
                      f"{task['est_time']:<{max_est_time_len}} |")

        print(divider)

    except (FileNotFoundError, PermissionError) as e:
        raise e
