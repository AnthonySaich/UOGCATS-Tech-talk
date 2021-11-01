import secrets# these are the libraries that are being used are inported  here.
import hashlib
import base64
salt = secrets.token_hex(16) #This makes produces a 32 character string



unsaltedpassword = 'Password2012' #This is the Users password to salt and hash
print('The password is',unsaltedpassword) 
print('THe salt is', salt)
print('The unsalted salt and password is',salt+unsaltedpassword) #This is the conbernation of the 32 character string and the password  of the 
salted_input_string = salt+unsaltedpassword#This line conbies both the salt and password into one varible
saltedpassword = hashlib.sha256(salted_input_string.encode('utf-8')).hexdigest()
print('The salted sha256 hashed password is',saltedpassword)





base64toencode = (str(input("Please enter a password to be encoded")))

print (base64toencode)

encodeed =  base64.b64encode(base64toencode.encode('ascii'))


print (encodeed)
