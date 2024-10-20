character_list = 'abcdefghijklmnopqrstuvwxyz1234567890 ,.'
print(len(character_list))

def get_position_of_character(character):
    global character_list
    return character_list.find(character)

def encrypt(plaintext, keyword):
    global character_list
    ciphertext = ""

    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        plain_char_index = get_position_of_character(plain_char)

        key_char = keyword[i%len(keyword)]
        key_char_index = get_position_of_character(key_char)

        if plain_char_index == -1 or key_char_index == -1:
            ciphertext += plain_char
            continue
        
        cipher_char = character_list[(plain_char_index+key_char_index)%len(character_list)]
        ciphertext += cipher_char

    return ciphertext

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

def decrypt(ciphertext,keyword):
    global character_list
    plaintext = ""

    for i in range(len(ciphertext)):
        cipher_char = ciphertext[i]
        cipher_char_index = get_position_of_character(cipher_char)

        key_char = keyword[i%len(keyword)]
        key_char_index = get_position_of_character(key_char)

        if cipher_char_index == -1 or key_char_index == -1:
            plaintext += cipher_char
            continue
        
        plain_chr = character_list[(cipher_char_index+key_char_index)%len(character_list)]

    return plaintext


print("Type \'e\' for encryption.")
print("Type \'d\' for decryption.")

user_Input = input("Give keyword\n").lower()

if user_Input == 'e':
    #Encrypt
    plaintext = input("Provide plaintext\n").lower()
    keyword = input("Enter the keyword: ").lower()
    # ciphertext = encrypt(plaintext,keyword)
    ciphertext = Encrypt_And_Decrypt(plaintext, keyword, False)

    print("Ciphered text:", ciphertext)
        
    
if user_Input == 'd':
    #Decrypt
    ciphertext = input("Enter the ciphertext: ").lower()
    keyword = input("Enter the keyword: ").lower()
    # plaintext = decrypt(ciphertext, keyword)
    plaintext = Encrypt_And_Decrypt(ciphertext, keyword, True)
    print("Decrypted text: ", plaintext)

