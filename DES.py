#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def encrypt_message(key, message):
    cipher = DES.new(key, DES.MODE_ECB)
    message = pad(message.encode(), 8)
    ct_bytes = cipher.encrypt(message)
    return b64encode(ct_bytes).decode('utf-8')

def decrypt_message(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    ct = b64decode(ciphertext)
    pt = cipher.decrypt(ct)
    return unpad(pt, 8).decode('utf-8')

# Contoh penggunaan
key = get_random_bytes(8)  # Generate random 8-byte key
message = "Hai, ini tugas DES dari matkul SKD"

ciphertext = encrypt_message(key, message)
print("Ciphertext:", ciphertext)

decrypted_message = decrypt_message(key, ciphertext)
print("Decrypted message:", decrypted_message)


# In[ ]:





# In[ ]:




