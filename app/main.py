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
    if path := shutil.which(cmd.split()[0]):
        subprocess.call(cmd, shell=True)
    else:
        print(f"{cmd}: not found")

def pwd():
    print(os.getcwd())

def cd(path):
    if os.path.isdir(path[0]):
        if path[0].startswith("/"):
            os.chdir(path[0])
        # elif path[0] == "./":


    else:
        print(f"cd: {path[0]}: No such file or directory")


def main():
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
            echo(command[5:])
        elif command.startswith("type "):
            cmd = command[5:]
            type_cmd(cmd)
        elif command.split()[0] not in builtins:
            exec_cmd(command)
        elif command.startswith("pwd"):
            pwd()
        elif command.startswith("cd"):
            path = command.split()[1:]
            cd(path)

        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()