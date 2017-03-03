number = 1000

for x in range(2,number+1):
  for y in range(2,x+1):
        rem = x % y
        if rem is 0:
            if y<x:
                break
            else:
                print(x, "is prime number")
