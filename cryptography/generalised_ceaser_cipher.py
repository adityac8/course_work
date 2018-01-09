# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:07:13 2017

@author: aditya
"""

#from sklearn.preprocessing import LabelEncoder
import string
arr1=list(string.lowercase)
dict_={}
for i in range(len(arr1)):
    dict_[arr1[i]] = i

def convert_to_number(num1):
    return dict_[num1]

def convert_to_alphabet(value):
    return next((k for k, v in dict_.items() if v == value), None)    


#str1="plain text"
str1=raw_input("Enter plain text\n")
key=int(raw_input("Enter key\n"))


print "Original Text"
encrypted_str=[]
print str1

print "Encrypt"
for x in str1:
    if x==' ':
        encrypted_str.append(' ')
    else:
        numbx=convert_to_number(x)
        new_val=(numbx+key)%26
        x_orig=convert_to_alphabet(new_val)
        encrypted_str.append(x_orig)
strx = ''.join(encrypted_str)
print strx

print "Decrypt"
decrypted_str=[]
for x in strx:
    if x==' ':
        decrypted_str.append(' ')
    else:
        numbx=convert_to_number(x)
        new_val=(numbx-key)%26
        x_orig=convert_to_alphabet(new_val)
        decrypted_str.append(x_orig)
stry = ''.join(decrypted_str)
print stry


    
"""
le1 = LabelEncoder()
le1.fit(arr1)

x1=le1.transform(test_y)
print x1
"""
#x='a'
#print x+3