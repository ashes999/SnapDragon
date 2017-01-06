import sys

def create(args):
    target_folder = input("Please enter the project's path: ")
    print("Copying to {0}".format(target_folder))

VALID_COMMANDS = { 'create': create }

if len(sys.argv) > 1:
    command = sys.argv[1]
    arguments = sys.argv[2:]

    if command in VALID_COMMANDS:
        func = VALID_COMMANDS[command]
        func(arguments)
    else:
        print("'{0}' isn't a valid command. Try one of: {1}".format(command, list(VALID_COMMANDS.keys())))
else:
    print("Usage: snap <command>. Valid commands: {0}".format(list(VALID_COMMANDS.keys())))

