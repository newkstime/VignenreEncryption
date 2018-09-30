def main():
    msg = input("Enter a multi-word message with punctuation: ").lower()
    key = input("Enter a single word key with no punctuation: ").lower()
    vig_square = create_vig_square()
    coded_msg, paired_key = encrypt(msg, key, vig_square)
    print("The encoded message is: ")
    print(coded_msg)
    decoded_msg = decrypt(coded_msg, paired_key, vig_square)
    print("The decoded message is: ")
    print(decoded_msg)

def encrypt(msg, key, vig_square):
    coded_msg = ""
    paired_key = pair_key_to_msg(key, msg)
    row_index = 0
    for msg_char in msg:
        if msg_char.isalpha():
            col = get_col_index(msg_char, vig_square)
            row = get_row_index(paired_key[row_index], vig_square)
            coded_msg = coded_msg + vig_square[row][col]
            row_index += 1
        else:
            coded_msg = coded_msg + msg_char
    return coded_msg, paired_key


def decrypt(coded_msg, key, vig_square):
    decoded_msg = ""
    row_index = 0
    for msg_char in coded_msg:
        if msg_char.isalpha():
            row = vig_square[0].index(key[row_index])
            col = vig_square[row].index(msg_char)
            decoded_char = vig_square[col][0]
            decoded_msg = decoded_msg + decoded_char
            row_index += 1
        else:
            decoded_msg = decoded_msg + msg_char
    return decoded_msg

def create_vig_square():
    counter = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    vig_square = []
    for y in range(26):
        row = []
        for x in range(26):
            row.append(alphabet[x + counter])
        counter += 1
        vig_square.append(row)
    return vig_square

def get_col_index(msg_char, vig_square):
    return vig_square[0].index(msg_char)

def get_row_index(key_char, vig_square):
    for x in range(26):
        if key_char == vig_square[x][0]:
            return x

def get_plain_text_char(coded_char, key_char, vig_square):
    raise NotImplementedError

def pair_key_to_msg(key, msg):
    paired_key = key * len(msg)
    return paired_key[0:len(msg)]


main()
