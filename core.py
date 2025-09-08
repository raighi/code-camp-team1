import argparse
def create_parser():
    # Create command line parser
    parser = argparse.ArgumentParser(description='Simple task manager')
    # Add a positional argument (the file storing the tasks)
    parser.add_argument('file', help='The tasks file')
    # Add a subparser for subcommands
    subparsers = parser.add_subparsers(help='The commands to manage tasks',
    dest='command', required=True)
    # Create parser for the add command
    parser_add = subparsers.add_parser('add', help='Add a new task. The rest of the command line is used for the task details, the default being "no details".')
    parser_add.add_argument('details', nargs='*', default="no details",
    help="task details")
    # Create parser for the modify command
    parser_modify = subparsers.add_parser('modify',help='Modify a task given its id. The rest of the command line is used for the task details, the default being "no details"')
    parser_modify.add_argument('id', help="the task id")
    parser_modify.add_argument('details', nargs='*', default="no details", help="the new details")
    # Create parser for the rm command
    parser_rm = subparsers.add_parser('rm', help='Remove a task given its id')
    parser_rm.add_argument('id', help="the task id")
    # Create parser for the show command
    parser_show = subparsers.add_parser('show', help='Show the tasks')
    return parser
