import os
def check_path(path):
    if os.path.exists(path):
        print(f"Directory: {os.path.dirname(path)}")
        print(f"File: {os.path.basename(path)}")
    else:
        print("Path does not exist.")
check_path("C:\Windows\System32")      