import time
import os

charType = ''
publicKeys = {
    # add in a set of (n, e) keys here (ex. these are small n!)
    444446005879: 679
}
privateKeys = {
    # add in a set of (n, d) keys here (ex. for small n)
    444446005879: 1309115239
}

# ENCRYPTION
def encrypt_prepare_chunks(rawTxt):
    # establish lists
    
    chunkList = []
    encrypted_chunks = []

    # divide text into smaller chunks (a list of)
    while rawTxt:
        new, rawTxt = helper_chunkText(rawTxt)
        chunkList.append(new)
    return chunkList, encrypted_chunks

def encrypt_process_chunks(chunkList, encrypted_chunks):
    # encode chunks, then RSA encrypt them
    for chunk in chunkList:
        this_chunk = helper_encode_output(helper_encode_ints(chunk))

        # x^e mod n
        this_encrypted_chunk = pow(this_chunk, publicKeys[444446005879], 444446005879)

        # add to list
        encrypted_chunks.append(this_encrypted_chunk)
    return encrypted_chunks

def encrypt_write_output(encrypted_chunks, outputPath):
    to_write = ''
    for chunk in encrypted_chunks:
        to_write += (str(chunk))
        to_write += ' '
    
    with open(outputPath, 'w') as f:
        f.write(to_write)
    return to_write

def encrypt(rawTxt, outputPath):
    chunkList, encrypted_chunks = encrypt_prepare_chunks(rawTxt)
    encrypted_chunks = encrypt_process_chunks(chunkList, encrypted_chunks)
    return encrypt_write_output(encrypted_chunks, outputPath)

# DECRYPTION
def decrypt_split(rawTxt):
    # Decrypt the text using a key
    # divide the string from file into numbers
    strs = rawTxt.split()
    nums = []
    for str in strs:
        num = int(str)
        nums.append(num)
    return nums

def decrypt_process_split(nums):
    text = ''
    for num in nums:
        # decrypt based on d mod n
        new = pow(num, privateKeys[444446005879], 444446005879)
        partial = helper_decode(new) # returns a partial string
        text += partial
    
        # eliminate whitespace if necessary
        new_text = text.rstrip()
    return new_text

def decrypt_write_output(new_text, outputPath):
    # return text and append to file.
    with open(outputPath, 'w') as f:
        f.write(new_text)
    return new_text

def decrypt(rawTxt, outputPath):
    nums = decrypt_split(rawTxt)
    new_text = decrypt_process_split(nums)
    return decrypt_write_output(new_text, outputPath)

# ENCRYPT/DECRYPT HELPER FUNCTIONS
def helper_chunkText(rawTxt):
    # Helper function to split string into correct block sizes
    # base case for recursion
    if len(rawTxt) < 4:
        textChunk = rawTxt
        to_add = 4 - len(textChunk)
        for i in range(1, to_add):
            textChunk += ' '    
        rawTxt = ""

    # take first 4 chars
    else:
        textChunk = rawTxt[:4]
        # remove those chars from rawTxt
        rawTxt = rawTxt[4:]

    # return both cases (we call this function recursively)
    return textChunk, rawTxt

def helper_encode_ints(chars):
    # Encodes 4 character blocks into a number.
    ints = []
    # use ord() to convert to ascii
    if len(chars) < 4:
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
    return ints

def helper_encode_output(ints):
    output = 0
    # implement division algorithm
    for i in range(0, 4):
        new = ints[i] * (128 ** i)
        output += new
    
    # return ascii ints
    return output

def helper_decode(n):
    # This function reverses the encoding process into characters
    # implement division algorithm reversed
    chars = []
    for i in range(1, 5):
        new = n % 128
        chars.append(new)
        n = n // 128
    
    # use chr() to convert to characters
    my_string = ''
    for num in chars:
        char_for_str = chr(num) # returns a string
        # concatenate all elements together
        my_string += char_for_str
    
    return my_string

# MAIN HELPER FUNCTIONS

def main_helper_read(inputPath):
    while True: # This loops reads the txt file once per second
        # sleep while waiting for input.txt
        with open(inputPath, "r") as f: 
            return f.read() # variable holding the text
        
def main_helper_write(inputPath):
    with open(inputPath, "w") as f:
            f.write("") # this erases the input text so that the program does not get confused

def main_helper_char(charType, rawTxt, outputPath):
    if (charType == 'e'): #first char e = encryption mode
        encrypt(rawTxt, outputPath)
    elif (charType == 'd'): #first char d = decryption mode
        decrypt(rawTxt, outputPath)
    else:
        print("Error: Main program sent unrecognized first character.")

# MAIN
def main():
    baseDir = os.path.dirname(os.path.abspath(__file__))
    inputPath = os.path.join(baseDir, "input.txt")
    outputPath = os.path.join(baseDir, "output.txt")

    while True:
        rawTxt = main_helper_read(inputPath)
        if not rawTxt: # if nothing read, sleep then repeat
            time.sleep(1)
            continue

        # once input.txt has text in it,
        # take the first char off the file and store in charType
        charType = rawTxt[0]
        # remove the first character from the text file
        rawTxt = rawTxt[1:] # this just leaves the rest of the string minus that first char
        
        main_helper_write(inputPath)
        main_helper_char(charType, rawTxt, outputPath)
        time.sleep(1)

if __name__ == "__main__":
    main()
