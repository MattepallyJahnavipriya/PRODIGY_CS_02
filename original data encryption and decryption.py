# Assign values 
data = 1281
key = 27

# Display values
print('Original Data:', data)
print('Key:', key)

# Encryption
data = data ^ key
print('After Encryption:', data)

# Decryption 
data = data ^ key
print('After Decryption:', data)
