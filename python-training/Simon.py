#--Value Returning Function
# This program displays a random number
# in the range of 1 through 10.
import random # import the random module

def main():
    # Get a random number.
    number = random.randint(1, 10)
    # Display the number.
    print('The number is', number)
# Call the main function.
main()

#----(dice.py)-----This program simulates the rolling of dice.
import random #-- import the random number module
# Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    again = 'y' # Create a variable to control the loop.
    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        again = input('Roll them again? (y = yes): ')  # Do another roll of the dice?
main() # Call the main function.
#========================== Module 7 files and exceptions ===============================================
#---When a program needs to save data for later use, it writes the data in a file.
# The data can be read from the file at a later time.

# This program writes three lines of data to a file.
def main():
    outfile = open('I:\programmers.txt', 'w') # Open a file named programmers.txt.
    # Write the names of three philosphers to the file.
    outfile.write('1. Paul Allen\n')
    outfile.write('2. Markachi\n')
    outfile.write('3. Luna Simon\n')
    outfile.close() # Close the file.
main() # Call the main function.

#This program reads and displays the contents of the programmers.txt file.
def main():
    infile = open('I:\programmers.txt', 'r') # Open a file named programmers.txt.
    file_contents = infile.read()  # Read the file's contents.
    line1 = infile.readline()  # read first line
    line2 = infile.readline()  # read 2nd line
    infile.close()  # close file.
    print(file_contents)  # Print the data that was read into memory.
    print("printing first line: ", line1)
    print("printing 2nd line: ", line2)
main()  # call main function

def main():
    infile = open('I:\emails.txt', 'r') # Open a file named emails.txt.
    file_contents = infile.read() # Read the file's contents.
    line1 = infile.readline() # read first line
    line2 = infile.readline()  # read another line
    infile.close() # close file.
    print(file_contents) # Print the data that was read into memory.
    print("printing first line: ", line1)
    print("printing 2nd line: ", line2)
    print(infile.readline())
main() # call main function

f = open("I:\emails.txt", "r")
print("printing first line: ", f.readline())
print("printing 2nd line: ", f.readline())

#------------ writeNames.py------------------------------
# This program gets three names from the user and writes them to a file.
def main():
    # Get three names.
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')
    # Open a file named goodFriends.txt.
    myfile = open('I:\goodFriends.txt', 'w') # use 'w' to overwrite file content and 'a' to append
    # Write the names to the file.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')
    # Close the file.
    myfile.close()
    print('The names were written to goodFriends.txt.')
main()

"""
NEXT: 7.3 PROCESSING RECORDS AND HANDLING EXCEPTIONS
"""
