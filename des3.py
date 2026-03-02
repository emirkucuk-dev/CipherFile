import random
from file import read_text_file, write_text_file

## Tables ve yardımcı fonksiyonlar

def isFull(arr):
    for i in arr:
        if i == 0:
            return False
    return True

IP = [0] * 16
for i in range(16):
    index = random.randint(0, 15)
    while True:
        if IP[index] == 0:
            IP[index] = i + 1
            break
        else:
            index = random.randint(0, 15)

FP = [0] * 16
for i, val in enumerate(IP):
    FP[val - 1] = i + 1

S0 = [[14, 4, 13, 1],
      [2, 15, 11, 8],
      [3, 10, 6, 12],
      [5, 9, 0, 7]]

S1 = [[0, 15, 7, 4],
      [14, 2, 13, 1],
      [10, 6, 12, 11],
      [9, 5, 3, 8]]

def text_to_bits(text):
    bits = []
    for char in text:
        bits.extend([int(x) for x in format(ord(char), '08b')])
    return bits

def bits_to_text(bits):
    text = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        text += chr(int(''.join(str(b) for b in byte), 2))
    return text

def permutation(bits, table):
    return [bits[i-1] for i in table]

def xor_des(a, b):
    return [x ^ y for x, y in zip(a, b)]

def sboxify(bits, sbox):
    row = bits[0] * 2 + bits[3]
    col = bits[1] * 2 + bits[2]
    value = sbox[row][col]
    return [int(b) for b in format(value, '04b')]

def f_function(R, key):
    xored = xor_des(R, key)
    left = sboxify(xored[:4], S0)
    right = sboxify(xored[4:], S1)
    return left + right

def en_des(bits, key):
    bits = permutation(bits, IP)
    R = bits[8:]
    L = bits[:8]
    new_R = xor_des(L, f_function(R, key))
    return permutation(R + new_R, FP)

def de_des(bits, key):
    bits = permutation(bits, IP)
    R = bits[:8]
    new_R = bits[8:]
    L = xor_des(new_R, f_function(R, key))
    return permutation(L + R, FP)

## 3DES metin fonksiyonları 

def en_3des(text, key):
    while len(text) % 2 != 0:
        text += " "

    k1 = text_to_bits(key[0])
    k2 = text_to_bits(key[1])
    k3 = text_to_bits(key[2])

    encrypted = []
    for i in range(0, len(text), 2):
        block = text_to_bits(text[i:i+2])
        e1 = en_des(block, k1)
        e2 = de_des(e1, k2)
        e3 = en_des(e2, k3)
        encrypted.extend(e3)

    return bits_to_text(encrypted)

def de_3des(text, key):
    k1 = text_to_bits(key[0])
    k2 = text_to_bits(key[1])
    k3 = text_to_bits(key[2])

    decrypted = []
    for i in range(0, len(text), 2):
        block = text_to_bits(text[i:i+2])
        d1 = de_des(block, k3)
        d2 = en_des(d1, k2)
        d3 = de_des(d2, k1)
        decrypted.extend(d3)

    return bits_to_text(decrypted).rstrip(' ')

## Dosya şifreleme / çözme 

def encrypt_file_3des(input_path, output_path, key_text: str):
    text = read_text_file(input_path)
    encrypted = en_3des(text, key_text)
    write_text_file(output_path, encrypted)

def decrypt_file_3des(input_path, output_path, key_text: str):
    text = read_text_file(input_path)
    decrypted = de_3des(text, key_text)
    write_text_file(output_path, decrypted)
