import random

def append_letter_or_number():
    alphabet = ['a','b','c','d','e','f']
    use_number = 0
    use_letter = 1

    letter_or_string = random.randrange(2)
    if letter_or_string == use_number:
        result = str(random.randrange(0,9))
    elif letter_or_string == use_letter:
        next_character = random.randrange(len(alphabet))
        result = str(alphabet[next_character])
    else:
        print("Uh-oh! You've got a bug. This should have selected number or letter.")
        return -1
    return result

# generates a random 16-byte NFC ID tag when a NFC is unavailable
def create_nfc_tag():
    random_nfc_tag = ''
    tag_size = 12 #96 bits (16 bytes)
    end_of_tag = tag_size - 1
    current_byte = 0
    byte_half = 0

    while current_byte < tag_size: 
        while byte_half != 2:
            random_nfc_tag += append_letter_or_number()
            byte_half += 1
        if current_byte != end_of_tag:
            random_nfc_tag += ':'
        current_byte += 1
        byte_half = 0
    return random_nfc_tag
