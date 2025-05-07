from cryptography.fernet import Fernet
import os
 
 ###################################key generation and loading #######################################

def generate_key():
    key = Fernet.generate_key()    
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    return open("encryption.key", "rb").read()

        
######################################file encrypt/decrypt #######################################

def encrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    # Cambiar la extensión del archivo a .ncrypt
    encrypted_file_name = file_name + ".ncrypt"
    os.rename(file_name, encrypted_file_name)
    with open(encrypted_file_name, "wb") as file:
        file.write(encrypted_data)
        
def decrypt_file(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    # Restaurar el nombre original del archivo eliminando la extensión .ncrypt
    if file_name.endswith(".ncrypt"):
        original_file_name = file_name[:-6]  # Elimina ".ncrypt"
        os.rename(file_name, original_file_name)
        file_name = original_file_name
    with open(file_name, "wb") as file:
        file.write(decrypted_data)

            
#######################################file encrypt/decrypt #######################################
def decrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Decrypting {file_path}...")
            decrypt_file(file_path, key)
            
def encrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Encrypting {file_path}...")
            encrypt_file(file_path, key)