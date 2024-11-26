# Inspiro Chatbot API

API REST que implementa un chatbot coach especializado en desarrollo personal y bienestar emocional, construido con **Django REST Framework** como tecnología principal e integrado con la **API de OpenAI** para capacidades de inteligencia artificial.

## 🚀 Características

- Chatbot basado en **GPT-3.5-turbo**.
- Coach experto en desarrollo personal y espiritualidad.
- Enfoque holístico: psicología positiva, neurociencia y mindfulness.
- Guía personalizada para el autoconocimiento.
- Documentación interactiva con **Swagger**.

## 🛠️ Tecnologías

- **Django REST Framework**: Principal tecnología para el desarrollo de la API.
- **OpenAI API**: Implementación de inteligencia artificial.
- **SQLite**: Base de datos ligera para almacenamiento local.

## 📂 Estructura del Proyecto

```
chatbot/
├── chat/                # Aplicación principal del chatbot
├── inspiro/             # Configuración general del proyecto
├── venv/                # Entorno virtual de Python
├── .env                 # Variables de entorno (excluido del control de versiones)
├── .env.example         # Plantilla de variables de entorno
├── .gitignore           # Exclusiones de Git
├── db.sqlite3           # Base de datos SQLite
├── manage.py            # Script principal para administración de Django
├── requirements.txt     # Dependencias del proyecto
```

## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/Jaolmos/inspiro-ai-coach.git
cd inspiro-ai-coach
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
El proyecto incluye un archivo `.env.example` como plantilla. Crea una copia llamada `.env` y completa las variables necesarias:

```env
SECRET_KEY=tu-clave-secreta-de-django
OPENAI_API_KEY=tu-api-key-de-openai
```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Iniciar el servidor
```bash
python manage.py runserver
```

Accede a la aplicación en `http://127.0.0.1:8000/`.

## 📖 Documentación API

- **Swagger UI**: `/swagger/`

## 🤖 Capacidades del Chatbot

- Crecimiento personal y autoconocimiento.
- Inteligencia emocional.
- Neurociencia aplicada al bienestar.
- Meditación y mindfulness.
- Equilibrio emocional y mental.
- Conexión con el propósito de vida.

## 📂 Endpoints Principales

### **Chats**

- **GET** `/chats/` - Lista todos los chats.
- **POST** `/chats/` - Crea un nuevo chat.
- **GET** `/chats/{id}/` - Obtiene los detalles de un chat específico.
- **PUT** `/chats/{id}/` - Actualiza completamente un chat.
- **PATCH** `/chats/{id}/` - Actualiza parcialmente un chat.
- **DELETE** `/chats/{id}/` - Elimina un chat.
- **POST** `/chats/{id}/send_message/` - Envía un mensaje al chat especificado.

## 🔧 Uso

1. Crear un usuario y obtener el token de autenticación.
2. Usar el token en las peticiones a la API.
3. Crear un nuevo chat.
4. Enviar mensajes y recibir respuestas del coach.

---

Este proyecto está diseñado para promover el desarrollo personal utilizando la inteligencia artificial de OpenAI integrada con una arquitectura sólida de Django REST Framework.
