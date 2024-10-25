import argparse
import os
import pandas as pd
import list_files
from datetime import datetime
from random import randint

def create_cmd(args, current_dir):
    print("create")
    file_path = os.path.join(current_dir, ".sr")
    file_status = os.path.exists(file_path)

    if file_status and args.force==False:
        print(f"{file_path} exists already, to overwrite use --force")
        return

    files = None

    try:
        files = list_files.list_files(current_dir)
    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)

    df = pd.DataFrame(columns=["times_read", "last_date", "period"])
    today = datetime.now().strftime("%d-%m-%Y")
    
    for file in files:
        period = randint(int(args.min), int(args.max))
        df.loc[file] = [0, today, period]

    df.to_csv(".sr")

    print(df)

def list_cmd(args, current_dir):
    print("list")

    if not file_status: 
        print(f"{file_path} does not exist, use `create` fist")
        return

    print(args)

def read_cmd(args, current_dir):
    print("read")

    if not file_status: 
        print(f"{file_path} does not exist, use `create` fist")
        return

    print(args)

COMMANDS = {
        "create": create_cmd,
        "list": list_cmd,
        "read": read_cmd
        }


