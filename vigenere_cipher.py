import string


def generate_vigenere_table_U():
    UpperCaseAlphabet = string.ascii_uppercase
    vigenere_table_U = [[0]*26 for _ in range(len(UpperCaseAlphabet))]

    for row in range(len(UpperCaseAlphabet)):
        for column in range(len(UpperCaseAlphabet)):
            vigenere_table_U[row][column] = UpperCaseAlphabet[(row+column) % len(UpperCaseAlphabet)]
    return vigenere_table_U


def generate_vigenere_table_L():
    LowerCaseAlphabet = string.ascii_lowercase
    vigenere_table_L = [[0]*26 for _ in range(len(LowerCaseAlphabet))]

    for row in range(len(LowerCaseAlphabet)):
        for column in range(len(LowerCaseAlphabet)):
            vigenere_table_L[row][column] = LowerCaseAlphabet[(row+column) % len(LowerCaseAlphabet)]
    return vigenere_table_L

def key_extend(key, targetSize):
    key_ext = key * (targetSize//len(key)) + key[:(targetSize % len(key))]
    return key_ext


def EncryptV(text, key, targetSize):
    key = key_extend(key, targetSize)
    convertedText = list(text)
    tableU = generate_vigenere_table_U()
    tableL = generate_vigenere_table_L()
    UpperCaseAlphabet = list(string.ascii_uppercase)
    LowerCaseAlphabet = list(string.ascii_lowercase)
    keyIndex = 0
    for index, char in enumerate(text):
        if char in UpperCaseAlphabet:
            row = UpperCaseAlphabet.index(key[keyIndex])
            col = UpperCaseAlphabet.index(char)
            convertedText[index] = tableU[row][col]
            keyIndex += 1
        elif char in LowerCaseAlphabet:
            row = LowerCaseAlphabet.index(key[keyIndex].lower())
            col = LowerCaseAlphabet.index(char)
            convertedText[index] = tableL[row][col]
            keyIndex += 1
        else:
            pass
    return ''.join(convertedText)


def DecryptV(text, key, targetSize):
    key = key_extend(key, targetSize)
    convertedText = list(text)
    tableU = generate_vigenere_table_U()
    tableL = generate_vigenere_table_L()
    UpperCaseAlphabet = list(string.ascii_uppercase)
    LowerCaseAlphabet = list(string.ascii_lowercase)
    keyIndex = 0
    for index, char in enumerate(text):
        if char in UpperCaseAlphabet:
            row = UpperCaseAlphabet.index(key[keyIndex])
            for col in range(len(UpperCaseAlphabet)):
                if tableU[row][col] == char:
                    convertedText[index] = tableU[0][col]
                    keyIndex += 1
        if char in LowerCaseAlphabet:
            row = LowerCaseAlphabet.index(key[keyIndex].lower())
            for col in range(len(LowerCaseAlphabet)):
                if tableL[row][col] == char:
                    convertedText[index] = tableL[0][col]
                    keyIndex += 1
        else:
            pass
    return ''.join(convertedText)

