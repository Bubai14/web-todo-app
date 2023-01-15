import glob
import csv
import shutil
import zipfile
import pathlib


def get_todos(filepath):
    """
    Read the text file from the filepath and return the todo items
    :param filepath: location of the text file
    :return: todo items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, new_todos):
    """
    Write the todo items to the text file.
    :param filepath: location of the text file
    :param new_todos: new list of todos to be written to the file.
    :return:
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(new_todos)


def compress(filepaths, folder):
    """
    Creates a compressed file from the filepaths and writes it to the folder
    :param filepaths: the files to be compressed
    :param folder: destination folder compressed files to be copied
    :return:
    """
    dest_path = pathlib.Path(folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            archive.write(filepath)


# The below code gets executed only when filehandler is run. For python whenever
# the current file is run, the variable __name__ always holds the value "__main__"
# This code will not be executed when this file is called from other files.
if __name__ == "__main__":
    print(get_todos("files/todos.txt"))


def read_all_files():
    allfiles = glob.glob("files/*.txt")
    for filepath in allfiles:
        with open(filepath, 'r') as file:
            print(file.read())


def get_temperature():
    with open("files/weather.csv", 'r') as file:
        records = list(csv.reader(file))
    city = input("Enter a city: ")
    for record in records[1:]:
        if record[0] == city:
            print(f'Temperature for the city {record[0]} is {record[1]} degree celcius')


def create_zip():
    shutil.make_archive("archive/allfiles", "zip", "files")


create_zip()
