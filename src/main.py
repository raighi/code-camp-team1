# !/usr/bin/env python3
import commands
from options import create_parser


def main():
    """
    Main entry point for the task management command-line application.

    Parses command-line arguments and executes the appropriate command based on the
    provided options. Supports task management operations including adding, creating,
    modifying, removing, displaying, and ending tasks.

    Supported commands:
        - add: Add a new task with details and user
        - create: Create a new task file with initial task
        - modify: Modify an existing task's details and user
        - rm: Remove a task by ID
        - show: Display all tasks from the file
        - end: Mark a task as completed with end time

    Raises:
        Exception: Catches and displays any errors that occur during command execution.
    """
    options = create_parser().parse_args()  # Get command-line options
    try:
        # tasks = core.read_tasks(options.file)
        if options.command == 'add':   # Case for the add command
            # Call the add function and assign parameters retrieved by the parser
            commands.add(details=' '.join(options.details), user=' '.join(options.user), file=options.file)
        if options.command == 'create':   # Case for the create command
            # Call the create function and assign parameters retrieved by the parser
            commands.create(new_file=options.file, new_details=' '.join([options.new_details]),
                            new_user=' '.join(options.new_user))
        elif options.command == 'modify':  # Case for the modify command
            # Call the modify function and assign parameters retrieved by the parser,
            # with a case to resolve errors related to the optional user argument (Author Thomas)
            commands.modify(id=options.id, new_details=' '.join(options.details),
                            new_user=' '.join(options.user) if options.user is not None else "unknown",
                            file=options.file)
        elif options.command == 'rm':  # Case for the rm command
            # Call the rm function and assign parameters retrieved by the parser
            commands.rm(id=options.id, file=options.file)
        elif options.command == 'show':   # Case for the show command
            # Call the show function and assign parameters retrieved by the parser
            commands.show(file=options.file)
        elif options.command == 'end':   # Case for the end command
            # Call the endTask function and assign parameters retrieved by the parser (Author Raphaël)
            commands.endTask(file=options.file, id=options.id, end_time=' '.join(options.realisedTime))
    except Exception as e:   # Error handling
        print(f"An error occurred: {e}")   # Display the error


if __name__ == '__main__':
    main()
