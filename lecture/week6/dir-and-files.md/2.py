import os 

def check_access(path):
    if not os.path.exists(path):
        print("The specified path does not exist")
        return
    if not os.access(path,os.R_OK):
        print("Path is not readable")
    else:
        print("path is raedable")
    if not os.access(path,os.W_OK):
        print("path is not writable")
    else:
        print("path is writable")
    if not os.access(path,os.X_OK):
        print("path is not executable")
    else:
        print("path is executable")
path=input()
check_access(path)
