import io

class Directory:
    def __init__(self, name, isDirectory):
        self.name = name
        self.isDirectory = isDirectory


files = []

def touch(name):
    files.append(io.StringIO(name + "\n" + "file" + "\n"))

def ls():
    for f in files:
        print(f.getvalue().splitlines()[0])

"""
Input: directory name
Format: name, type, other directories
"""
def mkdir(name):
    files.append(io.StringIO(name + "\n" + "dir" + "\n"))

if __name__ == "__main__":

    cmd = ""
    while cmd != "exit":
        cmd = input("Enter command: ")
        cmd = cmd.split(" ")
        if cmd[0] == "touch":
            if len(cmd) < 2:
                print("Please specify a file name!")
            else:
                touch(cmd[1])
        elif cmd[0] == "ls":
            ls()
        elif cmd[0] == "mkdir":
            if len(cmd) < 2:
                print("Please specify a directory name!")
            else:
                mkdir(cmd[1])
        else:
            print("Enter one of the following options:\nls\nmkdir\ncd\ntouch")
    
    print("Exiting...")
