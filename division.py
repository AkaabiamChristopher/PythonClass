x = int(input("Enter starting range: "))
y = int(input("Enter ending range: "))
p = int(input("Enter divisor: "))

count = 0

for i in range(x, y+1):
  if i % p == 0:
    count += 1

print(f"Number of integer divisible by {p} in the range [{x}, {y}]: {count}")

