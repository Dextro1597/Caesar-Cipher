plaintext = input('Enter the plain text:-')
alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabetc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher = ''
dicipher = ''
key = input('Enter the key Size:-')

for c in plaintext:
	if c in alphabets:
		cipher += alphabets[(alphabets.index(c)+int(key))%(len(alphabets))]
	else:
		cipher += alphabetc[(alphabetc.index(c)+int(key))%(len(alphabetc))]

for c in cipher:
	if c in alphabets:
		dicipher += alphabets[(alphabets.index(c)-int(key))%(len(alphabets))]
	else:
		dicipher += alphabetc[(alphabetc.index(c)-int(key))%(len(alphabetc))]

print('The key size is:-' +str(key))
print('The cipher text generated is:-' +cipher)
print('The dicipher text is:-' +dicipher)
