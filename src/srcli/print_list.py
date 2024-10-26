from datetime import datetime
import pandas as pd
from tabulate import tabulate

# Color functions
def color_days_to_repetition(days):
    if days <= -5:
        return f"\033[31;1m{days}\033[0m"  # Dark red
    elif -4 <= days <= -1:
        return f"\033[31m{days}\033[0m"    # Normal red
    elif days == 0:
        return f"\033[33m{days}\033[0m"    # Yellow
    elif 1 <= days <= 10:
        return f"\033[32m{days}\033[0m"    # Light green
    else:
        return f"\033[32;2m{days}\033[0m"  # Dark green

def display_dataframe(df, n):
    # Rename columns for display
    df = df.rename(columns={
        "name": "File",
        "times_read": "Times Read",
        "last_date": "Last Date",
        "period": "Period",
        "dif": "Days to Repetition"
    })

    df.index.name = "File"

    # Apply coloring to the "Days to Repetition" column
    df["Days to Repetition"] = df["Days to Repetition"].apply(color_days_to_repetition)

    # Display only the top `n` rows
    print(tabulate(df.head(n), headers="keys", tablefmt="plain", showindex=True))
