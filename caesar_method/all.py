# Caesar Cipher encryption and decryption logic for files

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()
        encrypted_data = bytearray()
        for byte in data:
            encrypted_data.append((byte + key) % 256)
    
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    print("Encryption successful.")

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()
        decrypted_data = bytearray()
        for byte in data:
            decrypted_data.append((byte - key) % 256)
    
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
    print("Decryption successful.")

# Config
input_file = '../files/input.wav'  # Replace with your input file name
encrypted_file = 'sample_encrypted.txt'  # Replace with desired output file name for encrypted file
decrypted_file = 'sample_decrypted.wav'  # Replace with desired output file name for decrypted file

EncryptionMode = 0
DecryptionMode = 1

def main():
    mode = input(f"Choose mode ({EncryptionMode} for encrypt, {DecryptionMode} for decrypt): ")
    mode = int(mode)
    if mode == EncryptionMode:
        print(f"\tEncryption Mode:")
        # Encrypt file
        encryption_key = input("Specify key to encrypt (int): ")
        encryption_key = int(encryption_key)
        encrypt_file(input_file, encrypted_file, encryption_key)
    elif mode == DecryptionMode:
        print(f"\tDecryption Mode:")
        # Decrypt file
        encryption_key = input("Specify key to decrypt (int): ")
        encryption_key = int(encryption_key)
        decrypt_file(encrypted_file, decrypted_file, encryption_key)
    else:
        print(f"[x] Undefinied mode ({mode}). Available: {EncryptionMode}, {DecryptionMode}.")


if __name__ == "__main__":
    main()