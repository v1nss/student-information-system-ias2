def dec(encrypted_text, keyword):
    decrypted_text = ''
    keyword_index = 0

    for char in encrypted_text:
        if char.isalpha() or char.isdigit():
            # Determine the shift amount based on the keyword character
            shift = ord(keyword[keyword_index % len(keyword)].lower()) - ord('a')
            keyword_index += 1

            # Apply the reverse shift to decrypt the current character
            if char.islower():
                shifted = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            elif char.isupper():
                shifted = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            elif char.isdigit():
                shifted = chr(((ord(char) - ord('0') - shift + 10) % 10) + ord('0'))
        else:
            shifted = char

        decrypted_text += shifted

    return decrypted_text

print(dec("Nmptigl", "SECRET"))