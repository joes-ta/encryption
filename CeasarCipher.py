def shiftCharacter(char, direct):
    shiftAmount = 32 #change to 0 if constraints on printable characters are lifted
    #this will accept a string or integer but only returns an integer
    if isinstance(char, str):
        char = ord(char)
    
    if direct == 'up':
        char = char + shiftAmount
    elif direct == 'down':
        char = char - shiftAmount
            
    return char 

modVal = 95 #the number of printable characters, but could be changed if constraints were lifted

while True:
    ordlist = []
    printlist = []
    data = input("Enter characters to be encrypted: ")
    print(' ')
    listdata = list(data)
    print(listdata)
    
    for character in range(0, len(listdata)):
        #shifting all the characters by -32 immediately 
        #to zero index the values for modulo math
        char = ord(listdata[character]) #unnecessary after testing
        shiftChar = shiftCharacter(listdata[character], 'down')
        #values MUST fall between 31 and 127 (not 31, 127 themselves)
        #I like this, Caesar would have had to use printable characters
        
        if shiftChar < 0 or shiftChar > modVal - 1:
            print(f'Only printable characters accepted')
            break
        else:
            ordlist.append(shiftChar)
            printlist.append(char)
        
    if len(ordlist) == len(listdata):
        break


print(f'The individual ordinal values are: {printlist}')
print(f'The ordlist values are: {ordlist}')

length = len(listdata)
print(f'The length of the input is: {length}\n')

while True:
	try:
		cyphershift = int(input('Enter desired index shift: '))
		print(' ')
		break
	except ValueError:
		print('Only integers accepted')

cyphershift = cyphershift % modVal
'''
in python this will always result in a positive value, which is congruent with
the negative values we might have arrived at in the original version
when we encrypt we will again use mod to loop the full list
'''

#basic encryption concept

encrypt0= []

for character in range(0, len(ordlist)):
    encryptChar = (ordlist[character] + cyphershift) % modVal
    encrypt0.append(encryptChar)

print(f'First encrypted values:{encrypt0}')

print(f'Decryption key : {cyphershift}')

for _ in range(len(encrypt0)):
    encrypt0[_] = shiftCharacter(encrypt0[_], 'up')
#we have shifted the values for the cypher, now we have to revert that shift to get to the printable values

decrypt0 = []
for character in range(0, len(listdata)):
	decrypt0.append(chr(int((encrypt0[character]))))

print(f'Encryption cypher output: {decrypt0}\n')
print(f'Encrypted string: {"".join(decrypt0)}')