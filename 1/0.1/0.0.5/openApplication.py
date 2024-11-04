import platform
import os
import subprocess


def open_file_location(path):
    while path:
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":
                subprocess.run(["open", path])
            else:
                subprocess.run(["xdg-open", path])
            print(f"Opened: {path}")
            break  # Exit loop if folder opens successfully
        except Exception as e:
            print(f"Failed to open {path}: {str(e)}")
            path = os.path.dirname(path)  # Move up one directory level



def process_command(command):
    if "open d drive" in command:
        parts = command.split("open d drive")
        folder = parts[1].strip() if len(parts) > 1 else ""

        if folder:
            # path = f"D:\\{folder}"
            path = os.path.join("D:\\", *folder.split())
        else:
            path = f"D:\\"

        open_file_location(path)
    
    else:
        print("Command not recognized. Try specifying 'open D drive'.")


process_command("open d drive projects clients clientprojects folder")
