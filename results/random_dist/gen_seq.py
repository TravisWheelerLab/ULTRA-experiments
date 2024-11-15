import numpy as np
import sys

file_path = sys.argv[1]
nucs = int(sys.argv[2])
at = float(sys.argv[3])

gc = 1.0 - at
p = [at / 2, gc / 2, gc / 2, at / 2]

seq = np.random.choice(['A', 'C', 'G', 'T'], size=nucs, p=p)

with open(file_path, 'w') as file:
	file.write('>seq ' + str(at))

	for i in range(nucs // 50):
		file.write('\n')
		file.write(''.join(seq[i*50:(i*50) + 50]))

