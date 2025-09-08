# code-camp-team1

## Overview
A simple command-line tool to manage tasks stored in a text file.
Each task has a unique ID and a description.

---

## Commands

| Command         | Description                          | Usage Example                     |
|-----------------|--------------------------------------|-----------------------------------|
| `add`           | Add a new task.                      | `main.py tasks.txt add "Buy milk"` |
| `modify`        | Update a task by ID.                 | `main.py tasks.txt modify "12345678" "Buy bread"` |
| `rm`            | Remove a task by ID.                 | `main.py tasks.txt rm "12345678"` |
| `show`          | Display tasks in a formatted table.  | `main.py tasks.txt show`      |

---

## File Format
Tasks are stored as `<ID>\t<description>` per line.

---

## Tests
Run tests with:
```bash
python -m unittest tests/test_commands.py
```
