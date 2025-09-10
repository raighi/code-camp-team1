#!/usr/bin/env python3
import commands
# import core
from options import create_parser


def main():
    options = create_parser().parse_args()
    try:
        # tasks = core.read_tasks(options.file)
        if options.command == 'add':
            commands.add(details=' '.join(options.details), user=' '.join(options.user), file=options.file)
        elif options.command == 'modify':
            commands.modify(id=options.id, new_details=' '.join(options.details), new_user=' '.join(options.user), file=options.file)
        elif options.command == 'rm':
            commands.rm(id=options.id, file=options.file)
        elif options.command == 'show':
            commands.show(file=options.file)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
