# Simple-Crypto-CTF  
### by Michelle Sun  

Welcome to the Simple-Crypto-CTF repository. This project contains several cryptographic challenges, each accompanied by detailed explanations and scripts to help solve them. 

For comprehensive documentation on each challenge, please refer to the markdown files located in the `WriteUp` folder.

---

### Contents

- **WriteUp Folder**  
  The `WriteUp` folder contains detailed explanations for each challenge, including screenshots, code snippets, and the steps taken to solve the tasks. Please review these markdown files for insights into the thought process behind each solution.

- **Scripts Folder**  
  The `Scripts` folder contains Python scripts that were used to solve the challenges. These scripts are linked to each challenge's write-up for reference.

- **CTF-Crypto Folder**  
  The `CTF-Crypto` folder contains the ciphertexts and encrypted files used in the challenges. **Note**: Some ciphertext files may not work correctly because they are not plain text files. To resolve this issue, simply rename the file with a `.txt` extension to work with the provided scripts.

- **Media Folder**
  The `Media` folder contains the images and screenshots used in the explainations within `WriteUp`. 

---

### Notable Challenges

1. **Challenge 1**  
   A Caesar cipher challenge where the ciphertext was decrypted using a brute-force script to shift through possible keys.

2. **Challenge 2**  
   A substitution cipher solved using frequency analysis, with clues hidden in references to literature like *Harry Potter*.

3. **Challenge 3**  
   An XOR-encrypted zip file challenge, where part of the key was discovered using known plaintext (the zip header) to partially decrypt the file and reveal key patterns.

4. **Challenge 4**  
   An image encrypted with ECB block cipher, identified by noticeable repetition in the hex-encoded ciphertext, eventually leading to the recovery of the flag using header manipulation.

---

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/mlxs/Simple-Crypto-CTF.git
   cd Simple-Crypto-CTF
   ```

2. Make sure you have Python installed. The scripts use common libraries such as sys and binascii, which should be available by default in Python installations.

3. For each challenge, navigate to the WriteUp folder and follow the instructions in the markdown files to run the corresponding Python scripts.

### Known Issues
- **Ciphertext Format:** Some files in the CTF-Crypto folder are not text files by default. Rename the files with a .txt extension for the scripts to handle them properly.