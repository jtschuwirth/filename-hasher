import os
from cryptography.fernet import Fernet

key = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM="
fernet = Fernet(key)


def decryptFilesFromDirectory(directory):
    for filename in os.listdir(directory):
        decryption = fernet.decrypt(filename[:-4]).decode()
        os.rename(
            os.path.join(directory, filename), 
            f"files/{decryption}"
            )
        print("decrypted file:", filename, "to:", decryption)

decryptFilesFromDirectory("./files")