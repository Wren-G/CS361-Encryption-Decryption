#This is the microservice to encrypt and decrypt text files :)

#libraries
import time


#Global variables
charType = ''
publicKeys = {
    # add in a set of (n, e) keys here (ex. these are small n!)
    4460543: 3791
}
privateKeys = {
    # add in a set of (n, d) keys here (ex. for small n)
    4460543: 2351
}

#This function will encrypt the text
def encrypt(rawTxt):
    # log_n = 4 for our current case
    
    # split rawTxt into 4 char blocks

    # take each block into numerical (ASCII based)

    # take each num to eth power based on n, then mod n

    # return raw text or write into file
    print("This is filler")

#This function will decrypt the text using a key
def decrypt(rawTxt):
    print("This is filler")

def main():
    while (True): #This loops reads the txt file once per second
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