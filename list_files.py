import os

def list_files(directory_path):
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Not found {directory_path}")

    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Not a dir {directory_path}")

    file_list = []

    for root, dir, files  in os.walk(directory_path):
        for file in files:
            if not file.endswith('.md'):
                continue

            full_file = os.path.join(root, file)
            relative_path = os.path.relpath(full_file, directory_path)

            file_list.append(relative_path)

    return file_list

