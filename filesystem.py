class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []
    
    #@classmethod
    def touch(self, name):
        self.files.append(File(name))
    
    #@classmethod
    def mkdir(self, name):
        self.dirs.append(Directory(name, self))
    
    #ls@classmethod
    def ls(self):
        if len(self.files) == 0 and len(self.dirs) == 0:
            print("Empty! Use touch/mkdir to add contents.")
        else:
            if len(self.files) != 0:
                for f in self.files:
                    print(f.name)
            if len(self.dirs) != 0:
                for d in self.dirs:
                    print(d.name)


class File:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":

    cdir = Directory("/", None)

    cmd = ""
    while True:
        cmd = input("Enter command: ")
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
                for d in cdir.dirs:
                    print(d.name)
                    if d.name == cmd[1]:
                        cdir = d
                        continue
                    print("Directory not found!")

        else:
            print("Enter one of the following options:\nls\nmkdir\ncd\ntouch\nType 'exit' to quit")
    
    