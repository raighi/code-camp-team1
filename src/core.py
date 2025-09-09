import commands_alois as commands
from options import create_parser
# Create command line parser
options = create_parser().parse_args()
try:
    # Read tasks file, if it exists
    with open(options.file, 'r') as f:
        tasks = f.readlines()
    # Run the command
    if options.command == 'add':
        commands.add(details=' '.join(options.details), file=options.file)
    elif options.command == 'modify':
        commands.modify(id=options.id, new_details=' '.join(options.details), file=options.file)
    elif options.command == 'rm':
        commands.rm(id=options.id, file=options.file)
    elif options.command == 'show':
        commands.show(tasks)
except FileNotFoundError:
    print(f"The file {options.file} was not found")
