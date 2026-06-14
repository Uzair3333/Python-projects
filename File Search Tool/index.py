import os

def search_file(path, keyword):
    output_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword in file:
                output_files.append(os.path.join(root, keyword))
    return output_files
