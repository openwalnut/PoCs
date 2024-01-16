# PoC of Apache Ofbiz Hash Cracker

This script is a simple utility for hashing passwords and searching for specific hashes within a file. It is designed for educational purposes to demonstrate password hashing techniques. The script allows users to input a hash type, salt, and a wordlist of passwords to be hashed which allows users to search for a specific hash. 

The script is based on the original Apache Offbiz [java code](https://github.com/apache/ofbiz/blob/trunk/framework/base/src/main/java/org/apache/ofbiz/base/crypto/HashCrypt.java).

## Disclaimer 

This script is provided for educational purposes only. It is intended for learning and understanding
how password hashing and comparison work. The authors and contributors of this script do not endorse or encourage
any malicious use. Use of this script for any unauthorized or harmful activities is strictly prohibited.

Please use this script responsibly and ethically, and respect the privacy and security of others.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/openwalnut/apache-ofbiz-hash-cracker.git
    cd apache-ofbiz-hash-cracker
    ```

2. Run the script:

    ```bash
    python3 ofbiz_hash_cracker.py
    ```

3. Follow the prompts to input hash type, salt, input file path, and the hash to search for (optional).

4. View the results or follow the on-screen instructions.

## Contribution

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
