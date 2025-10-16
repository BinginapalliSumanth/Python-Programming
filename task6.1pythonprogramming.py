def writefile(filename):
    with open(filename, "w") as f:
        f.write("Error objects are thrown when runtime errors occur. "
                "The Error object can also be used as a base object for user-defined exceptions ")

def readfile(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)

# Call the functions
writefile("log.txt")
readfile("log.txt")
