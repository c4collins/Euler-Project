number_words = [
	'','one','two',
	'three','four','five',
	'six','seven','eight','nine',
	'ten','eleven','twelve',
	'thirteen','fourteen','fifteen',
	'sixteen','seventeen','eighteen',
	'nineteen','twenty']
	
tens_words = [
	'twenty', 'thirty','forty','fifty',
	'sixty','seventy','eighty','ninety']

length_of_words = 0

for num in range(1,1001):
	tens = str(num)[-2:]
	hundreds = str(num)[-3:-2]
	thousands = str(num)[-4:-3]
	
	if thousands != '':
		print number_words[int(thousands)],
		print "thousand",
		length_of_words += len(number_words[int(thousands)]) + 8
		# the number word length + 8 for "thousand"
		
	if hundreds != '':
		if int(hundreds) > 0:
			print number_words[int(hundreds)],
			print "hundred",
			length_of_words += len(number_words[int(hundreds)]) + 7
			# the number word length + 7 for "hundred"
			
	if int(tens) < 21:
		if int(tens) > 0:
			if hundreds != '':
				print 'and', 
				length_of_words += 3
			print number_words[int(tens)],
			length_of_words += len(number_words[int(tens)])
	else:
		tens_column = tens[-2:-1]
		ones_column = tens[-1:]
		if hundreds != '':
				print 'and',
				length_of_words += 3
		print tens_words[int(tens_column)-2], #because ten is in
		# number_words[], I have to make the tens column match the index, 'thirty'
		# has an index of 1, so if tens_column = 3, then tens_words[3-2] = 'thirty'
		print '-',number_words[int(ones_column)],
		length_of_words += len(tens_words[int(tens_column)-2])
		length_of_words += len(number_words[int(ones_column)])

print
print length_of_words
