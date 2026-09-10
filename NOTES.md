# Web Application Technologies and Django (DJ4E)

## 📌 Module 1: Web Technologies Overview
**Core Objective:** Understand the HTTP Request-Response cycle and fundamental web protocols.
*   **Key Concepts:**
    *   Clients (Browsers) request resources from Servers.
    *   TCP/IP, Sockets, and Port 80 (HTTP) / 443 (HTTPS).
    *   HTML, CSS, and structural web design.

---

## 📌 Module 2: Environment & Command Line (PythonAnywhere)
**Core Objective:** Establish a cloud-based Linux environment, install Django, and bootstrap the core project architecture.

### 1. The Linux Shell (Bash)
*   **Directory Navigation:**
    *   `pwd` (Print Working Directory): Verifies current location.
    *   `ls -l`: Lists files with permissions and modification details.
    *   `cd <directory>`: Changes location. (`cd ~` returns to root).
*   **File Management:**
    *   `mkdir <name>`: Creates a new directory.
    *   `nano <file>`: Terminal-based text editor for modifying files.

### 2. Python Virtual Environment
*   **Purpose:** Isolates project dependencies (like Django 5.2) to prevent version conflicts across different applications on the same server.
*   **Setup (PythonAnywhere specific):**
    *   `mkvirtualenv django_env` (creates environment)
    *   `workon django_env` (activates environment)

### 3. Project Initialization
*   **Command:** `django-admin startproject mysite`
*   **Generated Architecture:**
    *   `manage.py`: The primary command-line utility used to execute server commands and database migrations.
    *   `mysite/settings.py`: The central registry for the project (database connections, registered apps, timezone).
    *   `mysite/urls.py`: The root URL dispatcher that routes incoming HTTP requests to application logic.

### 4. Application Architecture (The `polls` App)
*   **Concept:** A Django *project* configures the entire website; an *app* is a modular, reusable web application that executes a specific feature (e.g., a polling system).
*   **Command:** `python manage.py startapp polls`
*   **Core App Files:**
    *   `models.py`: Defines database schemas using Python classes (The "Model" in MVT).
    *   `views.py`: Handles business logic, processing HTTP requests and returning HTTP responses (The "View" in MVT).
    *   `urls.py` (Must be created manually): Routes app-specific URLs to their corresponding views.

### 🛠️ Troubleshooting Module 2
*   **"No changes detected":** This means you ran `makemigrations`, but Django did not find any model code in `models.py`, or the app is not registered in `settings.py` under `INSTALLED_APPS`.
*   **"Command not found":** Ensure your virtual environment is activated (`workon django_env`) before running `python manage.py ...` commands.

---
