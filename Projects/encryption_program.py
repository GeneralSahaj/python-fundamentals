import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print("=" * 50)
print("🔐 Secure Chat")
print("=" * 50)

print("\n🤖 System:")
print("Welcome to Secure Chat!")
print("Your message will be encrypted using a secret key.")

# Encrypt

plain_text = input("\n🧑 You: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("\n🤖 Secure Chat:")
print(f"Encrypted Message:\n{cipher_text}")

print("\n" + "=" * 50)

print("\n🤖 System:")
print("Paste an encrypted message below to decrypt it.")

# Decrypt

cipher_text = input("\n🧑 You: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("\n🤖 Secure Chat:")
print(f"Decrypted Message:\n{plain_text}")

print("\n🔒 Session Ended")
print("Thanks for using Secure Chat!")