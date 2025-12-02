
from rsa_algorithm import RSA

def main():
    print("===== RSA Encryption and Decryption =====")
    message = input("Enter a message to encrypt: ")

    # Initialize RSA object
    rsa = RSA()
    rsa.generate_keys()

    # Encrypt message
    cipher_text = rsa.encrypt(message)
    print("\n🔒 Encrypted Message:", cipher_text)

    # Decrypt message
    decrypted_message = rsa.decrypt(cipher_text)
    print("🔓 Decrypted Message:", decrypted_message)

    # Verify result
    if decrypted_message == message:
        print("\n✅ Success! Decryption matched the original message.")
    else:
        print("\n❌ Decryption failed. Something went wrong.")

if __name__ == "__main__":
    main()
