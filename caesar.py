from file import read_text_file, write_text_file

def en_caesar(text, key):  # str, int alıyor
    result = ""

    ASCII_ELEMENT_START = ' '  # Kullandığımız ASCII listesinin başlangıç elemanının değeri
    ASCII_ELEMENT_COUNT = 95   # Space ve Del dışındaki ASCII karakter sayısı

    key = key % ASCII_ELEMENT_COUNT

    for char in text:
        base = ord(ASCII_ELEMENT_START)
        newChar = chr(base + ((ord(char) - base + key) % ASCII_ELEMENT_COUNT))
        result += newChar

    return result

def de_caesar(text, key):
    return en_caesar(text, -key)

## Dosya şifreleme / çözme 

def encrypt_file_caesar(input_path, output_path, key_num: int):
    text = read_text_file(input_path)
    encrypted = en_caesar(text, key_num)
    write_text_file(output_path, encrypted)

def decrypt_file_caesar(input_path, output_path, key_num: int):
    text = read_text_file(input_path)
    decrypted = de_caesar(text, key_num)
    write_text_file(output_path, decrypted)