import hashlib
import base64

def crypt_bytes(hash_type, salt, byte_array):
    result = f"${hash_type}${salt}$"
    result += get_crypted_bytes(hash_type, salt, byte_array)
    return result

def get_crypted_bytes(hash_type, salt, byte_array):
    try:
        hash_object = hashlib.new(hash_type)
        hash_object.update(salt.encode('utf-8'))
        hash_object.update(byte_array)
        hashed_bytes = hash_object.digest()
        encoded_hash = base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')
        return encoded_hash
    except hashlib.algorithms_available as e:
        raise RuntimeError("Error while comparing password") from e

def search_hash(hash_to_find, hash_type, salt, input_file_path):
    try:
        with open(input_file_path, 'r', encoding='latin-1') as file:
            for password in file:
                byte_array = password.strip().encode('utf-8')
                result = crypt_bytes(hash_type, salt, byte_array)
                # Allow comparison with or without trimming equals signs
                if result == hash_to_find or result.rstrip('=') == hash_to_find:
                    return f"Password: {password.strip()}, Hash: {result}"
        return "Hash not found in the file."
    except FileNotFoundError:
        return f"Error: File '{input_file_path}' not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def get_user_input(prompt, default=''):
    user_input = input(f"{prompt} [{default}]: ")
    return user_input if user_input else default

#User Options

hash_type = get_user_input("Enter hash type", "SHA1")
salt = get_user_input("Enter salt")
input_file_path = get_user_input("Enter input file path", "/usr/share/wordlists/rockyou.txt")
hash_to_find = get_user_input("Enter the hash to search for: ", "$SHA1$d$bTMXfIdaCZk4d4ZYDvcgD0KKkG8")

# If a hash is provided, perform the search
if hash_to_find:
    result = search_hash(hash_to_find, hash_type, salt, input_file_path)
    print(result)
else:
    print("\n Please provide a hash to search for.")
