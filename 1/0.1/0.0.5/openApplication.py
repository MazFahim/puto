import platform
import os
import subprocess
import shutil


last_opened_folder = None

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
            last_opened_folder = path
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

    elif "open c drive" in command:
        parts = command.split("open c drive")
        folder = parts[1].strip() if len(parts) > 1 else ""

        if folder:
            # path = f"D:\\{folder}"
            path = os.path.join("C:\\", *folder.split())
        else:
            path = f"C:\\"

        open_file_location(path)
    
    elif "open e drive" in command:
        parts = command.split("open e drive")
        folder = parts[1].strip() if len(parts) > 1 else ""

        if folder:
            # path = f"D:\\{folder}"
            path = os.path.join("E:\\", *folder.split())
        else:
            path = f"E:\\"

        open_file_location(path)
    
    elif "open f drive" in command:
        parts = command.split("open f drive")
        folder = parts[1].strip() if len(parts) > 1 else ""

        if folder:
            # path = f"D:\\{folder}"
            path = os.path.join("F:\\", *folder.split())
        else:
            path = f"F:\\"

        open_file_location(path)
    
    else:
        print("Command not recognized. Try specifying 'open D drive'.")


def open_application(app_name):
    global last_opened_folder

    if last_opened_folder:
        app_path = os.path.join(last_opened_folder, app_name + ".exe")
        if os.path.exists(app_path):
            subprocess.run(app_path, shell=True)
            print(f"Opened {app_name} from {last_opened_folder}")
            return
    
    path = shutil.which(app_name)
    if path:
        subprocess.run(path, shell=True)
        print(f"Opened {app_name} from PATH.")
        return

# process_command("open d drive projects clients clientprojects folder")
