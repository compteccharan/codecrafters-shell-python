import subprocess
import sys
import shutil
import os

builtins = ["echo", "exit", "type", "pwd", "cd"]

def echo(msg):
    print(msg)

def type_cmd(cmd):
    if cmd in builtins:
        print(f"{cmd} is a shell builtin")
    elif path := shutil.which(cmd):
        print(f"{cmd} is {path}")
    else:
        print(f"{cmd}: not found")

def exec_cmd(cmd):
    parts = cmd.split()
    if shutil.which(parts[0]):
        subprocess.run(parts)
    else:
        print(f"{parts[0]}: command not found")

def pwd():
    print(os.getcwd())

def cd(args):
    target = args[0] if args else "~"
    path = os.path.expanduser(target)
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print(f"cd: {target}: No such file or directory")


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        try:
            command = input()
        except EOFError:
            break

        parts = command.split()
        if not parts:
            continue
        name, args = parts[0], parts[1:]

        if name == "exit":
            break
        elif name == "echo":
            echo(" ".join(args))
        elif name == "type":
            if args:
                type_cmd(args[0])
        elif name == "pwd":
            pwd()
        elif name == "cd":
            cd(args)
        else:
            exec_cmd(command)

if __name__ == "__main__":
    main()