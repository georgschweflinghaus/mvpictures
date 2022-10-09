import os

class DirReader(object):

    def __init__(self, startdir=None):
        self.files = []
        self.startdir = startdir

    def read(self, startdir):
        self.startdir = startdir
        directory = os.listdir(self.startdir)
        for entry in directory:
            entry = os.path.join(startdir,entry)
            if os.path.isdir(entry):
                self.read(entry)
            else:
                self.files.append(entry)
        return self.files


if __name__ == "__main__":
    print(DirReader().read("./data"))
