import os
import shutil


def organize_files(folder):
    if not os.path.exists(folder):
        print("Folder not found!")
        return

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        extension = os.path.splitext(file)[1]

        if extension == "":
            continue

        extension = extension[1:].lower()

        # Create folder according to extension
        new_folder = os.path.join(folder, extension)

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        # Create destination path
        destination = os.path.join(new_folder, file)

        # If file already exists, create a new name
        if os.path.exists(destination):
            name, ext = os.path.splitext(file)
            count = 1

            while os.path.exists(destination):
                new_name = name + "_" + str(count) + ext
                destination = os.path.join(new_folder, new_name)
                count += 1

        shutil.move(file_path, destination)

        print(file, "->", extension)


def main():
    folder = input("Enter folder path: ")

    organize_files(folder)

    print("Files organized successfully!")


if __name__ == "__main__":
    main()

#OUTCOME
#MyFiles
#│
#├── photo.jpg
#├── photo2.png
#├── notes.txt
#├── resume.pdf
#├── program.py
#└── data.xlsx

#Enter folder path: C:\Users\Mantasha\Desktop\Test

#photo.jpg -> jpg
#notes.txt -> txt
#resume.pdf -> pdf
#data.xlsx -> xlsx

#Files organized successfully!
