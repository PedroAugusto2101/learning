"""
DocString
I can write
what I want to

sdassdfafdsf
"""

''' use to write your notes '''

# Allows you to write a comment
print(123) # In front of
# Under
print(456)

import secrets

# Gerar uma sequência de 256 bits usando moeda (0 = cara, 1 = coroa)
num_bits = 256
entropy_bits = [secrets.choice([0, 1]) for _ in range(num_bits)]

# Converter para uma string binária
entropy_bin = ''.join(map(str, entropy_bits))

# Converter para hexadecimal (mais legível)
entropy_hex = hex(int(entropy_bin, 2))[2:]

print(f"Entropia (binária): {entropy_bin}")
print(f"Entropia (hex): {entropy_hex}")
