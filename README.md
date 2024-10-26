# srcli

**srcli** is a simple command-line spaced repetition tool designed for use with Obsidian. This tool helps users review notes in a structured, spaced repetition format to improve knowledge retention.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/pingponghero12/CLI-Spaced-Repetition-For-Obsidian.git
    cd srcli
    ```

2. Install using `pip`:
    ```bash
    pip install .
    ```

## Usage

Once installed, you can use `srcli` by running commands like:
```bash
srcli - Spaced Repetition CLI Tool

Commands:
  create     Create a new tracking file (.sr) for spaced repetition
    --min INT        Minimum days between repetitions
    --max INT        Maximum days between repetitions
    --force         Overwrite existing .sr file

  list       Show files due for review
    --number INT    Show N items (default: 10)
    --all          Show all items

  read       Mark a file as read/reviewed
    FILE            Name of file to mark as read
    --days INT      Set custom interval to next review

  update     Sync .sr file with current directory
            (Add new files, remove deleted ones)

Examples:
  srcli create --min 1 --max 7
  srcli list --number 5
  srcli read document.md
  srcli read document.md --days 14
  srcli update
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.
