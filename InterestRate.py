print(' Welcome to FinTech company where  you find your loan  interest is more less ')
principle = int(input("Enter your principle amount:"))
rate = int(input("Enter the annual interest rate:"))
year = int(input("Enter the  duration:"))
p = principle
r = (rate)/12
n = year * 12
m = ((p*(r*(1 + r)**n))/ (1 + r)**n -1

print(' your monthly payment isb$',m')