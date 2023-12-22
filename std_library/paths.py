from pathlib import Path


# Path("C:\\Program Files\\")
# Path("/user/local/bin")

# path = Path("ecommerce/__init__.py")


# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# print(path.absolute())


# path2 = Path("ecommerce")
# # path.exists()
# # path.mkdir()
# # path.rename("sth_else")
# # path.rmdir()

# #returns a generator object, a list of all files in a directory
# path = path.iterdir()
# for p in path:
#     print(p)


# #another type of search
# py_files = [p for p in path.glob("*.py")]
# recursive_py_files = [p for p in path.rglob("*.py")]


path = Path("files/text.txt")
print(path.exists())
path.rename("sth.txt")
#to delete a file 
path.unlink()

path.stat()


#takes care of openning and closing a file
path.read_text()

path.write_text()


import shutil 
shutil(oneFile, toAnotherFile)




from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    # for path in Path("ecommerce").rglob("*.*"):
    #     zip.write(path)
    zip.namelist()
    info = zip.getinfo("adress of a file")
    zip.extractall("directory we extract into")




