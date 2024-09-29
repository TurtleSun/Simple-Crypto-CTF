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

with open("../Course-CTF1/CTF-Crypto/challenge4", "rb") as file:
    ciphertext = file.read()

formatted_output = format_decrypted_content(ciphertext)

output_file_path = "../Course-CTF1/CTF-Crypto/challenge4.txt"
with open(output_file_path, "w") as output_file:
    output_file.write(formatted_output) 