#!/usr/bin/env python3
import commands
from options import create_parser


def main():
    options = create_parser().parse_args()
    try:
        if options.command == 'add':
            commands.add(details=' '.join(options.details), user=' '.join(options.user), file=options.file)
        elif options.command == 'modify':
            commands.modify(id=options.id, new_details=' '.join(options.new_details),
                            new_user=' '.join(options.new_user) if options.new_user is not None else "unknown",
                            file=options.file)
        elif options.command == 'rm':
            commands.rm(id=options.id, file=options.file)
        elif options.command == 'show':
            commands.show(file=options.file)
        elif options.command == 'end':
            commands.endTask(file=options.file, id=options.id, end_time=' '.join(options.end_time))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
