import os

class DirReader(object):
    """Read a directory and subdirectories.
    call read() to read in all files.
    """
    def __init__(self, startdir=None):
        self.files = []
        self.startdir = startdir

    def read(self, startdir):
        """read() will return an array containing the files it found
        in startdir and it's subdirectories.
        """
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
