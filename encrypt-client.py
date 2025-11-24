import time


# ENCRYPTION
def encryption_input():
    # prefer `input.txt` if present, otherwise ask the user
    stringEntry = ""
    try:
        with open("input.txt", "r") as f:
            stringEntry = f.read()
    except FileNotFoundError:
        stringEntry = ""
    if not stringEntry:
        # ask the user only if the file does not exist
        stringEntry = input("Enter text to be encrypted: ")
    return stringEntry


def encryption_request(stringEntry):
    # For Encryption: prefix with 'e' and send to `input.txt`
    stringEntry = "e" + stringEntry
    with open("input.txt", "w") as f:
        f.write(stringEntry)
    # sleep to wait
    time.sleep(2)


def read_encryption_output():
    # (safe: handle missing `output.txt`)
    try:
        with open("output.txt", "r") as f:
            newString = f.read()
        print("Encrypted:", newString)
    except FileNotFoundError:
        print("Encrypted: (no output.txt found yet)")


# DECRYPTION
def decryption_input():
    # For Decryption: again prefer `input.txt`, otherwise prompt user
    stringEntry = ""
    try:
        with open("output.txt", "r") as f:
            stringEntry = f.read()
    except FileNotFoundError:
        stringEntry = ""
    if not stringEntry:
        stringEntry = input("Enter text to be decrypted: ")
    return stringEntry


def decryption_request(stringEntry):
    stringEntry = "d" + stringEntry
    with open("input.txt", "w") as f:
        f.write(stringEntry)
    # sleep to wait
    time.sleep(2)


def decryption_output():
    try:
        with open("output.txt", "r") as f:
            newString = f.read()
        print("Decrypted:", newString)
    except FileNotFoundError:
        print("Decrypted: (no output.txt found yet)")


# MAIN
def main():
    text = encryption_input()
    encryption_request(text)
    read_encryption_output()
    text = decryption_input()
    decryption_request(text)
    decryption_output()

if __name__ == "__main__":
    main()