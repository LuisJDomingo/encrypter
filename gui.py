import tkinter as tk
from tkinter import filedialog, messagebox
from utils import generate_key, load_key, encrypt_file, decrypt_file, encrypt_folder, decrypt_folder
import os

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, folder_path)

def process_action():
    path = entry_path.get()
    action = action_var.get()
    target_type = target_var.get()

    if not path:
        messagebox.showerror("Error", "Por favor, selecciona un archivo o carpeta.")
        return

    if not os.path.exists(path):
        messagebox.showerror("Error", "La ruta seleccionada no existe.")
        return

    try:
        if action == "encrypt":
            generate_key()
            key = load_key()
            if target_type == "file":
                encrypt_file(path, key)
                messagebox.showinfo("Éxito", f"Archivo {path} encriptado correctamente.")
            elif target_type == "folder":
                encrypt_folder(path, key)
                messagebox.showinfo("Éxito", f"Carpeta {path} encriptada correctamente.")
        elif action == "decrypt":
            key = load_key()
            if target_type == "file":
                decrypt_file(path, key)
                messagebox.showinfo("Éxito", f"Archivo {path} desencriptado correctamente.")
            elif target_type == "folder":
                decrypt_folder(path, key)
                messagebox.showinfo("Éxito", f"Carpeta {path} desencriptada correctamente.")
        else:
            messagebox.showerror("Error", "Acción no válida.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Encrypter")

# Ruta del archivo o carpeta
frame_path = tk.Frame(root)
frame_path.pack(pady=10)

label_path = tk.Label(frame_path, text="Ruta:")
label_path.pack(side=tk.LEFT, padx=5)

entry_path = tk.Entry(frame_path, width=50)
entry_path.pack(side=tk.LEFT, padx=5)

btn_file = tk.Button(frame_path, text="Seleccionar archivo", command=select_file)
btn_file.pack(side=tk.LEFT, padx=5)

btn_folder = tk.Button(frame_path, text="Seleccionar carpeta", command=select_folder)
btn_folder.pack(side=tk.LEFT, padx=5)

# Tipo de objetivo (archivo o carpeta)
frame_target = tk.Frame(root)
frame_target.pack(pady=10)

target_var = tk.StringVar(value="file")
radio_file = tk.Radiobutton(frame_target, text="Archivo", variable=target_var, value="file")
radio_file.pack(side=tk.LEFT, padx=5)

radio_folder = tk.Radiobutton(frame_target, text="Carpeta", variable=target_var, value="folder")
radio_folder.pack(side=tk.LEFT, padx=5)

# Acción (encriptar o desencriptar)
frame_action = tk.Frame(root)
frame_action.pack(pady=10)

action_var = tk.StringVar(value="encrypt")
radio_encrypt = tk.Radiobutton(frame_action, text="Encriptar", variable=action_var, value="encrypt")
radio_encrypt.pack(side=tk.LEFT, padx=5)

radio_decrypt = tk.Radiobutton(frame_action, text="Desencriptar", variable=action_var, value="decrypt")
radio_decrypt.pack(side=tk.LEFT, padx=5)

# Botón para ejecutar la acción
btn_process = tk.Button(root, text="Procesar", command=process_action)
btn_process.pack(pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()