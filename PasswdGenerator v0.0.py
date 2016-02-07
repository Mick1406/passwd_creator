#------------------------------------------------------#
# Password Generator with Integrated graphic interface #
#------------------------------------------------------#
# Output and archive passwords into a text file
# Encrypt the file using cypher

# Generate a password

import string
import random

passwdL=input("How long do you want your password to be (number of digits)?")
Nnum=input("How many numbers do you want in your password?")
Nchar=input("How many character strings do you want in your password?")
Nsymb=input("How many sepcial character (or symbol)"\
"do you want in your password?")

symbols=('$','£','#','.','?','/','!','-','\')
lsymbols=len(symbols)

if passwdL==Nnum+Nchar+Nsymb:             
    i=0
    while i<passwdL:
        j=0
        while j<Nchar:
            rand[j]=random.choice(string.ascii_letters)
            passwd=passwd+rand[j]
            j=j+1
        k=0
        while k<Nnum:
            rand[k]=random.randint(0,9)
            passwd=passwd+rand[k]
            k=k+1
        if Nsymb>0:
            l=0
            while l<Nsymb:
            rand[l]=symbols[random.randint(0,lsymbols)]
            passwd=passwd+rand[l]
            l=l+1
else:
    print("Error:Your password length does not align with your numeric"\
          "and character selection. Password creation aborted!")

print("Your new password is:",passwd)


# Encrypt the password

# Print the encrypted passowrd into a txt file

