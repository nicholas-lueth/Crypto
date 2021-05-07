# This decodes and encode affine ciphers
# Created by Nicholas Lueth

import math
import string


def dc(ct):
    return_list = []
    for i in ct:
        return_list.append(letters_to_nums[i])
    return return_list


alphabet = string.ascii_letters[:26].upper()
letters_to_nums = {}
nums_to_letters = {}
for i, char in enumerate(alphabet):
    letters_to_nums[char] = i
for i, char in enumerate(alphabet):
    nums_to_letters[str(i)] = char

print(f"Letters2Num = {letters_to_nums}\nNum2Letters = {nums_to_letters}")
preText = "OPAMKNYIBYTXYPOBYNYTTYLCITTXYYVHMPTXOCEYCCIGYICHOGOTCTXYAGOBYAMKIVKEZYLAMKSONNVYYHNITYLMVZGHHX"

text = dc(preText)
a = 17
b = 8
mod = 26
print(text)


def encrypt():
    new_str = ""
    for i in range(len(text)):
        try:
            new_str += nums_to_letters[str((a * text[i] + b) % mod)]
        except KeyError:
            new_str += nums_to_letters[str(((a * text[i] + b) % mod) + 26)]
    print(new_str)


def decrypt():
    new_str = ""
    for i in range(len(text)):
        new_str += nums_to_letters[str((inverse(a, mod) * (text[i] - b)) % mod)]
    return new_str


def inverse(num, modular):
    # Set the variables
    gcd = math.gcd(num, modular)
    # Answer is a counter that increments with every failed iteration
    answer = 0

    if num % 2 == 0 and modular % 2 == 0:
        print("There is no modular inverse!")
        exit(0)

    while True:
        # If the remainder of num * answer / mod is the gcd then the answer is the modular inverse
        if (num * answer) % modular == gcd:
            break
        # If the the remainder isn't the gcd then increment the answer and try again
        else:
            answer += 1
    return answer


print(decrypt())
