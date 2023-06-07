def analyze(filepath):
# Define what value is being saved
    total = 0
    counter = 0

    try:
        # opening user defined filepath
        with open(filepath, "r") as num:
            # adding each line to the last, while keeping a counter
            for line in num:
                try:
                    value = int(line)
                    total += value
                    counter += 1
                except:
                    print(line.strip(), "is not a number")

            # Calculating mean from total and counter
            mean = total/counter

            # print the processed data
            print("count: ", counter)
            print("total: ", total)
            print("mean average: {mean:.2f}".format(mean=mean))

    # accounting for file not found error
    except FileNotFoundError:
        print(filepath, "not found.")

# Call the function in main
def main():
    filepath = input("Enter file path here: ")
    analyze(filepath)
#

if __name__ == '__main__':
    main()