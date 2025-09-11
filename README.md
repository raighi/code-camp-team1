# code-camp-team1

## Overview
A simple command-line tool to manage tasks stored in a text file.
Each task has a unique ID and a description.

---

## Commands

| Command         | Description                          | Usage Example                     |
|-----------------|--------------------------------------|-----------------------------------|
| `add`           | Add a new task.                      | `python src/main.py tasks.txt add "Buy milk"` |
| `modify`        | Update a task by ID.                 | `python src/main.py tasks.txt modify "12345678" "Buy bread"` |
| `rm`            | Remove a task by ID.                 | `python src/main.py tasks.txt rm "12345678"` |
| `show`          | Display tasks in a formatted table.  | `python src/main.py tasks.txt show`      |
| `end`           | End a task and specify the duration  | `python src/main.py tasks.txt end "12345678" "90"`|

## Positional arguments

| Argument | Required for | Type | Description | Example |
|----------|--------------|------|-------------|---------|
| `file`   | all commands | path | Path to the tasks file. Created on `add` if missing. | `tasks.txt` |
| `command` | all commands | literal | One of `add`, `modify`, `rm`, `show`. | `add` |
| `id` | `modify`, `rm` | 8-char hex | Task identifier printed by `add` or shown by `show`. | `1a2b3c4d` |
| `details` | `add`, `modify` | string (rest of line) | Task description. For `modify`, replaces the description for `id`. Quote if it contains spaces. | "Buy milk" |


## Arguments
| Argument | Required for | Type | Description | Example |
|----------|--------------|------|-------------|---------|
| `-u`, `--user` | `add`, `modify` | literal | Specifies which user the task belongs to. | `-u AloisHasNeurons` | 

---
## Other infos

When adding a task, an estimatation of the duration is asked. When an user want to end a task he has to notify how many seconds he needed to complete the task in his command.

Adding a new task to a non-preexistent file will result to the creation of the said file. Any other command to a non-preexistent file will result to a "no such file or directory" error.
## File Format
Tasks are stored as `<ID>\t<description>` per line.

---

## Tests
Run tests with:
```bash
python -m unittest tests/test_commands.py
```
