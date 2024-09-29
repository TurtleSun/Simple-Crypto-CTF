# Defined the key in hex format
key = [0x4C, 0x50, 0x43, 0x45, 0x52, 0x30]

#zipfile_header = [0x50, 0x4B, 0x03, 0x04] -> [0x4C, 0x50, 0x43, 0x45]

# XOR decryption function
def xor_decrypt(ciphertext, key):
    decrypted_text = bytearray()
    key_length = len(key)

    for i in range(len(ciphertext)):
        # XOR each byte of the ciphertext with the corresponding byte of the key
        decrypted_byte = ciphertext[i] ^ key[i % key_length]
        decrypted_text.append(decrypted_byte)

    return decrypted_text

# Function to convert decrypted content to hex and human-readable form
def format_decrypted_content(decrypted_data):
    hex_output = decrypted_data.hex()
    formatted_hex = ' '.join(hex_output[i:i+2] for i in range(0, len(hex_output), 2))  # Add spaces between pairs

    readable_output = ''.join([chr(byte) if 32 <= byte < 127 else '.' for byte in decrypted_data])  # Human-readable characters

    result = []
    # Display in chunks of 32 hex characters (16 bytes)
    for i in range(0, len(formatted_hex), 48):  # 48 characters = 16 bytes in hex (with spaces)
        chunk_hex = formatted_hex[i:i+48]
        chunk_readable = readable_output[i//3:(i//3)+16]  # Modified for readability purposes
        result.append(f"{chunk_hex}  |  {chunk_readable}")

    return "\n".join(result)

with open("../Course-CTF1/CTF-Crypto/challenge3", "rb") as file:
    ciphertext = file.read()

# Decrypt the ciphertext using XOR and the provided key
decrypted_data = xor_decrypt(ciphertext, key)
formatted_output = format_decrypted_content(decrypted_data)

output_file_path = "../Course-CTF1/CTF-Crypto/decrypted_output.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(formatted_output) 