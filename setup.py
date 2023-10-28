import os
import subprocess
from pathlib import Path
import django
import gunicorn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cmd = [
    "python3",
    "-m",
    "PyInstaller",
    "start.py",  # your main file with ui.run()
    "--name",
    "start",  # name of your app
    "--onedir",
    "--clean",
    # "--windowed",  # prevent console appearing, only use with ui.run(native=True, ...)
    "--add-data",
    f"{Path(django.__file__).parent}{os.pathsep}django",
    "--add-data",
    f"{Path(gunicorn.__file__).parent}{os.pathsep}gunicorn",
    "--add-data",
    f"{os.path.join(BASE_DIR, 'db.sqlite3')}:./",
    "--add-data",
    f"{os.path.join(BASE_DIR, 'djangor')}:djangor",
    "--add-data",
    f"{os.path.join(BASE_DIR, 'static')}:static",
]
print(cmd)
subprocess.call(cmd)
