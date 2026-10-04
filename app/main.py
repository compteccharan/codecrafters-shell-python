import subprocess
import sys
import shutil
import os

def main():
    builtins = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command = input()
        except EOFError:
            break
        if command == "exit":
            break
        if command.startswith("echo "):
            print(f"{command[5:]}")
        elif command.startswith("type "):
            cmd = command[5:]
            if cmd in builtins:
                print(f"{cmd} is a shell builtin")
            elif path := shutil.which(cmd):
                print(f"{cmd} is {path}")
            else:
                print(f"{cmd}: not found")
        elif command.split()[0] not in builtins:
            if path := shutil.which(command.split()[0]):
                subprocess.call(command, shell=True)
            else:
                print(f"{command}: not found")
        elif command.startswith("pwd"):
            print(os.getcwd())
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()