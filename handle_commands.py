import argparse
import os
import pandas as pd
import list_files
from datetime import datetime
from random import randint

def create_cmd(args, current_dir):
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

    df.index.name = "name"
    df.to_csv(".sr")

    print(df)

def list_cmd(args, current_dir):
    file_path = os.path.join(current_dir, ".sr")
    file_status = os.path.exists(file_path)

    if not file_status: 
        print(f"{file_path} does not exist, use `create` fist")
        return

    today = datetime.today()

    df = pd.read_csv(".sr", index_col="name")
    df["last_date"] = pd.to_datetime(df["last_date"], format="%d-%m-%Y")
    df["dif"] = df["period"] - (today - df["last_date"]).dt.days

    df = df.sort_values("dif")
    df = df.drop(columns="dif", axis=0)

    print(df)

def read_cmd(args, current_dir):
    file_path = os.path.join(current_dir, ".sr")
    file_status = os.path.exists(file_path)

    if not file_status: 
        print(f"{file_path} does not exist, use `create` fist")
        return

    read_path = os.path.join(current_dir, args.file)
    read_status = os.path.exists(read_path)

    if not read_status:
        print(f"{args.file} does not exists at {read_path}")
        return
    
    df = pd.read_csv(".sr", index_col="name")

    df.loc[args.file, "last_date"] = datetime.now().strftime("%d-%m-%Y")
    
    if args.days == None:
        df.loc[args.file, "period"] = 2 * df["period"][args.file]

    df.to_csv(".sr")


def update_cmd(args, current_dir):
    file_path = os.path.join(current_dir, ".sr")
    file_status = os.path.exists(file_path)

    if not file_status: 
        print(f"{file_path} does not exist, use `create` fist")
        return
    
    files = None

    try:
        files = list_files.list_files(current_dir)
    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)

    today = datetime.now().strftime("%d-%m-%Y")
    df = pd.read_csv(".sr", index_col="name")

    for file in files:
        if file not in df.index:
            df.loc[file] = [0, today, 2]

    df.to_csv(".sr")



COMMANDS = {
        "create": create_cmd,
        "list": list_cmd,
        "read": read_cmd,
        "update": update_cmd
        }


