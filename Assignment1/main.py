# -*- coding: utf-8 -*-
"""
@author: andrew-anter
"""
## Libraries needed ##
import sys      #parsing text from commandline 
import math     #using gcd()

## Global Variables Declaration ##
alphabet = 'abcdefghigklmnopqrstuvwxyz'


#################Shift Cipher ######################################################
## x is the message , k is the key(integer key) # y = ek(x) = ( x + k ) mod26
def encryptShiftCipher( x , k ):   
    y = ""
    x = x.strip().lower()

    for i in x : 
        if i == " " :
            y += " "
        else :
            y += alphabet[ ( alphabet.index(i) + k ) % 26 ] 

    return y + '\n'


## x is the *encrypted* message , k is the key (integer key) # x = dk(y) = ( y + k ) mod26
def decryptShiftCipher( x , k ):   
    y = ""
    x = x.strip().lower()

    for i in x : 
        if i == " " :
            y += " "
        else :
            y += alphabet[ ( alphabet.index(i) - k ) % 26 ] 

    return y + '\n'
#####################################################################


###############Vigenere Cipher#######################################
## x is the message , k is the key (string key) # y = ek(x)  = ( x(i) + k(i) ) mod26
def encryptVigenereCipher( x , k ):   
    y = ""
    x = x.strip().lower()
    k = k.lower()
    
    for i in x :
        k += k
        
    for i in range( len(x) ) : 
        if x[i] == " " :
            y += " "
        else :
            y += alphabet[ ( alphabet.index( x[i] ) + alphabet.index( k[i] ) ) % 26 ] 
    
    return y + '\n'


## x is the message , k is the key (string key) # x = dk(y)  = ( y(i) - k(i) ) mod26
def decryptVigenereCipher( x , k ):   
    y = ""
    x = x.strip().lower()
    k = k.lower()
    
    for i in x :
        k += k
        
    for i in range( len(x) ) : 
        if x[i] == " " :
            y += " "
        else :
            y += alphabet[ ( alphabet.index( x[i] ) - alphabet.index( k[i] ) ) % 26 ] 
    
    return y + '\n'

#####################################################################


###############Affine Cipher#######################################
## y = ek(x) = (a*x + b) mod26
def encryptAffineCipher(x,a,b):
    y = ""
    x = x.strip().lower()

        
    for i in x : 
        if i == " " :
            y += " "
        else :
            y += alphabet[(alphabet.index(i)*a +b) %26] 
    
    return y + '\n'


## y = dk(x) = ((x-b)*a^(-1)) mod26
def decryptAffineCipher(x,a,b):
    y = ""
    x = x.strip().lower()
    
    for i in x : 
        if i == " " :
            y += " "
        else :
            y += alphabet[( (alphabet.index(i) -b)*(1/a) ) %26] 
    
    return y + '\n'



##################################################################
def main() :
    #x,k = input(),input()    
    #print( decryptShiftCipher( encryptShiftCipher(x,k) , k ) )
    #print( decryptVigenereCipher( encryptVigenereCipher( x , k ),k ) )
    commandLineArguments() 
    
def commandLineArguments() :
    
    cipher = sys.argv[1]

    ## shift cipher ##
    if(cipher == 'shift') :
        temp = sys.argv[2]
        if(temp == 'encrypt') :
            inputFile = open(sys.argv[3],'r')
            outputFile = open(sys.argv[4],'w')

            k = int(sys.argv[5])
            
            inputLines = inputFile.readlines()
            
            for line in inputLines :
                outputFile.write( encryptShiftCipher(line,k) )
            inputFile.close()
            outputFile.close()
                
        elif(temp == 'decrypt') :
            inputFile = open(sys.argv[3],'r')
            outputFile = open(sys.argv[4],'w')

            k = int(sys.argv[5])
            
            inputLines = inputFile.readlines()
            
            for line in inputLines :
                outputFile.write( decryptShiftCipher(line,k) )
            inputFile.close()
            outputFile.close()
            
        else :
            print("no mode defined for shift cipher either \'encrypt\' or \'decrypt\'")
    
    
    ## vigenere cipher ##        
    elif(cipher == 'vigenere') :
        temp = sys.argv[2]
        if(temp == 'encrypt') :
            inputFile = open(sys.argv[3],'r')
            outputFile = open(sys.argv[4],'w')

            k = str(sys.argv[5])
            
            inputLines = inputFile.readlines()
            
            for line in inputLines :
                outputFile.write( encryptVigenereCipher(line,k) )
            inputFile.close()
            outputFile.close()
                
        elif(temp == 'decrypt') :
            inputFile = open(sys.argv[3],'r')
            outputFile = open(sys.argv[4],'w')

            k = str(sys.argv[5])
            
            inputLines = inputFile.readlines()
            
            for line in inputLines :
                outputFile.write( decryptVigenereCipher(line,k) )
            inputFile.close()
            outputFile.close()
            
        else :
            print("no mode defined for vigenere cipher either \'encrypt\' or \'decrypt\'")
    
    
    ## affine cipher ##         
    elif(cipher == 'affine') :
        temp = sys.argv[2]
        if(temp == 'encrypt') :
            
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            
            if math.gcd(a,26) != 1 :
                print("invalid \'a\' : a and 26 aren't coprime")
                sys.exit()
            
            inputFile = open(sys.argv[3],'r')
            outputFile = open(sys.argv[4],'w')
            
            inputLines = inputFile.readlines()
            
            for line in inputLines :
                outputFile.write( encryptAffineCipher(line,a,b) )
            inputFile.close()
            outputFile.close()
                
        elif(temp == 'decrypt') :
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            
            if math.gcd(a,26) != 1 :
                print("invalid \'a\' : a and 26 aren't coprime")
                sys.exit()
            
            inputFile = open(sys.argv[3],'r')
            outputFile = open(sys.argv[4],'w')
            inputLines = inputFile.readlines()
            
            for line in inputLines :
                #print(line)
                outputFile.write( decryptAffineCipher(line,a,b) )
            inputFile.close()
            outputFile.close()
            
        else :
            print("no mode defined for Affine cipher either \'encrypt\' or \'decrypt\'")
    
    else:
        print("ERROR no cipher is given either \'shift\' or \'affine\' or \'vigenere\'")
        
    
    
    
if __name__ == "__main__" :
    main()
##################################################################


