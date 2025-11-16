#This is the microservice to encrypt and decrypt text files :)

#libraries
import time

#Global variables
charType = ''
publicKeys = {
    # add in a set of (n, e) keys here (ex. these are small n!)
    # 4460543: 3791
    444446005879: 679
}
privateKeys = {
    # add in a set of (n, d) keys here (ex. for small n)
    # 4460543: 2351
    444446005879: 1309115239
}

#This function will encrypt the text
def encrypt(rawTxt):
    # establish lists
    # print('Encrypting...')
    
    chunkList = []
    encrypted_chunks = []

    # divide text into smaller chunks (a list of)
    while rawTxt:
        new, rawTxt = chunkText(rawTxt)
        chunkList.append(new)

    # encode chunks, then RSA encrypt them
    for chunk in chunkList:
        this_chunk = encode(chunk)

        # x^e mod n
        this_encrypted_chunk = pow(this_chunk, publicKeys[444446005879], 444446005879)

        # add to list
        encrypted_chunks.append(this_encrypted_chunk)

    to_write = ''
    for chunk in encrypted_chunks:
        to_write += (str(chunk))
        to_write += ' '
    
    with open('output.txt', 'w') as f:
        f.write(to_write)
    return to_write

#This function will decrypt the text using a key
def decrypt(rawTxt):
    # divide the string from file into numbers
    strs = rawTxt.split()
    nums = []
    for str in strs:
        num = int(str)
        nums.append(num)

    text = ''
    for num in nums:
        # decrypt based on d mod n
        new = pow(num, privateKeys[444446005879], 444446005879)
        partial = decode(new) # returns a partial string
        text += partial
    
    # eliminate whitespace if necessary
    new_text = text.rstrip()

    # return text and append to file.
    with open('output.txt', 'a') as f:
        f.write(new_text)
    return new_text

# Helper function to split string into correct block sizes
def chunkText(rawTxt):
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

# This function encodes 4 character blocks into a number.
def encode(chars):
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
        
    output = 0
    # implement division algorithm
    for i in range(0, 4):
        new = ints[i] * (128 ** i)
        output += new
    
    # return ascii ints
    return output

# This function reverses the encoding process into characters
def decode(n):
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
    
    # print(my_string)
    return my_string

def main():
    while True: #This loops reads the txt file once per second
        #sleep while waiting for input.txt
        with open("input.txt", "r") as f: 
            rawTxt = f.read() #rawTxt is just a variable holding the text!
        
        if not rawTxt: #if nothing was read...
            time.sleep(1) #sleeps for one second
            continue #start over

        #once input.txt has text in it,
        #take the first char off the file and store in charType
        charType = rawTxt[0]
        #remove the first character from the text file
        rawTxt = rawTxt[1:] #this just leaves the rest of the string minus that first char

        with open("input.txt", "w") as f:
            f.write("") #this erases the input text so that the program does not get confused
            #Don't worry! we already saved the important information in rawTxt

        if (charType == 'e'): #first char e = encryption mode
            encrypt(rawTxt)
        elif (charType == 'd'): #first char d = decryption mode
            decrypt(rawTxt)
        else:
            print("Error: Main program sent unrecognized first character.")

        time.sleep(1)

if __name__ == "__main__":
    main()