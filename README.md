# Proyecto CLI Lear Python - Gestor de Notas Personal

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Database](https://img.shields.io/badge/database-MySQL-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 📌 Propósito del Proyecto
Este sistema es una aplicación de interfaz de línea de comandos (CLI) diseñada para proporcionar un entorno seguro y eficiente de gestión de notas personales. El propósito principal es permitir a los usuarios registrarse, autenticarse y administrar sus pensamientos, tareas o recordatorios de forma privada, utilizando una base de datos robusta para la persistencia de la información.

---

## 🚀 Tecnologías Utilizadas
Desde una perspectiva técnica y de gestión, se han seleccionado herramientas que garantizan escalabilidad y seguridad básica:
*   **Lenguaje:** [Python 3.x](https://www.python.org/) - Por su legibilidad y eficiencia en el desarrollo de scripts CLI.
*   **Base de Datos:** [MySQL](https://www.mysql.com/) - Para una gestión relacional de datos estructurada.
*   **Seguridad:** `hashlib` (SHA-256) - Implementación de cifrado para la protección de credenciales de usuario.
*   **Conectividad:** `mysql-connector-python` - Driver oficial para la comunicación fluida entre la lógica de negocio y la persistencia.

---

## 📋 User Stories (Historias de Usuario)
Para garantizar que el desarrollo cumple con las expectativas del usuario final, el proyecto se basa en las siguientes historias:

1.  **Registro:** *"Como usuario nuevo, quiero crear una cuenta proporcionando mis datos básicos para poder empezar a usar el sistema de forma personalizada."*
2.  **Seguridad:** *"Como usuario consciente de la privacidad, quiero que mi contraseña esté cifrada para que nadie, ni siquiera el administrador de la base de datos, pueda verla en texto plano."*
3.  **Gestión de Notas:** *"Como usuario registrado, quiero poder crear, listar y eliminar mis propias notas para mantener mi información organizada."*
4.  **Persistencia:** *"Como usuario frecuente, quiero que mis notas se guarden de forma permanente para poder acceder a ellas en sesiones futuras."*

---

## 🛠️ Funcionalidades Principales

### Gestión de Usuarios
*   **Registro de Usuarios:** Captura de nombre, apellidos, email y contraseña con validación de persistencia.
*   **Autenticación (Login):** Validación de credenciales mediante comparación de hashes SHA-256.

### Sistema de Notas (CRUD)
*   **Creación:** Registro de nuevas notas vinculadas de forma relacional al ID del usuario activo.
*   **Visualización:** Listado filtrado de notas que pertenecen exclusivamente al usuario identificado.
*   **Eliminación:** Borrado selectivo de notas basado en coincidencias de títulos.

---

## 📂 Estructura del Proyecto
```text
20-proyecto-python/
├── main.py             # Punto de entrada de la aplicación
├── usuarios/           # Módulo de gestión de usuarios y conexión
│   ├── usuario.py      # Modelo de datos de Usuario
│   ├── acciones.py     # Controlador de lógica para usuarios
│   └── conexion.py     # Configuración de acceso a la DB
├── notas/              # Módulo de gestión de notas
│   ├── nota.py         # Modelo de datos de Nota
│   └── notacciones.py  # Controlador de lógica para notas
└── basedatos.sql       # Script de inicialización de la DB
```

---

## 🔧 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Gibson1987R/proyecto-cli-lear-python.git
    ```
2.  **Configurar la Base de Datos:**
    *   Importar el archivo `basedatos.sql` en su servidor MySQL.
3.  **Instalar dependencias:**
    ```bash
    pip install mysql-connector-python
    ```
4.  **Ejecución:**
    ```bash
    python main.py
    ```

---
**Desarrollado como parte del Master en Python.**
*Project Manager Vision: Eficiencia, Seguridad y Simplicidad.*
