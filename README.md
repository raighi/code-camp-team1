# code-camp-team1

## Overview
A simple command-line tool to manage tasks stored in a JSON file.
Each task has a unique ID and a description.

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
| `details` | `add`, `modify` | string (rest of line) | Task description. For `modify`, replaces the description for `id`. Quote if it contains spaces. | "Buy milk" |


## Arguments
| Argument | Optional for | Type | Description | Example |
|----------|--------------|------|-------------|---------|
| `-u`, `--user` | `add`, `modify` | literal | Specifies which user the task belongs to. (if no new description is informed calling modify it keeps the old one) | `python src/main.py tasks.json modify 0 -u AloisHasNeurons` |

---
## Other infos

When adding a task, an estimatation of the duration is asked. When an user want to end a task he has to notify how many seconds he needed to complete the task in his command.

Adding a new task to a non-preexistent file will result to the creation of the said file. Any other command to a non-preexistent file will result to a "no such file or directory" error.

For the compliance check : id are positive integers, details are strings of characters, the files are json files, users are strings of characters, est_time and end_time are positive integers representing time in seconds.
## File Format
Tasks are stored as `<ID>\t<description>` per line.

---

## Tests
Run tests with:
```bash
python -m unittest tests/test_commands.py
```
