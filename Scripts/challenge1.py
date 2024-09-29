with open("../Course-CTF1/CTF-Crypto/challenge1.txt", "r") as file:
    ciphertext = file.read()
    print(type(ciphertext))

def ascii_shift(ciphertext, shift_value):
    decrypted_text = ""
    for char in ciphertext:
        # Convert character to ASCII, apply shift, and convert back to character
        decrypted_text += chr((ord(char)-shift_value)%128)
    return decrypted_text


for shiftlength in range(1, 128): # Shifting through ASCII bounds
    decrypttext = ascii_shift(ciphertext, shiftlength)
    print(f"Shift {shiftlength}: {decrypttext}")
