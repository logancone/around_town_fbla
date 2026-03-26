import subprocess
from pathlib import Path


def convert_ui_to_py():
    ui_folder = Path('qt/')

    for item in ui_folder.iterdir():
        subprocess.run(f"pyside6-uic {str(item)} -o ui/{str(item)[3:-3]}.py")

if __name__ == "__main__":
    convert_ui_to_py()