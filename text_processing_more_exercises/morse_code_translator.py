morse_code = input().strip().split("|")
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def get_key(val):
    for key, value in MORSE_CODE_DICT.items():
        if val == value:
            return key

    return "key doesn't exist"


def translator(morse_code):
    result = ""
    decrypt_to_alphabet_char = ""
    for sequence in morse_code:
        strip_seq=sequence.strip()
        result+=" "
        for i in range(len(strip_seq)):
            if strip_seq[i] == " " :
                result+=get_key(decrypt_to_alphabet_char)
                decrypt_to_alphabet_char = ""
            else:
                decrypt_to_alphabet_char += strip_seq[i]
                if i == len(strip_seq) - 1:
                    result += get_key(decrypt_to_alphabet_char)
                    decrypt_to_alphabet_char = ""
    stripped_result=result.strip()
    return stripped_result




print(translator(morse_code))
#print(morse_code)
