


def get_cities(countries,country,state):
	for city in countries[country][state].items():
		print (city)

countries = {
        "USA":{"California":{"Los Angeles":4000000,"San Francisco":870000}},
        "Canada":{"Ontario":{"Toronto":2930000,"Ottawa":994837}},
	}
print(get_cities(countries,"USA","California"))