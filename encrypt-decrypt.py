import time
import os


charType = ""
publicKeys = {
    444446005879: 679
}
privateKeys = {
    444446005879: 1309115239
}


# ENCRYPTION
def encryptPrepareChunks(rawText):
    chunkList = []
    encryptedChunks = []

    while rawText:
        new, rawText = helperChunkText(rawText)
        chunkList.append(new)

    return chunkList, encryptedChunks


def encryptProcessChunks(chunkList, encryptedChunks):
    for chunk in chunkList:
        thisChunk = helperEncodeOutput(helperEncodeInts(chunk))
        thisEncryptedChunk = pow(
            thisChunk,
            publicKeys[444446005879],
            444446005879
        )
        encryptedChunks.append(thisEncryptedChunk)

    return encryptedChunks


def encryptWriteOutput(encryptedChunks, outputPath):
    toWrite = ""
    for chunk in encryptedChunks:
        toWrite += str(chunk)
        toWrite += " "

    with open(outputPath, "w") as f:
        f.write(toWrite)

    return toWrite


def encrypt(rawText, outputPath):
    chunkList, encryptedChunks = encryptPrepareChunks(rawText)
    encryptedChunks = encryptProcessChunks(chunkList, encryptedChunks)
    return encryptWriteOutput(encryptedChunks, outputPath)


# DECRYPTION
def decryptSplit(rawText):
    strs = rawText.split()
    nums = []
    for s in strs:
        nums.append(int(s))

    return nums


def decryptProcessSplit(nums):
    text = ""
    for num in nums:
        new = pow(num, privateKeys[444446005879], 444446005879)
        partial = helperDecode(new)
        text += partial
        newText = text.rstrip()

    return newText


def decryptWriteOutput(newText, outputPath):
    with open(outputPath, "w") as f:
        f.write(newText)

    return newText


def decrypt(rawText, outputPath):
    nums = decryptSplit(rawText)
    newText = decryptProcessSplit(nums)
    return decryptWriteOutput(newText, outputPath)


# HELPERS
def helperChunkText(rawText):
    if len(rawText) < 4:
        textChunk = rawText
        toAdd = 4 - len(textChunk)
        for _ in range(1, toAdd):
            textChunk += " "
        rawText = ""
    else:
        textChunk = rawText[:4]
        rawText = rawText[4:]

    return textChunk, rawText


def helperEncodeInts(chars):
    ints = []
    if len(chars) < 4:
        for i in range(0, len(chars) - 1):
            ints.append(ord(chars[i]))

        space = ord(" ")
        while len(ints) != 4:
            ints.append(space)
    else:
        for i in range(0, 4):
            ints.append(ord(chars[i]))

    return ints


def helperEncodeOutput(ints):
    output = 0
    for i in range(0, 4):
        output += ints[i] * (128 ** i)

    return output


def helperDecode(n):
    chars = []
    for _ in range(4):
        new = n % 128
        chars.append(new)
        n //= 128

    my_string = ""
    for num in chars:
        my_string += chr(num)

    return my_string


# MAIN HELPERS
def mainHelperRead(inputPath):
    while True:
        with open(inputPath, "r") as f:
            return f.read()


def mainHelperWrite(inputPath):
    with open(inputPath, "w") as f:
        f.write("")


def mainHelperChar(charType, rawText, outputPath):
    if charType == "e":
        encrypt(rawText, outputPath)
    elif charType == "d":
        decrypt(rawText, outputPath)
    else:
        print("Error: Main program sent unrecognized first character.")


# MAIN
def main():
    baseDir = os.path.dirname(os.path.abspath(__file__))
    inputPath = os.path.join(baseDir, "input.txt")
    outputPath = os.path.join(baseDir, "output.txt")

    while True:
        rawText = mainHelperRead(inputPath)

        if not rawText:
            time.sleep(1)
            continue

        charType = rawText[0]
        rawText = rawText[1:]

        mainHelperWrite(inputPath)
        mainHelperChar(charType, rawText, outputPath)

        time.sleep(1)


if __name__ == "__main__":
    main()
