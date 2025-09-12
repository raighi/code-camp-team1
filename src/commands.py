import json
import os


def get_tasks(file):
    """
    Reads tasks from a JSON file and returns a list of dictionaries.
    Each task has: id, description, est_time, and optionally user and end_time.
    """
    tasks = []
    try:
        if os.path.exists(file):
            with open(file, 'r') as f:
                content = f.read().strip()
                if content:
                    tasks = json.loads(content)
                else:
                    tasks = []
        else:
            tasks = []
    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        print("WARNING:", e)
        tasks = []
    return tasks


def save_tasks(file, tasks):
    """
    Saves tasks to a JSON file with proper formatting.
    """
    try:
        with open(file, 'w') as f:
            json.dump(tasks, f, indent=2)
    except (PermissionError, IOError) as e:
        raise e


def add(details, file, user):
    tasks = get_tasks(file)

    while True:
        est_time = input("Please enter the estimated time of the task (in seconds): ")
        try:
            time_value = int(est_time)
            if time_value >= 0:
                break
            else:
                print("Error: Time must be a positive number or zero.")
        except ValueError:
            print("Error: Please enter a valid integer number.")

    # Find next ID
    new_id = 0
    if tasks:
        new_id = max(int(task['id']) for task in tasks) + 1

    # Create new task
    new_task = {
        'id': str(new_id),
        'description': details,
        'est_time': str(est_time)
    }

    if user:
        new_task['user'] = user

    tasks.append(new_task)
    save_tasks(file, tasks)
    print(f"Successfully added task {details} (ID: {new_id})")


def modify(id, file, new_details, new_user):
    print(new_details)
    try:
        tasks = get_tasks(file)
        task_found = False

        for task in tasks:
            if task['id'] == id:
                # Update task fields
                if new_details != "no details":
                    task['description'] = new_details

                if new_user != "unknown":
                    if new_user:
                        task['user'] = new_user
                    else:
                        # Remove user field if empty string is passed
                        task.pop('user', None)
                task_found = True
                break

        if task_found:
            save_tasks(file, tasks)
            print(f"Successfully modified task {id}.")
        else:
            raise ValueError(f"ID {id} not found in {file}")

    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        raise e


def rm(id, file):
    try:
        tasks = get_tasks(file)
        task_found = False

        # Filter out the task with the specified ID
        updated_tasks = []
        for task in tasks:
            if task['id'] == id:
                task_found = True
            else:
                updated_tasks.append(task)

        if task_found:
            save_tasks(file, updated_tasks)
            print(f"Successfully removed task {id}.")
        else:
            raise ValueError(f"ID {id} not found in {file}")

    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        raise e


def show(file):
    try:
        tasks = get_tasks(file)
        if not tasks:
            print("No tasks found.")
            return

        # Sort tasks by ID
        tasks.sort(key=lambda x: int(x['id']))

        # Calculate column widths
        id_width = max(len("id"), max(len(task['id']) for task in tasks))
        max_desc_len = max(len("description"), max(len(task['description']) for task in tasks))
        max_user_len = max(len("user"), max(len(task.get('user', '')) for task in tasks))
        max_est_time_len = max(len("est. time"), max(len(str(task.get('est_time', ''))) for task in tasks))
        max_end_time_len = max(len("end time"), max(len(str(task.get('end_time', ''))) for task in tasks))

        # Create table header
        header = f"| {'id':<{id_width}} | {'description':<{max_desc_len}} | {'user':<{max_user_len}} | {'est. time':<{max_est_time_len}} | {'end time':<{max_end_time_len}} |"
        divider = "+" + "-" * (id_width + 2) + "+" + "-" * (max_desc_len + 2) + "+" + "-" * (max_user_len + 2) + "+" + "-" * (max_est_time_len + 2) + "+" + "-" * (max_end_time_len + 2) + "+"

        print(divider)
        print(header)
        print(divider)

        # Print each task
        for task in tasks:
            user_display = task.get('user', '-')
            end_time_display = task.get('end_time', '-')

            print(f"| {task['id']:<{id_width}} | {task['description']:<{max_desc_len}} | "
                  f"{user_display:<{max_user_len}} | {task['est_time']:<{max_est_time_len}} | {end_time_display:<{max_end_time_len}} |")

        print(divider)

    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        raise e


def endTask(file, id, end_time):
    """
    Marks a task as completed by adding an end_time.
    """
    try:
        tasks = get_tasks(file)
        if not tasks:
            print("No tasks found.")
            return

        task_found = False
        for task in tasks:
            if task['id'] == id:
                if task.get('end_time'):
                    print(f"ERROR: task {id} already has an end time.")
                    return

                # Add end_time to the task
                task['end_time'] = end_time
                task_found = True
                break

        if task_found:
            save_tasks(file, tasks)
            print(f"Successfully marked task {id} as completed.")
        else:
            raise ValueError(f"ID {id} not found in {file}")

    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        raise e
