import os
from cryptography.fernet import Fernet

key = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM="
fernet = Fernet(key)


def encryptFilesFromDirectory(directory):
    for filename in os.listdir(directory):
        encryption = str(fernet.encrypt(filename.encode()))[2:]
        os.rename(
            os.path.join(directory, filename), 
            f"files/{encryption}.png"
            )
        print("encrypted file:", filename, "to:", encryption)


encryptFilesFromDirectory("./files")
