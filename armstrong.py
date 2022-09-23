x = int(input("soru"))
global total
total = 0
total_armstrong = 0
for i in range(x):
	for j in range(len(str(i))):
		sx = str(i)
		total += int(sx[j])**3
	if total == i:
		total_armstrong += 1
		print(f"{i} is a Armstrong number:")
	total = 0

print(f"There is {total_armstrong} number in numbers up to {x}")
