#This is the microservice to encrypt and decrypt text files :)

#libraries
import time
import os

#Global variables
charType = ''

# public encryption keys (n, e)
publicKeys = {
    444446005879: 679
}

# private encryption keys (n, d)
privateKeys = {
    444446005879: 1309115239
}

# Encrypts text based on (n, e)
def encrypt(rawTxt, outputPath):
    # establish lists 
    chunkList = []
    # encrypted_chunks = []
    toWrite = ''

    # divide text into a list of smaller chunks
    while rawTxt:
        new, rawTxt = chunkText(rawTxt)
        chunkList.append(new)

    # encode chunks, then encrypt them (RSA based)
    for chunk in chunkList:
        thisChunk = encode(chunk)

        # x^e mod n
        thisEncryptedChunk = pow(thisChunk, publicKeys[444446005879], 444446005879)

        toWrite += (str(thisEncryptedChunk))
        toWrite += ' '
        
        # encrypted_chunks.append(this_encrypted_chunk)
    
    with open(outputPath, 'w') as f:
        f.write(toWrite)
    return toWrite

# Decrypts text based on (n, d)
def decrypt(rawTxt, outputPath):
    # divide the string from file into numbers
    strs = rawTxt.split()
    nums = []
    for str in strs:
        try:
            num = int(str)
            nums.append(num)
        except ValueError:
            print('error in decryption')

    text = ''
    for num in nums:
        # decrypt based on d mod n
        new = pow(num, privateKeys[444446005879], 444446005879)
        partial = decode(new) # returns a partial string
        text += partial
    
    # eliminate whitespace if necessary
    new_text = text.rstrip()

    # return text and append to file.
    with open(outputPath, 'w') as f:
        f.write(new_text)
    return new_text

# Helper function for encryption: split string into correct block sizes
def chunkText(rawTxt):
    # base case for recursion (rawTxt almost empty)
    if len(rawTxt) < 4:
        textChunk = rawTxt
        toAdd = 4 - len(textChunk)

        # if we don't have a 4-block, make it a 4-block
        for i in range(1, toAdd):
            textChunk += ' '    
        
        rawTxt = "" # erase rawTxt

    # take first 4 chars
    else:
        textChunk = rawTxt[:4]
        # remove those chars from rawTxt
        rawTxt = rawTxt[4:]

    # return both cases (we call this function recursively)
    return textChunk, rawTxt

# This function encodes 4 character blocks into a number.
def encode(chars):
    ints = []
    if len(chars) < 4:
        # if we don't have a 4-block, make it a 4-block with spaces
        for i in range(0, len(chars) - 1):
            new = ord(chars[i])
            ints.append(new)
        
        space = ord(' ')
        while len(ints) != 4:
            ints.append(space)
    
    else:
    # use ord() to convert to ascii
        for i in range(0, 4):
            new = ord(chars[i]) # ord is an integer
            ints.append(new)
        
    output = 0
    # reverses division algorithm
    for i in range(0, 4):
        new = ints[i] * (128 ** i)
        output += new
    
    # return ascii ints
    return output

# This function reverses the encoding process into characters
def decode(num):
    # division algorithm
    chars = []
    for i in range(1, 5):
        new = num % 128 # mod out remainder
        chars.append(new)
        num = num // 128 # floor div to get next num
    
    # use chr() to convert to characters
    myString = ''
    for num in chars:
        charForStr = chr(num) # returns a string
        # concatenate all elements together
        myString += charForStr
    
    return myString

def main():
    # handles file path issues
    baseDir = os.path.dirname(os.path.abspath(__file__))
    inputPath = os.path.join(baseDir, "input.txt")
    outputPath = os.path.join(baseDir, "output.txt")

    while True: 
        #sleep while waiting for input.txt
        with open(inputPath, "r") as f: 
            # get data from file
            rawTxt = f.read() 
        
        # if we do not read, loop
        if not rawTxt: 
            time.sleep(1) 
            continue 

        # first char determines encryption vs. decryption
        charType = rawTxt[0]
        # remove the first character from the body of text
        rawTxt = rawTxt[1:] 

        with open(inputPath, "w") as f:
            f.write("") # erases the input text

        if (charType == 'e'): # first char e = encryption mode
            print('encrypting...')
            encrypt(rawTxt, outputPath)
        
        elif (charType == 'd'): # first char d = decryption mode
            print('decrypting...')
            decrypt(rawTxt, outputPath)
        
        else:
            print("Error: Main program sent unrecognized first character.")

        time.sleep(1)

if __name__ == "__main__":
    main()