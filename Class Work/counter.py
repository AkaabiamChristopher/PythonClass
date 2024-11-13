number = int(input("slot in number:"))
for count in range (1,number+1):
  for counter in range(1,(number+1)-count):
    print(counter,end=" ")
  print(count)