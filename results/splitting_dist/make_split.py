import sys
import numpy as np
import random
period = int(sys.argv[1])
sub_rate = float(sys.argv[2])
w_dir = sys.argv[3]
n = int(sys.argv[4])

letters = ['A','C','G','T']

def units_eq(unit1, unit2):
	for i in range(len(unit1)):
		count=0.0
		for j in range(len(unit2)):
			c = (i + j) % len(unit2)
			if unit1[j] == unit2[c]:
				count +=1
		if count / len(unit1) > 0.5:
			return True
	return False

def create_repeat(period):
	unit = []
	for i in range(period):
		unit.append(random.choice(letters))

	return unit

def create_seq(unit, sub_rate, seq_len):
	seq = ''
	rand_numbers = np.random.rand(seq_len)
	for i in range(seq_len):
		if rand_numbers[i] < sub_rate:
			seq += random.choice(letters)
		else:
			seq += unit[i % len(unit)]
	return seq

def create_split_repeat(period, sub_rate, seq_len):
	unit_1 = create_repeat(period)
	unit_2 = create_repeat(period)
	while units_eq(unit_1, unit_2):
		unit_2 = create_repeat(period)
	return create_seq(unit_1, sub_rate, seq_len) + create_seq(unit_2, sub_rate, seq_len)

for i in range(n):
	with open(w_dir + '/' + str(i) + '.fa', 'w') as file:
		file.write(">Period_" + str(period) + "_" + str(sub_rate) + "_" + str(i) + '\n')
		file.write(create_split_repeat(period, sub_rate, 500) + '\n')