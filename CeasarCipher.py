data = input("Enter characters to be encrypted: ")
print(' ')
listdata = list(data)
print(listdata)
ordlist = []
for character in range(0, len(listdata)):
	ordlist.append(ord(listdata[character]))

print(f'The individual ordinal values are: {ordlist}')

length = len(listdata)
print(f'The length of the input is: {length}\n')

#encryption algorithm
#values MUST fall between 31 and 127 (not 31, 127 themselves)

#input error detection

while True:
	try:
		cyphershift = int(input('Enter desired index shift: '))
		print(' ')
		break
	except ValueError:
		print('Only integers accepted')

while cyphershift > 126:
	cyphershift = cyphershift - 126
	print(f'Decreasing shift value to acceptable integer {cyphershift}')
	
while cyphershift < -126:
	cyphershift = cyphershift + 126
	print(f'Increasing shift value to acceptable integer {cyphershift}')

#basic encryption concept

encrypt0= []
benchmark0 = 127 - cyphershift
print(f'Checking for out of bounds values with {benchmark0}')
ordindex = 0

for character in range(0, len(ordlist)):
	if ordlist[ordindex] < benchmark0:
		encrypt0.append(cyphershift + ordlist[character])
		#print(f'adding {cyphershift}')
		print(f'Shifting {ordlist[ordindex]} by {cyphershift}: {encrypt0[ordindex]}\n')

		
		if encrypt0[character] < 32:
			encrypt0.append(encrypt0[character] + 95)
			encrypt0.pop(ordindex)
			print(f'negative shift detected pushing values below 32 to 126 then continuing shift: {encrypt0[ordindex]}\n')

	else:
		encrypt0.append(ordlist[character] - benchmark0 + 32)
		print(f'{ordlist[ordindex]} + {cyphershift} exceeds {benchmark0}')
		print(f'Subtracting (126 - {cyphershift}) then adding 32')
	
	ordindex +=1

print(f'First encrypted values:{encrypt0}')

print(f'Decryption key : {cyphershift}')

decrypt0 = []

for character in range(0, len(listdata)):
	decrypt0.append(chr(int((encrypt0[character]))))

print(f'Encryption cypher output: {decrypt0}\n')
print(f'Encrypted string: {"".join(decrypt0)}')