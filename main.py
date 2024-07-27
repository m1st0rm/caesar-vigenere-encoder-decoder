import string
import tkinter as tk
import re
from tkinter import filedialog
from caesar_cipher import EncryptC, DecryptC
from vigenere_cipher import EncryptV, DecryptV

fileChosen = False
fileText = ""
fileTextLettersSize = 0
selectedCaesarKey = None
selectedVigenereKey = None

def caesar_encrypt():
    resultText = EncryptC(fileText, int(selectedCaesarKey.get()))
    textConverted.config(state=tk.NORMAL)
    textConverted.delete(1.0, tk.END)
    textConverted.insert(tk.END, resultText)
    textConverted.config(state=tk.DISABLED)


def caesar_decrypt():
    resultText = DecryptC(fileText, int(selectedCaesarKey.get()))
    textConverted.config(state=tk.NORMAL)
    textConverted.delete(1.0, tk.END)
    textConverted.insert(tk.END, resultText)
    textConverted.config(state=tk.DISABLED)


def vigenere_encrypt():
    resultText = EncryptV(fileText, selectedVigenereKey.get(), fileTextLettersSize)
    textConverted.config(state=tk.NORMAL)
    textConverted.delete(1.0, tk.END)
    textConverted.insert(tk.END, resultText)
    textConverted.config(state=tk.DISABLED)

def vigenere_decrypt():
    resultText = DecryptV(fileText, selectedVigenereKey.get(), fileTextLettersSize)
    textConverted.config(state=tk.NORMAL)
    textConverted.delete(1.0, tk.END)
    textConverted.insert(tk.END, resultText)
    textConverted.config(state=tk.DISABLED)


def read_file():
    global fileChosen
    global fileText
    global fileTextLettersSize
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            fileText = file.read()
        fileChosen = True
        textFromFile.config(state=tk.NORMAL)
        textFromFile.delete(1.0, tk.END)
        textFromFile.insert(tk.END, fileText)
        textFromFile.config(state=tk.DISABLED)
    else:
        fileChosen = False
        textFromFile.config(state=tk.NORMAL)
        textFromFile.delete(1.0, tk.END)
        textFromFile.config(state=tk.DISABLED)
    update_button_states()
    for char in fileText:
        if (char in string.ascii_uppercase) or (char in string.ascii_lowercase):
            fileTextLettersSize += 1
        else:
            pass


def validate_vigenere_key(*args):
    key = selectedVigenereKey.get()
    key = re.sub('[^A-Za-z]', '', key.upper())
    key = key[:fileTextLettersSize]
    selectedVigenereKey.set(key)


def update_button_states():
    global fileChosen
    caesarEncryptButton["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    caesarDecryptButton["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    vigenereEncryptButton["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    vigenereDecryptButton["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    caesarKeyLabel["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    caesarKeySpinbox["state"] = "readonly" if fileChosen else tk.DISABLED
    vigenereKeyLabel["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    vigenereKeyEntry["state"] = tk.NORMAL if fileChosen else tk.DISABLED
    if not fileChosen:
        textConverted.config(state=tk.NORMAL)
        textConverted.delete(1.0, tk.END)
        textConverted.config(state=tk.DISABLED)



window = tk.Tk()
window.title("Шифратор/дешифратор Цезаря/Виженера для латинского текста")

selectedCaesarKey = tk.StringVar(value='1')
selectedVigenereKey = tk.StringVar(value='A')

chooseFileButton = tk.Button(window, text="Выбор текстового файла", command=read_file)
chooseFileButton.pack()

caesarEncryptButton = tk.Button(window, text="Зашифровать текст шифром Цезаря", command=caesar_encrypt, state=tk.DISABLED)
caesarEncryptButton.pack()

caesarDecryptButton = tk.Button(window, text="Расшифровать текст шифром Цезаря", command=caesar_decrypt, state=tk.DISABLED)
caesarDecryptButton.pack()

vigenereEncryptButton = tk.Button(window, text="Зашифровать текст шифром Виженера", command=vigenere_encrypt, state=tk.DISABLED)
vigenereEncryptButton.pack()

vigenereDecryptButton = tk.Button(window, text="Расшифровать текст шифром Виженера", command=vigenere_decrypt, state=tk.DISABLED)
vigenereDecryptButton.pack()

caesarKeyLabel = tk.Label(window, text="Выбор ключа для шифрования/дешифрования шифром Цезаря (от 1 до 25, по умолчанию - 1)", state=tk.DISABLED)
caesarKeyLabel.pack()

caesarKeySpinbox = tk.Spinbox(window, from_=1, to=25, textvariable=selectedCaesarKey, state=tk.DISABLED)
caesarKeySpinbox.pack()

vigenereKeyLabel = tk.Label(window, text="Ввод ключа для шифрования/дешифрования шифром Виженера (не может быть больше количества букв в тексте из файла, по умолчанию - A)", state=tk.DISABLED)
vigenereKeyLabel.pack()

selectedVigenereKey.trace_add("write", validate_vigenere_key)
vigenereKeyEntry = tk.Entry(window, textvariable=selectedVigenereKey, validate='key', validatecommand=(validate_vigenere_key, '%P'), state=tk.DISABLED)
vigenereKeyEntry.pack()

textFromFileLabel = tk.LabelFrame(window, text="Исходный текст из файла")
textFromFileLabel.pack(side=tk.LEFT, padx=10, pady=10)

textConvertedLabel = tk.LabelFrame(window, text="Зашифрованный/Расшифрованный текст")
textConvertedLabel.pack(side=tk.RIGHT, padx=10, pady=10)

textFromFile = tk.Text(textFromFileLabel, height=20, width=50, bg="lightgray", state=tk.DISABLED)
textFromFile.pack()

textConverted = tk.Text(textConvertedLabel, height=20, width=50, bg="lightblue", state=tk.DISABLED)
textConverted.pack()

window.mainloop()
