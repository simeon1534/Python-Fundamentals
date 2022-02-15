import re
#.*(?<=@)(?P<planet>[A-Z][a-z]+)[^@!>-]*(?<=:)(?P<population>\d+)[^@:>-]*(?<=!)(?P<command>[AD])(?=!)[^@:]*(?<=->)(?P<soldiers>\d+).*
pattern=r".*(?<=@)(?P<planet>[A-Z][a-z]+)[^@!>-]*(?<=:)(?P<population>\d+)[^@:>-]*(?<=!)(?P<command>[AD])(?=!)[^@:]*(?<=->)(?P<soldiers>\d+).*"
lines_data = int(input())

attacked_planets=[]
destroyed_planets=[]

def key_count(data):
    data_lower = data.lower()
    star_letters = data_lower.count("s") + data_lower.count("t") + data_lower.count("a") + data_lower.count("r")
    return star_letters


def decrypting_data(data, key):
    decrypt_res = ''
    for letter in data:
        decrypt_res += chr(ord(letter) - key)
    return decrypt_res

for i in range(1, lines_data + 1):
    data = input()
    key = key_count(data)
    decrypted_result = decrypting_data(data, key)
    the_match=re.finditer(pattern,decrypted_result)
    for single_match in the_match:
        match_dictionary=single_match.groupdict()
        if match_dictionary['command']=='A':
            attacked_planets.append(match_dictionary['planet'])
        else:
            destroyed_planets.append(match_dictionary['planet'])
   # print(decrypted_result)
    #print(key)

print(f"Attacked planets: {len(attacked_planets)}")
attacked_planets.sort()
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
destroyed_planets.sort()
for planet in destroyed_planets:
    print(f"-> {planet}")