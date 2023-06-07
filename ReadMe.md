# Files and Exceptions 

There are for parts to this assignment: reader.py, stats.py, writer.py & pluralize.py.  Each part has a corresponding test script you can run to test your work.  The test scripts are in the same directory as the assignment scripts in this assignment to avoid problems with paths and 'working directories'.  The *working directory* is the directory from which the python script is executed and all relative paths are relative to that directory.  

You'll find a number of test text files you can use in the `files` directory.  Don't modify them as the tests are counting on them being as they are. 

## 1) reader.py

This script should:
1. Ask the user for a file path then pass that file path string to a function named `readFile(readFile())` 
2. The readFile function should then read that text file printing its lines one by one
3. If a path given for the file does not exist then the exception thrown needs to be caught with a **try/except** and an error message should be printed that includes the faulting file path. 

## 2) stats.py
This script should:
1. Ask the user for the path to a script that contains a list on numbers.  The file should have one number of each line. See the `files/numbers.txt` as an example. 
2. It should pass that file path to a function named `analyze`
3. The analyze function should read the numbers in the list and print out on three lines: The line count, total and mean average, in that order.  
4. If a path given for the file does not exist then the exception thrown needs to be caught with a **try/except** and an error message should be printed that includes the faulting file path. 
5. if the file has none number lines (see `files/number2.txt`) then then script should catch the errors with a `try/except`, print a warning including the line text, and then skip the line continuing to calculate the rest of the file.  

## 3) writer.py
This script should: 
1. First ask a user for a file path where the file will be saved
2. Repeatedly as the user to enter lines writing them to the new file, until they enter a blank line to quit.

## 4) puralize.py
This script should:
1. First ask the user for a file to read in containing nouns. See `files/nouns.txt`
2. Second ask the user for a path to save the new file 
3. The script should read each line, take the noun and 'pluralize' by adding an 's' to the end. 
    - Some words end in 'y', you get extra pride points for correctly puralizing these words but it's not required.  The test will pass if you do or if you just add the 's' after the 'y'.  Hint: you can treat a string just like a list of characters.
    
4. The pluralized words should be saved the new file path.
5. Specific fuctions are not required for this script but for full style points you should consider using 1 or 2 additional functions to beak up your script into logical groups of code.  For example it might be nice to have a function solely responsible for pluralizing words.  
    
