import os
def write_list_to_file(filename, data):
    with open(filename, 'a', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")
write_list_to_file("C:\\Users\\Elnur\\Desktop\\PP2_Labs\\lab_6\\files\\task4", ["New", "Information"])      