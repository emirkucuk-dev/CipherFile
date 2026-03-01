from file import read_text_file, write_text_file

def en_XOR(text, key):  # str, char alıyor
    result = []
    key_len = len(key)
    for i, char in enumerate(text):
        result.append(ord(char) ^ ord(key[i % key_len]))
    return "-".join(str(x) for x in result)

def de_XOR(text, key):
    numbers = [int(x) for x in text.split("-")]
    encrypted_string = "".join(chr(num) for num in numbers)

    result = ""
    key_len = len(key)
    for i, char in enumerate(encrypted_string):
        result_char = chr(ord(char) ^ ord(key[i % key_len]))
        result += result_char

    return result

# Dosya şifreleme / çözme
def encrypt_file_xor(input_path, output_path, key_text: str):
    text = read_text_file(input_path)
    encrypted = en_XOR(text, key_text)
    write_text_file(output_path, encrypted)

def decrypt_file_xor(input_path, output_path, key_text: str):
    text = read_text_file(input_path)
    decrypted = de_XOR(text, key_text)
    write_text_file(output_path, decrypted)