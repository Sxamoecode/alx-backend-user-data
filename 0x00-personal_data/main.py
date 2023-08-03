#!/usr/bin/env python3
"""
Encryption main file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid


password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))

print('\n')
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))
