import sys
import os
from utils import generate_key, load_key, encrypt_file, decrypt_file, encrypt_folder, decrypt_folder

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypter.py <encrypt/decrypt> <file_or_folder_path>")
        sys.exit(1)

    action = sys.argv[1]
    path = sys.argv[2]

    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        sys.exit(1)

    if action == "encrypt":
        generate_key()
        key = load_key()
        if os.path.isfile(path):
            encrypt_file(path, key)
            print(f"File '{path}' encrypted successfully.")
        elif os.path.isdir(path):
            encrypt_folder(path, key)
            print(f"Folder '{path}' encrypted successfully.")
        else:
            print(f"Error: The path '{path}' is neither a file nor a folder.")
    elif action == "decrypt":
        key = load_key()
        if os.path.isfile(path):
            decrypt_file(path, key)
            print(f"File '{path}' decrypted successfully.")
        elif os.path.isdir(path):
            decrypt_folder(path, key)
            print(f"Folder '{path}' decrypted successfully.")
        else:
            print(f"Error: The path '{path}' is neither a file nor a folder.")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)