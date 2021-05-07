# Code written by Nick Lueth

import string
# The cipher text
ciphertext = """nkdtz ymymw tzlmt zyfqq mnxyt wdmfi mfifh mfrun tsytx yfsiz uktwn yytxm tbfit zgyns lbtwq iymfy fhmnq 
ihfsy mnspf siutx xngqd itnyu wfhyn hfqqd dtzbt zqisy htsxy fsyqd wzsfh wtxxk tqpxy tifdb mthqf nrymf yfhmn qiits ypstb 
fsdym nslfh mnqix gwfns xyfwy xkzsh yntsn slfyg nwymf simfx frtsl xynyx rfsdn skfsy htsat qzynt sxymt zxfsi xtkit wrfsy 
fytrx nsytb mnhml timfx uzyfr dxynh utxxn gnqny dktws tynhn slfsf izqyx fhyfs iknlz wnslt zynyx uzwut wy""".upper()

# Creates a string of the alphabet in uppercase
alphabet = string.ascii_letters[:26].upper()
# Dictionary associating letters to numbers
letters_to_nums = {}
# Dictionary associating numbers to letters
nums_to_letters = {}
# Filling the dictionaries
for i, char in enumerate(alphabet):
    letters_to_nums[char] = i
for i, char in enumerate(alphabet):
    nums_to_letters[str(i)] = char

# Go through every valid key in the alphabet
for key in range(26):
    # Initialize a string to put results in
    return_string = ""
    # For every letter in the cipher text increase the character by the key
    for letter in ciphertext:
        # If the character is a letter apply the shift
        if letter.isalpha():
            return_string += nums_to_letters[str((letters_to_nums[letter] + key) % 26)]
        # Otherwise just add the character to the return string
        else:
            return_string += letter
    # Print the result string associated with the key
    print(f"Key ({key}):\n{return_string}\n")
