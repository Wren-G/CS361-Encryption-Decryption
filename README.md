# CS361-Encryption-Decryption
A microservice using ZeroMQ to communicate with a main program and provide text encryption and decryption services.


# Instructions
Before using this microservice, the user will want to remember the useages of the text files given to you.

With the code, you get two text files:
input.txt
and
output.txt
These names are meant to be straightforward.

input.txt will be written to with the text to be encrypted or decrypted,
then the microservice will write to output.txt.

Two files are to prevent the microservice from getting caught in a loop, instead it can read input, clean the input, and write to the output.

Your main program should write to input.txt, then read from output.txt

# Example Call in Main Program
This example code uses 'entry.txt' as a text file the main program reads into a string variable 'stringEntry'. It can be used with just strings, not reading from files too.
For Encryption:
with open("entry.txt", "r") as f: 
    stringEntry = f.read()
stringEntry = 'e' + stringEntry
with open("input.txt", "w") as f:
    f.write(stringEntry)


For Decryption:
with open("entry.txt", "r") as f: 
    stringEntry = f.read()
stringEntry = 'd' + stringEntry
with open("input.txt", "w") as f:
    f.write(stringEntry)


An if statement to use both Encryption and Decryption based on a bool variable 'encryption':
with open("entry.txt", "r") as f: 
    stringEntry = f.read()
if (encryption):
    stringEntry = 'e' + stringEntry
else:
    stringEntry = 'd' + stringEntry

with open("input.txt", "w") as f:
    f.write(stringEntry)



Now example for taking the output is as simple as:
    with open("output.txt", "r") as f: 
            newstring = f.read()


# Error Messages

 # Error: Main program sent unrecognized first character.
 Main program did not append either the character 'e', or the character 'd', to the front of the text file. 