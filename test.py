def xor_encrypt_decrypt(data, key):
    # Initialize the encrypted/decrypted result as an empty string
    result = ''

    # Perform XOR operation for each character of data with the corresponding character of the key
    for i in range(len(data)):
        # Calculate the ASCII value of the XOR result
        xor_result = ord(data[i]) ^ ord(key[i % len(key)])  # Use modulo to repeat the key if it's shorter than data
        # Convert the ASCII value back to a character and add it to the result
        result += chr(xor_result)

    return result

# Example usage:
plaintext = "TUPM-21-4882,Vincent Robles,June 27 2003,20,Male,4416 F. Macabagdal St. Brgy Ugong Valenzuela City,BSIS-NS,3"
encryption_key = "mysecretkey"

encrypted_data = xor_encrypt_decrypt(plaintext, encryption_key)
print("Encrypted:", encrypted_data)

decrypted_data = xor_encrypt_decrypt(encrypted_data, encryption_key)
print("Decrypted:", decrypted_data)
