import time


# ENCRYPTION
def encryptionInput():
    # prefer `input.txt` if present, otherwise ask the user
    stringEntry = ""
    try:
        with open("input.txt", "r") as f:
            stringEntry = f.read()
    except FileNotFoundError:
        stringEntry = ""

    if not stringEntry:
        stringEntry = input("Enter text to be encrypted: ")

    return stringEntry


def encryptionRequest(stringEntry):
    # For Encryption: prefix with "e" and send to `input.txt`
    stringEntry = "e" + stringEntry
    with open("input.txt", "w") as f:
        f.write(stringEntry)

    time.sleep(2)


def readEncryptionOutput():
    try:
        with open("output.txt", "r") as f:
            newString = f.read()
        print("Encrypted:", newString)
    except FileNotFoundError:
        print("Encrypted: (no output.txt found yet)")


# DECRYPTION
def decryptionInput():
    stringEntry = ""
    try:
        with open("output.txt", "r") as f:
            stringEntry = f.read()
    except FileNotFoundError:
        stringEntry = ""

    if not stringEntry:
        stringEntry = input("Enter text to be decrypted: ")

    return stringEntry


def decryptionRequest(stringEntry):
    stringEntry = "d" + stringEntry
    with open("input.txt", "w") as f:
        f.write(stringEntry)

    time.sleep(2)


def decryptionOutput():
    try:
        with open("output.txt", "r") as f:
            newString = f.read()
        print("Decrypted:", newString)
    except FileNotFoundError:
        print("Decrypted: (no output.txt found yet)")


# MAIN
def main():
    text = encryptionInput()
    encryptionRequest(text)
    readEncryptionOutput()

    text = decryptionInput()
    decryptionRequest(text)
    decryptionOutput()


if __name__ == "__main__":
    main()
