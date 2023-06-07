# The purpose of this program is to find a file for the user
# First we create a function that opens and reads the file inputted by the user

def readFile(filename):
    try:
        open_file = open(filename)
        open_file2 = open_file.readline()

        # Read the text on the line one by one
        while open_file2 != "":
            print(open_file2)
            open_file2 = open_file.readline()
        open_file.close()
    # If the path file does not exist, we throw an exception
    except FileNotFoundError as error:
        print(filename, "Error reading the file")

# Ask the user for a file
# Call the readFile function in the main to output the result to the user.
def main():
    filename = input("Please input the file name: ")
    readFile(filename)


if __name__ == '__main__':
    main()
