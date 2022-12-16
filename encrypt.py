import os
from cryptography.fernet import Fernet

key = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM="
fernet = Fernet(key)


def encryptFilesFromDirectory(directory, encrypt_words):
    count = 0
    for filename in os.listdir(directory):
        if filename == ".gitkeep":
            continue
        file_words = filename[:-4].split(" ")
        words_to_encrypt = []
        other_words = []
        for word in file_words:
            if word in encrypt_words:
                words_to_encrypt.append(word)
            else:
                other_words.append(word)
        string_to_encrypt = " ".join(str(x) for x in words_to_encrypt)

        if words_to_encrypt:
            encrypt = fernet.encrypt(string_to_encrypt.encode()).decode()
            final_filename = f"{count} {' '.join(str(x) for x in other_words)} {encrypt}"
            os.rename(
                os.path.join(directory, filename),
                f"files/{final_filename}.png"
            )
            print("encrypted file:", filename)
        count+=1


words = []
with open('encryption_words.txt') as lines:
    for line in lines:
        line = line.strip("\n")
        words.append(line)


encryptFilesFromDirectory("./files", words)
