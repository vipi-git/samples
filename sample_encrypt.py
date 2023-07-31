#### sample codes below ###

#encryptiom

from cryptography.fernet import Fernet

# Generate a new encryption key (do this only once and keep it safe)
encryption_key = Fernet.generate_key()

# Encrypt the API key
fernet = Fernet(encryption_key)
encrypted_api_key = fernet.encrypt(b'your_api_key_here')

# Save the encrypted API key to a file
with open('encrypted_key.bin', 'wb') as file:
    file.write(encrypted_api_key)

# Access the API key in your code
with open('encrypted_key.bin', 'rb') as file:
    encrypted_api_key = file.read()

fernet = Fernet(encryption_key)
api_key = fernet.decrypt(encrypted_api_key).decode()
print(api_key)

## fetching Env data

import os

# Set the API key as an environment variable
os.environ['API_KEY'] = 'your_api_key_here'

# Access the API key in your code
api_key = os.environ.get('API_KEY')
print(api_key)

# read encryption key from environment variables and decrypt 

import os
from cryptography.fernet import Fernet

# Read the encryption key from the environment variable
encryption_key_str = os.environ.get('ENCRYPTION_KEY')
if not encryption_key_str:
    raise ValueError("Encryption key not found in the environment variable.")

# Convert the encryption key from string to bytes
encryption_key = bytes.fromhex(encryption_key_str)

# Read the encrypted data from the file
with open('encrypted_data.bin', 'rb') as file:
    encrypted_data = file.read()

# Decrypt the data
fernet = Fernet(encryption_key)
decrypted_data = fernet.decrypt(encrypted_data).decode()

# Print the decrypted data
print(decrypted_data)


