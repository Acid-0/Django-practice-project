# Run Django project (with Django REST Framework + Djongo)

This file gives a **step-by-step** guide (commands + short explanations) to create a Python virtual environment, install Django, Django REST Framework, and Djongo, configure basic settings, run migrations, and start the development server. The examples use the folder name `firstProject` and Django project name `myDjango` (you can replace them with your preferred names).

---

## Prerequisites

* Python 3.x installed and available as `python` (or `python3` on some systems).
* `pip` available.
* If you plan to use **Djongo** (MongoDB as the DB backend): a running MongoDB instance (local or remote).
* Basic familiarity with the command line / terminal.

---

## 1. Open a terminal and choose a working directory

Pick a parent folder where you want to create the project, e.g. `C:\projects` (Windows) or `~/projects` (macOS/Linux).

```sh
# Example (Unix/macOS)
cd ~/projects

# Example (Windows PowerShell or CMD)
cd C:\projects
```

---

## 2. Create a virtual environment

Run:

```sh
python -m venv firstProject
```

This creates a folder named `firstProject` containing the virtual environment.

---

## 3. Activate the virtual environment

**Windows (Command Prompt)**

```cmd
firstProject\Scripts\activate
```

**Windows (PowerShell)**

```powershell
# from the same parent directory
.\firstProject\Scripts\Activate.ps1

# or sometimes
.\firstProject\Scripts\activate
```

**macOS / Linux (bash, zsh)**

```bash
source firstProject/bin/activate
```

After activation, your shell prompt should change (you'll see `(firstProject)` prefix).

---

## 4. Upgrade `pip` (optional, recommended)

```bash
pip install --upgrade pip
```

---

## 5. Install Django, Django REST Framework, and Djongo

Install packages using `pip`.

```bash
pip install django
pip install djangorestframework
pip install djongo
```

You can also combine them:

```bash
pip install django djangorestframework djongo
```

> Note: If you plan to use Djongo, make sure your MongoDB server is reachable and running.

---

## 6. Start a new Django project

Run the `django-admin` command to create a project skeleton. This will create a new folder named `myDjango`.

```bash
django-admin startproject myDjango
```

Now move into the project folder:

```bash
cd myDjango
```

You should now see `manage.py` and a folder named `myDjango` (which contains `settings.py`, `urls.py`, etc.).

---

## 7. Edit `settings.py`

Open `myDjango/settings.py` and make the following minimal changes:

1. **Add allowed hosts** (so the server can accept connections):

```py
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
```

2. **Add Django REST Framework to installed apps**:

```py
INSTALLED_APPS = [
    # default django apps...
    'rest_framework',
    # add any apps you create below
]
```

3. **(If using Djongo) Configure the database** — add or replace the `DATABASES` section with something like:

```py
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_database_name',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://127.0.0.1:27017',
            # if needed: 'username': 'your_user', 'password': 'your_pass'
        }
    }
}
```

Save the file after editing.

---

## 8. Run Django migrations

Apply initial migrations (this will create the default tables/collections required by Django):

```bash
python manage.py migrate
```

If you use Djongo and have some issues with migrations, check that MongoDB is running and reachable and that `djongo` installed correctly.

---

## 9. (Optional) Create a superuser

To manage your site via the admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the interactive prompts to set username/email/password.

---

## 10. Run the development server

Start the server with:

```bash
python manage.py runserver
```

Open a browser and visit:

```
http://127.0.0.1:8000/
```

To run on a different port (e.g., 8001) or bind to all interfaces (useful for testing inside VM or container):

```bash
python manage.py runserver 0.0.0.0:8001
```

---

## 11. Common utility commands

```bash
# Stop the server: Ctrl+C in the terminal
# Deactivate the virtualenv
deactivate

# Save installed packages to requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt on another machine
pip install -r requirements.txt
```

---

## 12. Quick one-shot command list (copy & paste)

```bash
# create venv and activate (Unix/macOS)
python -m venv firstProject
source firstProject/bin/activate
pip install --upgrade pip
pip install django djangorestframework djongo
django-admin startproject myDjango
cd myDjango
# edit settings.py (ALLOWED_HOSTS, add 'rest_framework', add DATABASES for djongo)
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```

**Windows (CMD)**

```cmd
python -m venv firstProject
firstProject\Scripts\activate
pip install --upgrade pip
pip install django djangorestframework djongo
django-admin startproject myDjango
cd myDjango
# edit settings.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 13. Troubleshooting tips

* If `activate` fails on PowerShell due to execution policy, try opening a regular Command Prompt (CMD) or adjust execution policy carefully (PowerShell warning).
* If `djongo` installation or usage fails, ensure:

  * Your Python version is supported by that `djongo` release.
  * MongoDB is running and reachable at the `host` you set in `DATABASES`.
  * You can try installing `pymongo` separately if there are driver errors: `pip install pymongo`.
* If migrations fail, read the error message carefully — often it’s connectivity or compatibility with Djongo/MongoDB.

---

## 14. Next steps (suggested)

* Create an app: `python manage.py startapp api` and add it to `INSTALLED_APPS`.
* Build serializers and viewsets using Django REST Framework.
* Add URLs to `myDjango/urls.py` and test endpoints.

---

If you want, I can also:

* Add a sample `settings.py` snippet with `INSTALLED_APPS` and `DATABASES` pre-filled.
* Create a simple DRF view + serializer example.
* Provide a `.gitignore` for Python/Django projects.

## 14. Rough commands

* python -m venv firstProject(folder name)
* \firstProject\Scripts\activate
* pip install django
* pip install djangorestframework
* django-admin startproject myDjango(proj name)

* Add allowed host in settings py
* add 'rest_framework' in installed_apps

* for DB:
   pip install djongo

*python manage.py runserver