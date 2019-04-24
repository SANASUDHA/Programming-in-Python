#Python Program- Convert Binary to Decimal

binary = raw_input('enter a number in binary : ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print(decimal)
