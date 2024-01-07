target = int(input("Input a number: "))
even_sum = 0

for number in range(2, target + 1, 2): # range(start, stop, step)
  even_sum += number

print(even_sum)