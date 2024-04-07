#!/usr/bin/env python3
import getopt
import sys

class Knife:
    def __init__(self, main_cmd):
        self.main_cmd = main_cmd

    def node_show(self, node_name):
        print(f"Executing: {self.main_cmd} node show {node_name}")

    def role_show(self, role_name):
        print(f"Executing: {self.main_cmd} role show {role_name}")

class CommandDispatcher:
    def __init__(self, main_cmd):
        self.knife = Knife(main_cmd)

    def dispatch(self, args):
        if args[0] == "ns":
            self.knife.node_show(*args[1:])
        elif args[0] == "rs":
            self.knife.role_show(*args[1:])
        else:
            print("Invalid option")

def main():
    # Define default values
    my_dir = "/tmp/test"
    main_cmd = "ls"

    try:
        # Parse options
        opts, args = getopt.getopt(sys.argv[1:], "hd:m:", ["help", "directory=", "main-cmd="])

        # Process options
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print_help()
                sys.exit()
            elif opt == "-d" or opt == "--directory":
                my_dir = arg
            elif opt == "-m" or opt == "--main-cmd":
                main_cmd = arg

        # Initialize command dispatcher
        dispatcher = CommandDispatcher(main_cmd)

        # Dispatch command
        dispatcher.dispatch(args)

    except getopt.GetoptError as err:
        print(err)
        print_help()
        sys.exit(1)

def print_help():
    print("Usage: script.py [OPTIONS] [PROGRAM OPTIONS]")
    print("Options:")
    print("  -h, --help             Show help message and exit")
    print("  -d, --directory DIR    Specify directory (default: /tmp/test)")
    print("  -m, --main-cmd CMD     Specify main command (default: ls)")
    print("Program Options:")
    print("  ns NODE_NAME           Execute 'knife node show' for NODE_NAME")
    print("  rs ROLE_NAME           Execute 'knife role show' for ROLE_NAME")

if __name__ == "__main__":
    main()
