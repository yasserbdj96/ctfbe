from ctfbe import ctfbe
#to encrypt:
ctfbe("<THE_PATH_TO_THE_FILE_TO_BE_ENCRYPTED>").encode(passw="<PASSWORD>")
#to decode:
ctfbe("<THE_PATH_TO_THE_FILE_TO_BE_DECRYPTED>").decode(passw="<PASSWORD>",key_path="<KEY_FILE_PATH>")
