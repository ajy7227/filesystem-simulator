"""
Directory class
Name: name of directory
Parent: parent directory object
"""

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []
        self.path = [name]
    
    # Creates a new file and adds it to files list
    def touch(self, name):
        self.files.append(File(name))
    
    # Creates a new directory and adds it to directory list
    def mkdir(self, name):
        new_dir = Directory(name, self)
        new_dir.path = self.path + new_dir.path
        self.dirs.append(new_dir)
    
    # Lists all contents of directory
    def ls(self):
        if len(self.files) == 0 and len(self.dirs) == 0:
            print("Empty! Use touch/mkdir to add contents.")
        else:
            fnames = []
            dnames = []
            if len(self.files) != 0:
                for f in self.files:
                    fnames.append(f.name)
                print("Files:", *fnames)
            if len(self.dirs) != 0:
                for d in self.dirs:
                    dnames.append(d.name)
                print("Directories:", *dnames)

"""
File Class
Name: name of file
There are currently no contents in these files
"""
class File:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":

    # Set current root directory
    cdir = Directory("root", None)

    # Continuously prompt for user input until receive "exit"
    cmd = ""
    while True:
        cmd = input('/'.join(str(x) for x in cdir.path) + " > ")
        if cmd.lower() == "exit":
            print("Exiting...")
            break
        cmd = cmd.split(" ")
        if cmd[0] == "touch":
            if len(cmd) < 2:
                print("Please specify a file name!")
            else:
                cdir.touch(cmd[1])
        elif cmd[0] == "ls":
            cdir.ls()
        elif cmd[0] == "mkdir":
            if len(cmd) < 2:
                print("Please specify a directory name!")
            else:
                cdir.mkdir(cmd[1])
        elif cmd[0] == "cd":
            if len(cmd) < 2:
                print("Please specify a valid directory name!")
            else:
                if cmd[1] == "..":
                    cdir = cdir.parent
                else:
                    for d in cdir.dirs:
                        print("Changing to", d.name, "...")
                        if d.name == cmd[1]:
                            cdir = d
                            continue
                        print("Invalid directory!")
        else:
            print("Enter one of the following options:\nls\nmkdir\ncd\ntouch\nType 'exit' to quit")
    
    