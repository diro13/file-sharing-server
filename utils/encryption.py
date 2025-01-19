from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_url(url):
    return cipher_suite.encrypt(url.encode()).decode()

def decrypt_url(encrypted_url):
    return cipher_suite.decrypt(encrypted_url.encode()).decode()
