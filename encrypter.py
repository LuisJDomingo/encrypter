import os
import sys
from cryptography.fernet import Fernet
print("1\n")
def generate_key():
    key = Fernet.generate_key()
    print("key: ", key)
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
        print("\t1.1\n")
print("2\n")
def load_key():
    return open("encryption.key", "rb").read()
print("3\n")
def encrypt_file(file_name, key):
    f = Fernet(key)
    print("f: ", f)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)
print("4\n")
def decrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
print("0\n")
if __name__ == "__main__":
    print("0.1\n")
    if len(sys.argv) != 3:
        print("Usage: python encrypt_storage.py <encrypt/decrypt> <file_path>")
        sys.exit(1)

    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "encrypt":
        generate_key()
        key = load_key()
        encrypt_file(file_path, key)
        print(f"File {file_path} encrypted successfully.")
    elif action == "decrypt":
        key = load_key()
        decrypt_file(file_path, key)
        print(f"File {file_path} decrypted successfully.")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)
