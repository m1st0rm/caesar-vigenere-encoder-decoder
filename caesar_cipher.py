import string

UpperCaseAlphabet = list(string.ascii_uppercase)
LowerCaseAlphabet = list(string.ascii_lowercase)

def EncryptC(text, step):
    convertedText = list(text)
    for index,char in enumerate(text):
        try:
            originalLetterIndex = UpperCaseAlphabet.index(char)
            newCharIndex = (originalLetterIndex+step) % len(UpperCaseAlphabet)
            convertedText[index] = UpperCaseAlphabet[newCharIndex]
            continue
        except Exception:
            pass
        try:
            originalLetterIndex = LowerCaseAlphabet.index(char)
            newCharIndex = (originalLetterIndex+step)% len(LowerCaseAlphabet)
            convertedText[index] = LowerCaseAlphabet[newCharIndex]
            continue
        except Exception:
            pass
    return ''.join(convertedText)



def DecryptC(text, step):
    convertedText = list(text)
    for index, char in enumerate(text):
        try:
            originalLetterIndex = UpperCaseAlphabet.index(char)
            newCharIndex = (originalLetterIndex-step) % len(UpperCaseAlphabet)
            convertedText[index] = UpperCaseAlphabet[newCharIndex]
            continue
        except Exception:
            pass
        try:
            originalLetterIndex = LowerCaseAlphabet.index(char)
            newCharIndex = (originalLetterIndex-step) % len(LowerCaseAlphabet)
            convertedText[index] = LowerCaseAlphabet[newCharIndex]
            continue
        except Exception:
            pass
    return ''.join(convertedText)
