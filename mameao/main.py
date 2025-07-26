import sys
import os
from mameao.processor import MameAOProcessor
from mameao.operations import process_operation

def parse_arguments(args):
    arguments = {}
    if args and "=" not in args[0]:
        args[0] = f"operation={args[0]}"
    for arg in args:
        if "=" not in arg:
            raise Exception(f"Bad argument, expecting key=value: {arg}")
        k, v = arg.split("=", 1)
        arguments[k.strip().lower()] = v.strip()
    if "directory" not in arguments:
        arguments["directory"] = os.getcwd()
    return arguments

def main():
    args = sys.argv[1:]
    arguments = parse_arguments(args)

    if "operation" in arguments:
        if "version" not in arguments:
            arguments["version"] = "0"
        return process_operation(arguments)
    if "update" in arguments:
        print(f"Would self-update with: {arguments['update']}")
        # TODO: Port SelfUpdate logic
        return 0
    proc = MameAOProcessor(arguments["directory"])
    proc.run()
    return 0

if __name__ == "__main__":
    sys.exit(main())
