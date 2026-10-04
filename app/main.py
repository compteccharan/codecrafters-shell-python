import sys


def main():
    while True:
        sys.stdout.write("$ ")
        pass
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo"):
            print(command[5:])
        elif command.startswith("type"):
            cmd=command[5:]
            if  cmd in ("type","echo","exit"):
                print(f"{cmd} is a shell builtin")
            else:
                print(f"{cmd}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":

    main()
