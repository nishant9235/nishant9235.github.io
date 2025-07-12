import os
import hashlib

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                with open(filepath, 'rb') as f:
                    filehash = hashlib.md5(f.read()).hexdigest()
                if filehash in hashes:
                    duplicates.append(filepath)
                else:
                    hashes[filehash] = filepath
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
    return duplicates

folder = input("Enter folder path to check duplicates: ")
dupes = find_duplicates(folder)

for d in dupes:
    print(f"Deleting: {d}")
    os.remove(d)
