# Encrypter

## Descripción
Encrypter es una aplicación de línea de comandos para cifrar y descifrar archivos utilizando el módulo `cryptography.fernet`. Esta herramienta genera una clave de cifrado, la guarda en un archivo y utiliza esta clave para cifrar o descifrar archivos especificados por el usuario.

## Requisitos
- Python 3.x
- Módulo `cryptography`

## Instalación
1. Clona este repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd encrypter
    ```

2. Instala las dependencias:
    ```sh
    pip install cryptography
    ```

## Uso
### Cifrar un archivo
Para cifrar un archivo, utiliza el siguiente comando:
```sh
python encrypter.py encrypt <ruta_del_archivo>
```

### Cifrar un archivo
Para desencriptar un archivo, utiliza el siguiente comando:
```sh
python encrypter.py decrypt <ruta_del_archivo>
```
