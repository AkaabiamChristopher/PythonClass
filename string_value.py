def get_numbers(String_value):
	
	return[int(letter) for letter in String_value if letter.isdigit()]
print(get_numbers('abc123def456'))