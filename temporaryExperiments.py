import os
import re

# Folder path
folder_path = "/home/dhyey/Kalis/Transformers Prime/"

# Get list of all files
files = os.listdir(folder_path)

# Filter out non-files (optional, but good to avoid directories)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Function to extract leading number
def get_leading_number(filename):
    match = re.match(r'^(\d+)', filename.strip())
    if match:
        return int(match.group(1))
    else:
        return float('inf')  # Files without leading number go last

# Sort files by leading number
sorted_files = sorted(files, key=get_leading_number)

# Print result
for f in sorted_files:
    print(f"file '{f}'")
