def char_to_code(char):
    if char.isalpha():
        # Alphabetical position (a=1, b=2, ...)
        return str(ord(char.lower()) - ord('a') + 1)
    elif char == ' ':
        return '00'  # space
    else:
        return '.'  # any other symbol

def encrypt_phrase(phrase):
    # Step 1: Convert phrase chars to code string (letters to numbers, spaces to 00, symbols to .)
    codes = [char_to_code(c) for c in phrase]
    base_num_str = ''.join(codes)
    
    # Step 2: Length of the base number string (digits count)
    length = len(base_num_str)
    
    # Step 3: Multiply base number by length
    # Note: Need to remove '.' before conversion to int, because '.' is non-numeric
    # So let's treat '.' as zero for arithmetic or skip encryption if symbols exist?
    # Since symbols are ".", which can't be converted to int, let's skip encryption if symbol exists.
    
    if '.' in base_num_str:
        return f"Cannot encrypt phrase with symbols, '.' detected in encoding."
    
    base_num_int = int(base_num_str)
    multiplied = base_num_int * length
    
    # Step 4: Reverse the multiplied number string
    multiplied_str = str(multiplied)
    reversed_str = multiplied_str[::-1]
    
    # Step 5: Subtract reversed number from multiplied number
    reversed_int = int(reversed_str)
    subtracted = multiplied - reversed_int
    
    # Step 6: Multiply by 2
    final_result = subtracted * 2
    
    # Step 7: Prefix with length + "/"
    encrypted = f"{length}/{final_result}"
    return encrypted

def main():
    phrase = input("Enter a word or phrase to encrypt: ")
    encrypted_phrase = encrypt_phrase(phrase)
    print(f"Encrypted: {encrypted_phrase}")

if __name__ == "__main__":
    main()