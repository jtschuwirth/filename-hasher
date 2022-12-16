import os
from cryptography.fernet import Fernet

key = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM="
fernet = Fernet(key)


def decryptFilesFromDirectory(directory):
    for filename in os.listdir(directory):
        if filename == ".gitkeep":
            continue
        file_words = filename[:-4].split(" ")
        decrypted_file_words = []
        for word in file_words:
            try:
                decryption = fernet.decrypt(word).decode()
                decrypted_file_words.append(decryption)
            except:
                decrypted_file_words.append(word)

        decryption = " ".join(str(x) for x in decrypted_file_words)
        os.rename(
            os.path.join(directory, filename),
            f"files/{decryption}.png"
        )


