def get_double_digit(number):
	return [x+x for x in number]
print(get_double_digit([1,2,3]))



def words_greater_than_five(words:list)-> str:
	return[x for x in words if len(x) >= 5 ]
print(words_greater_than_five(['apple','fish','orange','ice','lime']))