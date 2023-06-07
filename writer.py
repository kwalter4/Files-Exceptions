# This program will continue to write user input into a file until prompted to end
def main():
    try:
        filepath = input('Please name your file path: ')
        new_file = open(filepath, 'w')
        not_blank = ''
        while True:
            not_blank = new_file.write(input('Write to File: '))
            # Enter a blank line to quit
            if not not_blank:
                break
        print("File Saved!")

    except:
        print(f'The file {filepath} already exists')


if __name__ == '__main__':
    main()