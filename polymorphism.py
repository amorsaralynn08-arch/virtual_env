class File:
    def open(self):
        print("opening file")
class PDF(File):
    def open(self):
        print("opening PDF file")
class ZipFile(File):
    def open(self):
        print("Opening ZipFile")

files = [File() , PDF() , ZipFile()]
for f in files:
    f.open()