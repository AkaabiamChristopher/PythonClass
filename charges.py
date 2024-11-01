number = int(input('Enter days late: '))

if number <=6:
	print('5 days, the fine is 50 paise')
if number >=6 and number<=10:
	print('6-10 day one rupees,')
if number  >=10 and number<=30:
	print('after 10 days 5 rupees: ')
if number   > 30:
	print('return after 30 day membership is cancelled: ')