import math
import string

codebook = ['cereal', 'jam', 'bread', 'eggs', 'banana', 'ramen', 'cream', 'coffee', 'meat', 'spices', 'tomatoes', 'apple', 'butter'
            'milk', 'grapes', 'cheese', 'juice', 'salt', 'sugar', 'cookies', 'flour', 'honey']


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

p = 3
q = 7
 
print("\n*****Encryption*****")

message = input("Input message for encryption: ")

n = p * q
func = (p-1) * (q-1)

#genearting secret message from user input
def getpos(text):
    secret_message = []
    for i in text:
        if i.islower():
            secret_message.append(string.ascii_lowercase.index(i))
        elif i.isupper():
            secret_message.append(string.ascii_uppercase.index(i))

    return secret_message

#calculating value of e for public key
def publickey(func):
    for i in range(2,func):
        if math.gcd(i,func) == 1:
            e = i
            break
    return e

#calculating value of d for private key
def privatekey():

    e = publickey(func)
    i = 1
    while True:
        if (e*i) % func == 1:
            d = i
            break
        else:
            i = i + 1
    return d


#function to check if number is prime or not
def prime(num):
    if num > 1:
        for i in range(2,(int(num/2)+1)):
            if num % i == 0:
                return False
        return True

    else:
        return False


#encrypting secret message
def encrypt(list1):
    if prime(p) and prime(q):
        e = publickey(func)
        encipher_m = []
        for i in list1:
            en = int(math.pow(i,e) % n)
            encipher_m.append(en)
            

        return encipher_m

    else:
        print("Numbers not prime")

#decrypting cipher text
def decrypt(list2):
    decipher_m = []
    d = privatekey()
    for i in list2:
        power = i ** d
        m = power % n
        decipher_m.append(m)
    print("\nDecrypted messsage: ",decipher_m)

    return decipher_m


print("Secret message: ",getpos(message))
#print("Cipher text: ",encrypt(getpos(message)))

cipher = []
cipher = encrypt(getpos(message))
print("Cipher: ",cipher)
ciphertext = []
for i in cipher:
    ciphertext.append(codebook[i])

print("Cipher Text: ",ciphertext)

plain = []
ciphercode = []
plaintext = ""
text = ""

print("\n*****Decryption*****")
print("Message for decryption: ",ciphertext)

for i in ciphertext:
    ciphercode.append(codebook.index(i))

#print('ciphercode: ',ciphercode)
plain = decrypt(ciphercode)
for i in plain:
    plaintext += alphabet[i]

print("Plaintext: ",plaintext,"\n")



