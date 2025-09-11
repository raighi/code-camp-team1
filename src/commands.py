def get_tasks(file):
    """
    Reads tasks from a file and returns a list of dictionaries.
    Handles formats:
    - id\tdescription\test_time
    - id\tdescription\tuser\test_time
    - id\tdescription\t\test_time\tend_time (no user, with end_time)
    - id\tdescription\tuser\test_time\tend_time
    """
    tasks = []
    try:
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 3:
                    # Format: id\tdescription\test_time
                    id, description, est_time = parts
                    tasks.append({
                        'id': id,
                        'description': description,
                        'est_time': est_time
                    })
                elif len(parts) == 4:
                    # Format: id\tdescription\tuser\test_time or id\tdescription\test_time\tend_time
                    id, description, third_part, fourth_part = parts
                    if third_part and not third_part.isdigit():  # Non-empty user, not an integer time
                        # Format: id\tdescription\tuser\test_time
                        user, est_time = third_part, fourth_part
                        tasks.append({
                            'id': id,
                            'description': description,
                            'user': user,
                            'est_time': est_time
                        })
                    else:  # No user, but maybe an end_time
                        est_time, end_time = third_part, fourth_part
                        tasks.append({
                            'id': id,
                            'description': description,
                            'est_time': est_time,
                            'end_time': end_time
                        })
                elif len(parts) == 5:
                    # Format: id\tdescription\tuser\test_time\tend_time
                    id, description, user, est_time, end_time = parts
                    if user.strip():  # Non-empty user
                        tasks.append({
                            'id': id,
                            'description': description,
                            'user': user,
                            'est_time': est_time,
                            'end_time': end_time
                        })
                    else:  # Empty user field
                        tasks.append({
                            'id': id,
                            'description': description,
                            'est_time': est_time,
                            'end_time': end_time
                        })
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
        new_id = int(tasks[-1]['id']) + 1
    if user:
        entry = f"{new_id}\t{details}\t{user}\t{estimated_time}\n"
    else:
        entry = f"{new_id}\t{details}\t\t{estimated_time}\n"  # Consistent empty user
    with open(file, 'a') as f:
        f.write(entry)
    print(f"Successfully added task {details} (ID: {new_id})")


def modify(id, file, new_details, new_user, new_est_time):
    try:
        tasks = get_tasks(file)
        task_found = False
        with open(file, 'w') as f:
            for task in tasks:
                if task['id'] == id:
                    details_to_use = task['description'] if new_details == "no details" else new_details
                    user_to_use = task.get('user') if new_user is None else new_user
                    est_time_to_use = str(new_est_time) if new_est_time is not None else task['est_time']

                    entry_parts = [id, details_to_use]
                    if user_to_use:
                        entry_parts.append(user_to_use)
                    else:
                        entry_parts.append("")
                    entry_parts.append(est_time_to_use)

                    if 'end_time' in task:
                        entry_parts.append(task['end_time'])

                    entry = "\t".join(entry_parts) + "\n"
                    f.write(entry)
                    task_found = True
                else:
                    # Preserve other tasks in their original format
                    if 'user' in task and task['user']:
                        entry_parts = [task['id'], task['description'], task['user'], task['est_time']]
                    else:
                        entry_parts = [task['id'], task['description'], '', task['est_time']]

                    if 'end_time' in task:
                        entry_parts.append(task['end_time'])

                    entry = "\t".join(entry_parts) + "\n"
                    f.write(entry)

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
                    # Preserve all fields of remaining tasks
                    entry_parts = [task['id'], task['description']]
                    if 'user' in task and task['user']:
                        entry_parts.append(task['user'])
                    else:
                        entry_parts.append('')

                    entry_parts.append(task['est_time'])

                    if 'end_time' in task:
                        entry_parts.append(task['end_time'])

                    entry = "\t".join(entry_parts) + "\n"
                    f.write(entry)

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

        tasks.sort(key=lambda x: int(x['id']))  # Fixed to sort by int

        id_width = max(len(task['id']) for task in tasks)
        max_desc_len = max(len("description"), *(len(task['description']) for task in tasks))
        max_user_len = max(len("user"), *(len(task.get('user', '')) for task in tasks))
        max_est_time_len = max(len("est. time"), *(len(str(task.get('est_time', ''))) for task in tasks))
        max_end_time_len = max(len("end time"), *(len(str(task.get('end_time', ''))) for task in tasks))

        header = f"| {'id':<{id_width}} | {'description':<{max_desc_len}} | {'user':<{max_user_len}} | {'est. time':<{max_est_time_len}} | {'end time':<{max_end_time_len}} |"
        divider = "+" + "-" * (id_width + 3) + "+" + "-" * (max_desc_len + 2) + "+" + "-" * (max_user_len + 2) + "+" + "-" * (max_est_time_len + 2) + "+" + "-" * (max_end_time_len + 2) + "+"

        print(divider)
        print(header)
        print(divider)

        for task in tasks:
            end_time_display = task.get('end_time', '-')
            if 'user' in task:
                print(f"| {task['id']:<{id_width}}  | {task['description']:<{max_desc_len}} | "
                      f"{task['user']:<{max_user_len}} | {task['est_time']:<{max_est_time_len}} | {end_time_display:<{max_end_time_len}} |")
            else:
                print(f"| {task['id']:<{id_width}}  | {task['description']:<{max_desc_len}} | {'-':<{max_user_len}} | "
                      f"{task['est_time']:<{max_est_time_len}} | {end_time_display:<{max_end_time_len}} |")

        print(divider)

    except (FileNotFoundError, PermissionError) as e:
        raise e


def endTask(file, id, end_time):
    """
    Marks a task as completed by adding an end_time.
    Handles all possible task formats and preserves existing structure.
    """
    try:
        tasks = get_tasks(file)
        if not tasks:
            print("No tasks found.")
            return

        task_found = False
        with open(file, 'w') as f:
            for task in tasks:
                if task['id'] == id:
                    if task.get('end_time'):  # Correctly checks if end_time key exists and is not empty
                        print(f"ERROR: task {id} already has an end time.")
                        return
                    # Task being ended - add end_time
                    entry_parts = [task['id'], task['description']]
                    if 'user' in task and task['user']:
                        entry_parts.append(task['user'])
                    else:
                        entry_parts.append('')

                    entry_parts.extend([task['est_time'], end_time])

                    f.write("\t".join(entry_parts) + "\n")
                    task_found = True
                else:
                    # Preserve other tasks in their original format
                    entry_parts = [task['id'], task['description']]
                    if 'user' in task and task['user']:
                        entry_parts.append(task['user'])
                    else:
                        entry_parts.append('')

                    entry_parts.append(task['est_time'])

                    if 'end_time' in task:
                        entry_parts.append(task['end_time'])

                    f.write("\t".join(entry_parts) + "\n")

        if task_found:
            print(f"Successfully marked task {id} as completed.")
        else:
            raise ValueError(f"ID {id} not found in {file}")

    except (FileNotFoundError, PermissionError) as e:
        raise e
