import distutils.dir_util
import os
import shutil
import sys

TEMPLATES_DIRECTORY = 'templates'
LIBGDX_BASE_TEMPLATE = 'hello-world'
BUILD_OUTPUTS_DIRECTORY = 'dist'

def create(args):
    target_folder = input("New project's folder path: ")
    
    if not os.path.exists(target_folder):
        
        # Copy the base 4MB libGDX project. Later, when we have multiple templates,
        # we copy this first, then overwrite/update to use Python for the specific example
        # that the user requested.
        os.makedirs(target_folder)    
        distutils.dir_util.copy_tree("{0}/{1}".format(TEMPLATES_DIRECTORY, LIBGDX_BASE_TEMPLATE), target_folder)
        print("Created new project in {0}".format(target_folder))
    else:
        print("Can't use '{0}', that folder already exists.".format(target_folder))

def build(args):
    if not os.path.exists("build.gradle"):
       print("This doesn't look like a project (where's build.gradle?)")
    else:
        # For now, build desktop only
        os.system("./gradlew desktop:dist")
        # move JAR to "dist"
        if not os.path.exists(BUILD_OUTPUTS_DIRECTORY):
            os.makedirs(BUILD_OUTPUTS_DIRECTORY)
        shutil.copyfile("desktop/build/libs/desktop-1.0.jar", "{0}/{1}".format(BUILD_OUTPUTS_DIRECTORY, "desktop.jar"))

# Main entry point
def run():
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

VALID_COMMANDS = {
    "create": create,
    "build": build
}

run()