""" 
This is clearly a caesar/sub cipher like entity since there are only english letters
First thing, character frequency checker
I see that Q is the most frequent character, so based on english frequency, Q:E 
"""

from collections import Counter

with open("../Course-CTF1/CTF-Crypto/challenge2.txt", "r") as file:
    ciphertext = file.read()

""" def analyze_frequency(ciphertext):
    # Remove non-alphabetic characters and convert to uppercase
    filtered_text = ''.join([char for char in ciphertext if char.isalpha()])
    frequencies = Counter(filtered_text)
    total_letters = sum(frequencies.values())

    # Sort frequencies from most to least common
    sorted_frequencies = frequencies.most_common()

    print("Letter Frequencies (most common to least common):")
    for letter, freq in sorted_frequencies:
        percentage = (freq / total_letters) * 100
        print(f"{letter}: {freq} ({percentage:.2f}%)")
    
    return sorted_frequencies

# Analyze the frequency of letters in the ciphertext
frequencies = analyze_frequency(ciphertext)

# Print the results
print("Most frequent letters in the ciphertext:")
print(frequencies)
"""

def substitution_decrypt(ciphertext, mapping):
    # Create a translation table based on the mapping
    table = str.maketrans(mapping)
    return ciphertext.translate(table)

# Define the initial letter mapping (Ciphertext -> English)
letter_mapping = {
    'A': 'Z', 
    'B': 'C', 
    'C': 'A', 
    'D': 'K',
    'E': 'V',   
    'F': 'X', 
    'G': 'D', 
    'H': 'H', 
    'I': 'S', 
    'J': 'T', 
    'K': 'N', 
    'L': 'J', 
    'M': 'I', 
    'N': 'U', 
    'O': 'P', 
    'P': 'G', 
    'Q': 'E', 
    'R': 'F', 
    'S': 'M', 
    'T': 'Y', 
    'U': 'B', 
    'V': 'Q', 
    'W': 'O', 
    'X': 'W', 
    'Y': 'R', 
    'Z': 'L'
}

plaintext = substitution_decrypt(ciphertext, letter_mapping)

# Print the partially decrypted text
print("Partially decrypted text:")
print(plaintext)

