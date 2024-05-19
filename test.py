import os

def find_null_bytes_in_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    if b'\x00' in content:
                        print(f"Null byte found in: {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

find_null_bytes_in_files('.')