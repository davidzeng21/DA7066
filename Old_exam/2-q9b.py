def my_special_sum(lis):
	total = 0
	for i in range(len(lis)):
		if type(lis[i]) != int:
			print(f'invalid datatype at list at index: {i}')
			continue
		if lis[i] % 2 == 0:
			total += lis[i]
		else:
			total -= lis[i]
	return total

print(my_special_sum([7.0,6,2,4]))
print(my_special_sum([1,'1',1,1,True]))
