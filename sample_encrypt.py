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
