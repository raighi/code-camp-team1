# code-camp-team1

## Overview
A simple command-line tool to manage tasks stored in a JSON file.
Each task has a unique ID, a description and an estimated time for completion, it can be associated with a user.

---

## Commands

| Command         | Description                          | Usage Example                                                |
|-----------------|--------------------------------------|--------------------------------------------------------------|
| `add`           | Add a new task.                      | `python src/main.py tasks.json add "Buy milk"`                |
| `modify`        | Update a task by ID.                 | `python src/main.py tasks.json modify "12345678" "Buy bread"` |
| `rm`            | Remove a task by ID.                 | `python src/main.py tasks.json rm "12345678"` |
| `show`          | Display tasks in a formatted table.  | `python src/main.py tasks.json show`      |
| `end`           | End a task and specify the duration  | `python src/main.py tasks.json end "12345678" "90"`|
| `create`           | Create a task and specify the first task and its duration  | `python src/main.py tasks.json create "Buy milk"`|

## Positional arguments

| Argument | Required for | Type | Description | Example |
|----------|--------------|------|-------------|---------|
| `file`   | all commands | path | Path to the tasks file. Created on `add` if missing. | `tasks.json` |
| `command` | all commands | literal | One of `add`, `modify`, `rm`, `show`, `end`. | `add` |
| `id` | `modify`, `rm` | int | Task identifier printed by `add` or shown by `show`. | `0` |
| `details` | `add`, `modify`,`create` | string (rest of line) | Task description. For `modify`, replaces the description for `id`. Quote if it contains spaces. | "Buy milk" |


## Arguments
| Argument | Optional for | Type | Description | Example |
|----------|--------------|------|-------------|---------|
| `-u`, `--user` | `add`, `modify`, `create` | literal | Specifies which user the task belongs to. (if no new description is informed calling modify it keeps the old one) | `python src/main.py tasks.json modify 0 -u AloisHasNeurons` |

---
## Other infos

When adding a task, an estimatation of the duration is asked. When an user want to end a task he has to notify how many seconds he needed to complete the task in his command.

Adding a new task to a non-preexistent file will result to the creation of the said file. Any other command to a non-preexistent file will result to a "no such file or directory" error.

For the compliance check : id are positive integers, details are strings of characters, the files are json files, users are strings of characters, est_time and end_time are positive integers representing time in seconds.


## File Format

The task data is stored in a JSON file with the following structure:

```json
[
  {
    "id": "0",
    "description": "task description",
    "est_time": "120",
    "user": "username",
    "end_time": "timestamp"
  },
  ...
]
```

Each file contains an array of task objects. Each task object has the following fields:

- `id` (string): A unique identifier for the task. IDs are assigned sequentially starting from 0.
- `description` (string): A description of the task.
- `est_time` (string): The estimated time required to complete the task, in seconds.
- `user` (string, optional): The user assigned to the task. If this field is not present, no user is assigned to the task.
- `end_time` (string, optional): The timestamp when the task was completed, represented as a Unix timestamp (seconds since epoch). This field is only present for completed tasks.

All field values are stored as strings, even for numeric values like `id`, `est_time`, and `end_time`.

The file must be a valid JSON array. Each task object must have at least the `id`, `description`, and `est_time` fields. The `user` and `end_time` fields are optional.

Example:

```json
[
  {
    "id": "0",
    "description": "super description",
    "est_time": "23",
    "user": "unknown"
  },
  {
    "id": "1",
    "description": "another task",
    "est_time": "345",
    "user": "michel",
    "end_time": "1625097600"
  }
]
```

In the example above:
- The first task does not have an `end_time`, indicating it is not yet completed.
- The second task has an `end_time`, indicating it has been completed. The value is a Unix timestamp (e.g., "1625097600" represents July 1, 2021).
- The `user` field is optional; if not present, no user is assigned to the task.



---
# Authors

Aloïs VINCENT, email : alois.vincent@imt-atlantique.net

Raphaël HIERSO, email : raphael.hierso-iglesias@imt-atlantique.net

Heitor SARDINHA GONÇALVES PAIVA, email : heitor.sardinha-goncalves-paiva@imt-atlantique.net

Thomas BRUYERE, email : thomas.bruyere@imt-atlantique.net

Ala ABDESSAYED, email : alaabdessaied@gmail.com

Mingyang WANG, email : mingyang.wang@imt-atlantique.net
