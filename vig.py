# This method works!
def Encrypt_And_Decrypt(plaintext, keyword, decrypting):
    plaintext = plaintext.lower()
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890 ,.'
    ciphertext = ""

    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        plain_char_i = chars.find(plain_char)

        key_char = keyword[i % len(keyword)]
        key_char_i = chars.index(key_char)

        if plain_char_i == -1 or key_char_i == -1:
            ciphertext += plain_char  
            continue
        
        offset = key_char_i #add
        if decrypting == True:
            offset = offset * -1 #subtract
        
        new_index = (plain_char_i + offset + len(chars)) % len(chars)

        cipher_char = chars[new_index]
        ciphertext += cipher_char

    return ciphertext

print("Welcome to Vigenere Cipher Program!")
print("Type \'e\' for encryption.")
print("Type \'d\' for decryption.")
print("Type \'q\' to quit.")

user_Input = "default"
while user_Input != "q":
    user_Input = input("\nEcrypt (e), Decrypt (d), or quit (q)? ").lower()

    if user_Input == 'e':
        #Encrypt
        plaintext = input("Provide plaintext:\n").lower()
        keyword = input("Enter the keyword: ").lower()
        ciphertext = Encrypt_And_Decrypt(plaintext, keyword, False)

        print("Ciphered text:", ciphertext)
        
    if user_Input == 'd':
        #Decrypt
        ciphertext = input("Enter the ciphertext:\n").lower()
        keyword = input("Enter the keyword: ").lower()
        plaintext = Encrypt_And_Decrypt(ciphertext, keyword, True)
        print("Decrypted text:", plaintext)

print("Thank you for using the Vigenere Cipher program!")