
## 2. Plan de mejoras

### Mejoras propuestas
1. **Interfaz gráfica de usuario (GUI)**: Desarrollar una interfaz gráfica para facilitar el uso de la aplicación a usuarios no técnicos.
2. **Soporte para múltiples archivos**: Permitir el cifrado y descifrado de múltiples archivos a la vez.
3. **Gestión de claves**: Implementar una funcionalidad para gestionar múltiples claves de cifrado y permitir al usuario seleccionar la clave a utilizar.
4. **Integración con servicios en la nube**: Permitir el cifrado y descifrado de archivos almacenados en servicios de almacenamiento en la nube como Google Drive, Dropbox, etc.
5. **Registro de actividades**: Implementar un sistema de registro para llevar un seguimiento de las operaciones de cifrado y descifrado realizadas.
6. **Soporte para diferentes algoritmos de cifrado**: Ampliar la aplicación para soportar diferentes algoritmos de cifrado además de `Fernet`.

### Aplicaciones futuras
- **Cifrado de comunicaciones**: Extender la aplicación para cifrar y descifrar mensajes en tiempo real para aplicaciones de mensajería.
- **Protección de datos sensibles**: Integrar la aplicación en sistemas empresariales para proteger datos sensibles como información financiera y personal.
- **Seguridad en dispositivos móviles**: Desarrollar una versión de la aplicación para dispositivos móviles para proteger archivos y comunicaciones en smartphones y tablets.

## 3. Stack tecnológico

### Lenguaje de programación
- **Python 3.x**: Lenguaje de programación interpretado, de alto nivel y de propósito general.

### Librerías y módulos
- **cryptography**: Librería de Python que proporciona herramientas para cifrado y descifrado de datos. Utiliza el módulo `Fernet` para cifrado simétrico.

### Entorno de desarrollo
- **Visual Studio Code**: Editor de código fuente utilizado para el desarrollo de la aplicación.

### Control de versiones
- **Git**: Sistema de control de versiones distribuido utilizado para gestionar el código fuente del proyecto.
- **GitHub**: Plataforma de alojamiento de código fuente y colaboración en proyectos de software.

### Dependencias
- **cryptography**: Instalado mediante `pip` para proporcionar funcionalidades de cifrado y descifrado.

```sh
pip install cryptography
