import pandas as pd
import os
import argparse
import list_files
import handle_commands

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument('--min', type=int, required=True)
    create_parser.add_argument('--max', type=int, required=True)
    create_parser.add_argument("--force", action="store_true")

    list_parser = subparsers.add_parser("list")
    group = list_parser.add_mutually_exclusive_group()
    group.add_argument("--number", type=int, default=10)
    group.add_argument("--all", action="store_true")

    read_parser = subparsers.add_parser("read")
    read_parser.add_argument("file", help="file to read")
    read_parser.add_argument("--days", help="custom number of days to next repetition", type=int, required=False)

    update_parser = subparsers.add_parser("update")

    return parser.parse_args()

def main():
    current_dir = os.getcwd()

    args = parse_args()
    handle_commands.COMMANDS[args.command](args, current_dir)


if __name__ == "__main__":
    main()
