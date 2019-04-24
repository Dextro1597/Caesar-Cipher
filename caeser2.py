#code by Ahad Patel
plaintext = input('Enter the message:')
key= input('Enter the bits by which we want to shift it:')
cipher=''
dicipher=''

for c in plaintext:
	if c.isupper():
		cipher += chr((ord(c) + int(key) - 65) % 26 + 65)
	else :
		cipher += chr((ord(c) + int(key) - 97) % 26 + 97)


for c in cipher:
	if c.isupper():
		dicipher += chr((ord(c) - int(key) - 65) % 26 + 65)
	else :
		dicipher += chr((ord(c) - int(key) - 97) % 26 + 97)

print('Number of shifts:' +str(key))
print('your encrypted message is:' +cipher)	
print('your decrypted message is:' +dicipher)

