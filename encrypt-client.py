# Milestone 2 test file
# Group 42 - The Dream Team
import time

# Microservice 3: Encryption

# Prepare input: prefer `input.txt` if present, otherwise ask the user
stringEntry = ""
try:
    with open("input.txt", "r") as f:
        stringEntry = f.read()
except FileNotFoundError:
    # ask the user only if the file does not exist
    stringEntry = input("Enter text to be encrypted: ")

# For Encryption: prefix with 'e' and send to `input.txt`
stringEntry = 'e' + stringEntry
with open("input.txt", "w") as f:
    f.write(stringEntry)

#sleep to wait
time.sleep(2)

# Reading output (safe: handle missing `output.txt`)
try:
    with open("output.txt", "r") as f:
        newString = f.read()
    print("Encrypted:", newString)
except FileNotFoundError:
    print("Encrypted: (no output.txt found yet)")

# For Decryption: again prefer `input.txt`, otherwise prompt user
stringEntry = ""
try:
    with open("input.txt", "r") as f:
        stringEntry = f.read()
except FileNotFoundError:
    stringEntry = input("Enter text to be decrypted: ")

stringEntry = 'd' + newString
with open("input.txt", "w") as f:
    f.write(stringEntry)

#sleep to wait
time.sleep(2)

# Reading output (safe)
try:
    with open("output.txt", "r") as f:
        newString = f.read()
    print("Decrypted:", newString)
except FileNotFoundError:
    print("Decrypted: (no output.txt found yet)")