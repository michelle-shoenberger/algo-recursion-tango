def factorial(x):
	# x must be an integer 0 or greater
	if x <= 1:
		return 1
	return x * factorial(x-1)

import re
def palindrome(string):
	if len(string) <= 1:
		return True
	new_word = re.sub(r'[^\w]', '', str(string).lower()) 
	if new_word[0] != new_word[-1]:
		return False
	return palindrome(new_word[1:-1])

def bottles(num, original=None):
	if original==None: original = num
	if num == 0:
		print(f'No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {original} bottle{"s" if original>1 else ""} of beer on the wall.')
		return 1
	if num == 1:
		print(f'{num} bottle of beer on the wall, {num} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.')
		return bottles(num - 1, original)
	print(f'{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottle{"s" if num-1>1 else ""} of beer on the wall.')
	return bottles(num - 1, original)

def roman_num(num):
	romanNumeralsMap = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
	}

	for item in romanNumeralsMap:
		if num == item:
			return romanNumeralsMap[item]
		elif num > item:
			return romanNumeralsMap[item] + roman_num(num-item)