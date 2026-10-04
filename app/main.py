import sys
import os
from pathlib import Path


builtins = ["echo", "exit", "type"]


def handle_echo(args):
    print(f"{' '.join(args)}\n")


def handle_type(func):
    if func in builtins:
        print(f"{func} is a shell builtin\n")
        return
    for pathway in os.environ["PATH"].split(os.pathsep):
        pathway = Path(pathway)
        if not pathway.exists() or not pathway.is_dir():
            continue
        for file in Path(pathway).iterdir():
            if file.name == func and file.is_file() and os.access(file, os.X_OK):
                print(f"{func} is {file}\n")
                return

    print(f"{func} not found\n")


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        parsed_command = command.split()
        if parsed_command[0] == "exit":
            break
        if parsed_command[0] == "echo":
            handle_echo(parsed_command[1:])
            continue
        if parsed_command[0] == "type":
            handle_type(parsed_command[1])
            continue
        print(f"{command}: command not found\n")


if __name__ == "__main__":
    main()