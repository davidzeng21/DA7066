def my_special_sum(lis):
	total = 0
	for num in lis:
		if num % 2 == 1:
			num = -num
		total += num
	return total

print(my_special_sum([6,2,4]))
print(my_special_sum([2,3,4]))
print(my_special_sum([1,1,1]))