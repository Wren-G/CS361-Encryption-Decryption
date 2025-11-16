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

# Example Call in Main Program (Python)
At the top of your program with your libraries make sure you have:
import time

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

Reccomended:
One of two methods, either a long sleep to wait for the logic:
import time

time.sleep(5)
with open("output.txt", "r") as f: 
    newstring = f.read()

OR, a loop with one second intervals to wait for the contents to come back
import time

while (true):
with open("output.txt", "r") as f: 
    newstring = f.read()
if (newstring):
    break
else:
    time.sleep(1)

# Error Messages

 # Error: Main program sent unrecognized first character.
 Main program did not append either the character 'e', or the character 'd', to the front of the text file. 


# UML Sequence Diagram
<img width="1235" height="719" alt="Encrypt-Decrypt_1" src="https://github.com/user-attachments/assets/e8ed24f0-5f7e-488d-8ed9-605f38c54605" />
