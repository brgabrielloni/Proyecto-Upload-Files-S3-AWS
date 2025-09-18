# Proyecto S3 Uploader Files

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Descripción

Este proyecto en Python permite subir archivos a AWS S3 utilizando la librería **boto3**. 
Para este caso particular, se definió que solo se subirán archivos CSV, 

- Uso de entornos virtuales
- Manejo seguro de credenciales con archivo `.env`
- Código limpio y modular

---

## ✅ Requisitos

- Python 3.8 o superior  
- Credenciales de AWS configuradas en un archivo `.env`  
- Entorno virtual para instalar las dependencias  

---

## ⚙️ Instalación

### 1. Crear y activar el entorno virtual:

En la terminal, dentro de la carpeta raíz del proyecto, ejecutá:

python -m venv venv

Luego activá el entorno virtual según tu sistema operativo:

🔹 Windows CMD
venv\Scripts\activate.bat

🔹 Windows PowerShell
.\venv\Scripts\activate

🔹 macOS / Linux
source venv/bin/activate

### 2. Instalar dependencias:

Con el entorno virtual activado, ejecutá:

pip install -r requirements.txt

### 3. Configurar archivo .env:

Crea un archivo llamado .env en la raíz del proyecto con tus credenciales de AWS:

AWS_ACCESS_KEY = your_access_key
AWS_SECRET_ACCESS_KEY = your_secret_key
AWS_REGION = your_region
BUCKET_NAME = your_bucket_name

### Importante: nunca subas este archivo a GitHub. Asegurate de incluir .env en tu archivo .gitignore.

---

## 🚀 Uso

Para subir archivos a S3, simplemente ejecutá el script principal:

python main.py

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Si querés aportar, seguí estos pasos:

🔹 Hacé un fork del repositorio.

🔹 Creá una nueva rama para tu feature o bugfix:
    git checkout -b mi-nueva-funcionalidad
    
🔹Hacé commit de tus cambios con mensajes claros:
    git commit -m "Agrega nueva funcionalidad X"
    
🔹Enviá tu rama al repositorio remoto y abrí un Pull Request.

---

## 📬 Contacto

Si tenés preguntas o sugerencias, podés contactarme por:

✉️ E-mail: br.a.gabrielloni@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/braian-a-gabrielloni/

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT — ¡usalo, modificalo y compartilo libremente!

¡Gracias por visitar este proyecto! 

