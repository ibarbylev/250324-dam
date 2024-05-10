import os
from datetime import datetime


def create_new_folder():
    today = datetime.today()
    date_string = today.strftime("%d_%m_%Y")   # dd_mm_yyyy

    # get list of folders with prefix lesson_000__dd_mm_yyyy
    folders: list[str] = [f for f in os.listdir() if os.path.isdir(f) and f.startswith("lesson_")]

    if folders and [f for f in folders if date_string in f]:
        return f"The folder with the date {date_string} already exists!"

    if not folders:
        nnn = "000"
    else:
        # get folder with max nnn
        folders.sort()
        old_nnn = folders[-1].split("_")[1]
        nnn = f"{int(old_nnn) + 1:03d}"

    new_folder_name = f"lesson_{nnn}__{date_string}"

    # create a folder new_folder_name
    os.makedirs(new_folder_name)

    # create a "homework" folder in the new_folder_name folder
    homework_path = os.path.join(new_folder_name, "homework")
    os.makedirs(homework_path)

    # create 2 files in the folder "homework"
    for filename in ["task_01.py", "task_02.py"]:
        with open(os.path.join(homework_path, filename), "w") as f:
            f.write("")

    return f"Created new folder: {new_folder_name}"


print(create_new_folder())

