import zipfile
import pathlib


def make_arhive(filepaths, destination_dir):
    dest_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)



if __name__ == "__main__":
    make_arhive(filepaths=["bonus.py", "bonus2.py"], destination_dir="files")