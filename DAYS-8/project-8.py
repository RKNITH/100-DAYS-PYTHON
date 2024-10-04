#  CAESAR CIPHER 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Type ENCODE to encrypt, type DECODE to decrypt: ').lower()

text = input('Type your message: ').lower()
shift = int(input('Type the shift number: '))

# Encryption function
def encrypt(text):
    msg = []
    for let in text:
        if let in alphabet:
            index = alphabet.index(let)
            new_index = (index + shift) % 26
            msg.append(alphabet[new_index])
        else:
            msg.append(let)  # Append non-alphabetic characters as is
    return ''.join(msg)  # Use ''.join() instead of msg.join()

# Decryption function
def decrypt(text):
    msg = []
    for let in text:
        if let in alphabet:
            index = alphabet.index(let)
            new_index = (index - shift) % 26
            msg.append(alphabet[new_index])
        else:
            msg.append(let)  # Append non-alphabetic characters as is
    return ''.join(msg)  # Use ''.join() instead of msg.join()

# Check the direction and call the corresponding function
if direction == 'encode':
    print(f"Encrypted message: {encrypt(text)}")
elif direction == 'decode':
    print(f"Decrypted message: {decrypt(text)}")
else:
    print("Invalid input! Please type ENCODE or DECODE.")
