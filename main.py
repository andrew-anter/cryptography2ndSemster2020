# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:35:00 2020

@author: andrew-anter
"""


def encryptShiftCipher( x , k ):   ## x is the message , k is the key #ek(x) = y s= ( x + k ) mod26
    alphabet = 'abcdefghigklmnopqrstuvwxyz'  
    y = ""
    x = x.lower()
    
    
    for i in x : 
        if i == " " :
            y += " "
        else :
            y += alphabet[ ( alphabet.index(i) + k ) % 26 ] 
    
    return y


def decryptShiftCipher( y , k ):   ## y is the *encrypted* message , k is the key #dk(y) = x = ( y + k ) mod26
    alphabet = 'abcdefghigklmnopqrstuvwxyz'  
    x = ""
    y = y.lower()
    
    
    for i in y : 
        if i == " " :
            x += " "
        else :
            x += alphabet[ ( alphabet.index(i) - k ) % 26 ] 
    
    return x


##################################################################
def main() :
    x,k = input(),int(input())    
    print( decryptShiftCipher( encryptShiftCipher(x,k) , k ) )
    
if __name__ == "__main__" :
    main()
##################################################################


