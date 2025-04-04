import os
def list_directory_contents(path):
    try:
        print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
        print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        print("All:", os.listdir(path))
    except FileNotFoundError:
        print("Path not found.")
list_directory_contents("C:\Windows\System32")   