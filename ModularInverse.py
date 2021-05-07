# Code written by Nick Lueth

import math
import sys
# Set the variables
num = 3
mod = 26
gcd = math.gcd(num, mod)
# Answer is a counter that increments with every failed iteration
answer = 0

if num % 2 == 0 and mod % 2 == 0:
    print("There is no modular inverse!")
    exit(0)

while True:
    # If the remainder of num * answer / mod is the gcd then the answer is the modular inverse
    if (num * answer) % mod == gcd:
        break
    # If the the remainder isn't the gcd then increment the answer and try again
    else:
        answer += 1

# Print the answer
print(answer)
