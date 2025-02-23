countries = {
        "USA":{"California":{"Los Angeles":4000000,"San Francisco":870000}},
        "Canada":{"Ontario":{"Toronto":2930000,"Ottawa":994837}},
	}

def get_cities(countries):
	for city in countries["USA"].values():
		print(city)


get_cities(countries)