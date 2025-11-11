#This is the microservice to encrypt and decrypt text files :)

#libraries
import time


#Global variables
charType = ''


#This function will encrypt the text
def encrypt(rawTxt):
    print("This is filler")

#This function will decrypt the text using a key
def decrypt(rawTxt):
    print("This is filler")

def main():
    while (True): #This loops reads the txt file once per second
        #sleep while waiting for encrypt.txt
        with open("encrypt.txt", "r") as f: 
            rawTxt = f.read() #rawTxt is just a variable holding the text!
        
        if not rawTxt: #if nothing was read...
            time.sleep(1) #sleeps for one second
            continue #start over
        else: #Something was read!
            break 

    #once encrypt.txt has text in it,
    #take the first char off the file and store in charType
    charType = rawTxt[0]
    #remove the first character from the text file
    rawTxt = rawTxt[1:] #this just leaves the rest of the string minus that first char

    if (charType == 'e'): #first char e = encryption mode
        encrypt(rawTxt)
    elif (charType == 'd'): #first char d = decryption mode
        decrypt(rawTxt)
    else:
        print("Error: Main program sent unrecognized first character.")