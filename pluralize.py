
def main():
    # Input statements for fie name and file path
    filename = input("Enter the file name containing nouns: ")
    filepath = input("Enter the file path you would like to save it as: ")
    # Calling in readfile function
    readFile(filename, filepath)

def readFile(filename, filepath):
    # Create a new file containing nouns that are plural
    try:
        open_file = open(filename)
        read_file = open_file.readline()
        new_file = open(filepath, 'w')
        # Create a loop that repeats until there are no more nouns
        while read_file != "":
            plurals = pluralize(read_file)
            writer(new_file, plurals)
            read_file = open_file.readline()
        open_file.close()
    # Create an exception if the file is not found
    except FileNotFoundError:
        print(filename, "File Not Found Error")

# Create a function that adds an "s" to every noun
def pluralize(line):
    line = line.strip()
    string = ""
    return line + "s"

# Write a new file with pluralized noun on every other line
def writer(new_file,string):
    try:
        new_file.write(string)
        new_file.write("\n")
    except:
        print(f"The file {filepath} already exists")


if __name__ == '__main__':
    main()